# =============================================================================
# Replication Script: Interventions to Reduce Affective Polarization
# =============================================================================
# Columbia University | IRB Protocol: AAAU3946
#
# Reproduces the published results (redesign_site/filedrawer/affective_polarization):
#   - party = the in-party the survey assigned each respondent (group1)
#   - finished responses only; T33 (GPT-3 chatbot, technical failures) excluded
#   - IPW weights = 1 / arm share among all finished respondents (as in analysis.R)
#   - UDP index = mean of the items answered (rowMeans(na.rm = TRUE), as in analysis.R)
#   - WLS: post ~ treatment + pre, HC2 robust SEs, normal-based p-values
# =============================================================================

library(tidyverse)
library(sandwich)  # for vcovHC (robust SEs)
library(lmtest)    # for coeftest

# =============================================================================
# 1. LOAD DATA
# =============================================================================

dat <- read_csv("replication_data.csv", show_col_types = FALSE)

cat("Data loaded:", nrow(dat), "rows,", ncol(dat), "columns\n\n")

# =============================================================================
# 2. SAMPLE AND IPW WEIGHTS
# =============================================================================

# Finished responses with an assigned arm
finished <- dat %>%
  filter(Finished == 1, !is.na(id))

# Assignment probabilities: arm share among all finished respondents
treatment_probs <- finished %>%
  count(id, name = "n_treat") %>%
  mutate(treat_prob = n_treat / nrow(finished),
         ipw_weight = 1 / treat_prob)

cat("Finished respondents:", nrow(finished), "\n")
cat("Treatment counts and weights (all finished respondents):\n")
print(treatment_probs, n = Inf)
cat("\n")

# =============================================================================
# 3. CONSTRUCT MEASURES
# =============================================================================

analysis_data <- finished %>%
  # Party = in-party assigned by the survey (group1)
  mutate(
    is_democrat = group1 == "Democratic",
    is_republican = group1 == "Republican"
  ) %>%
  # Partisans only
  filter(is_democrat | is_republican) %>%
  # Affective polarization: inparty - outparty feeling thermometer
  mutate(
    # *_ap_scores_1 = rating of Republicans, *_ap_scores_2 = rating of Democrats
    pre_inparty = if_else(is_democrat, pre_ap_scores_2, pre_ap_scores_1),
    pre_outparty = if_else(is_democrat, pre_ap_scores_1, pre_ap_scores_2),
    pre_ap = pre_inparty - pre_outparty,

    post_inparty = if_else(is_democrat, post_ap_scores_2, post_ap_scores_1),
    post_outparty = if_else(is_democrat, post_ap_scores_1, post_ap_scores_2),
    post_ap = post_inparty - post_outparty
  ) %>%
  # Support for undemocratic practices (UDP): mean of the items answered (1-7 scale)
  mutate(
    pre_udp = rowMeans(pick(pre_udp_scores_1:pre_udp_scores_4), na.rm = TRUE),
    post_udp = rowMeans(pick(post_udp_scores_1:post_udp_scores_4), na.rm = TRUE),
    pre_udp = if_else(is.nan(pre_udp), NA_real_, pre_udp),
    post_udp = if_else(is.nan(post_udp), NA_real_, post_udp)
  ) %>%
  # Remove T33 (broken intervention)
  filter(id != 33) %>%
  left_join(treatment_probs, by = "id") %>%
  # Treatment factor with T0 (pure control) as reference
  mutate(treatment = relevel(factor(id), ref = "0"))

cat("Analysis sample (finished partisans, excluding T33):", nrow(analysis_data), "\n\n")

# =============================================================================
# 4. ESTIMATION
# =============================================================================

estimate_effects <- function(data, outcome, pre) {
  complete <- data %>% filter(!is.na(.data[[pre]]), !is.na(.data[[outcome]]))
  model <- lm(reformulate(c("treatment", pre), outcome), data = complete, weights = ipw_weight)
  # Normal-based (z) inference, as in the published results
  robust <- coeftest(model, vcov = vcovHC(model, type = "HC2"), df = Inf)
  coefs <- robust[grepl("^treatment", rownames(robust)), ]

  results <- tibble(
    treatment = gsub("treatment", "", rownames(coefs)),
    estimate = coefs[, "Estimate"],
    se = coefs[, "Std. Error"],
    z_value = coefs[, "z value"],
    p_value = coefs[, "Pr(>|z|)"]
  ) %>%
    mutate(ci_lower = estimate - 1.96 * se,
           ci_upper = estimate + 1.96 * se) %>%
    left_join(complete %>% count(treatment) %>% mutate(treatment = as.character(treatment)),
              by = "treatment") %>%
    arrange(estimate)  # most negative (best) first

  list(model = model, complete = complete, results = results)
}

print_results <- function(fit, label, pre) {
  cat(strrep("=", 70), "\n")
  cat(label, "\n")
  cat(strrep("=", 70), "\n\n")
  cat("Complete cases:", nrow(fit$complete), "\n\n")
  fit$results %>%
    select(treatment, n, estimate, se, ci_lower, ci_upper, p_value) %>%
    mutate(across(c(estimate, se, ci_lower, ci_upper), ~round(., 2)),
           p_value = round(p_value, 4)) %>%
    print(n = Inf)
  cat("\nModel R-squared:", round(summary(fit$model)$r.squared, 3), "\n")
  cat("Pre-treatment coefficient:", round(coef(fit$model)[pre], 3), "\n\n")
}

ap <- estimate_effects(analysis_data, "post_ap", "pre_ap")
print_results(ap, "AFFECTIVE POLARIZATION: post_ap ~ treatment + pre_ap (WLS, IPW, HC2)", "pre_ap")

udp <- estimate_effects(analysis_data, "post_udp", "pre_udp")
print_results(udp, "UNDEMOCRATIC PRACTICES: post_udp ~ treatment + pre_udp (WLS, IPW, HC2)", "pre_udp")

write_csv(ap$results, "results_ap.csv")
write_csv(udp$results, "results_udp.csv")

# =============================================================================
# 5. SUMMARY STATISTICS
# =============================================================================

cat(strrep("=", 70), "\n")
cat("SUMMARY STATISTICS\n")
cat(strrep("=", 70), "\n\n")

cat("Total N (complete AP cases):", nrow(ap$complete), "\n")
cat("Total N (complete UDP cases):", nrow(udp$complete), "\n")
cat("Number of treatments (excluding T33 and control):", nrow(ap$results), "\n")
cat("Statistically significant effects (p < 0.05, AP):", sum(ap$results$p_value < 0.05), "\n")
cat("Statistically significant effects (p < 0.05, UDP):", sum(udp$results$p_value < 0.05), "\n")

cat("\nBest performing interventions (AP):\n")
ap$results %>% slice_head(n = 5) %>% select(treatment, n, estimate, p_value) %>% print()

cat("\nWorst performing interventions (AP, potential backfire):\n")
ap$results %>% slice_tail(n = 5) %>% select(treatment, n, estimate, p_value) %>% print()

# =============================================================================
# 6. SESSION INFO
# =============================================================================

cat("\n", strrep("=", 70), "\n")
cat("SESSION INFO\n")
cat(strrep("=", 70), "\n\n")
sessionInfo()
