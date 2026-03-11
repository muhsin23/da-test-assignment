"""
Block 4: Statistics & A/B Tests
====================================
Task 1 - Samokat AB Test (multiple choice)
Task 2 - p-value definition (multiple choice)
Task 3 - t-test applicability with large sample
"""


# ── Task 1: Samokat Delivery Experiment ───────────────────────────────────────
# An AB experiment was run in ONE small town. Results were significant.
# Should the company roll out changes nationally?
#
# Correct answers:
#   ✅ The test is NOT representative of the whole country — don't roll out nationally.
#   ✅ The test IS representative of similar small towns — can apply there.
#   ✅ The effect shows potential — run more experiments in other cities first.
#
# Key principle: Representativeness. A sample is only valid for the population
# it was drawn from. One small town ≠ all of Russia.

TASK1_ANSWER = """
Correct statements:
  2. The test is not representative of the whole country — national rollout is premature.
  3. The test is representative for similar small towns — can apply in comparable cities.
  4. The effect confirms potential — but we should test in more cities before scaling.

Key concept: REPRESENTATIVENESS.
Never extrapolate AB results beyond the population they were sampled from.
"""


# ── Task 2: What is p-value? ──────────────────────────────────────────────────
# Correct definition:
#   "The probability of observing a result this extreme (or more),
#    assuming the null hypothesis is true."
#
# Common misconceptions:
#   ❌ p-value is NOT "the probability that H0 is true"
#   ❌ p-value is NOT the significance level alpha
#   ❌ p-value is NOT the sample mean

TASK2_ANSWER = """
Correct answer:
  The probability of observing such an extreme (or more extreme) result
  given that the null hypothesis is true.

p-value does NOT tell you the probability that H0 is true.
It tells you: "If H0 were true, how surprising would this data be?"
"""


# ── Task 3: Can we use t-test with lognormal distribution? ───────────────────
# Sample size: 5,000,000+ observations per group. No significant outliers.
# Target metric: mean unique purchases per user (lognormal distribution).
#
# Answer: YES, we can use the t-test.
#
# Why? Central Limit Theorem (CLT):
# With very large samples (n >> 30), the SAMPLING DISTRIBUTION of the mean
# converges to normal regardless of the underlying distribution.
# At n = 5,000,000 this convergence is essentially complete.
#
# If sample were small: Mann-Whitney U test would be safer (non-parametric).

TASK3_ANSWER = """
Yes, the t-test is applicable here.

Reason: Central Limit Theorem.
With n > 5,000,000 observations, the distribution of the sample mean
approaches normality regardless of the original data distribution.
The lognormality of individual observations does not prevent us from
using a t-test on the means.

Note: for small samples with lognormal data, Mann-Whitney U test is preferred.
"""


if __name__ == "__main__":
    print("=" * 50)
    print("BLOCK 4: Statistics & A/B Tests")
    print("=" * 50)

    print("\nTask 1 — Samokat AB Test")
    print(TASK1_ANSWER)

    print("\nTask 2 — p-value definition")
    print(TASK2_ANSWER)

    print("\nTask 3 — t-test with lognormal distribution")
    print(TASK3_ANSWER)
