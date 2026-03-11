"""
Block 5: ML Base
====================================
Task 1 - Model selection (ROC-AUC 0.1 vs 0.7)
Task 2 - Manual ROC-AUC calculation
Task 3 - Manual Pearson correlation
"""

import math


# ── Task 1: Pony vs Horse — Which model to pick? ─────────────────────────────
# Model A: ROC-AUC = 0.7
# Model B: ROC-AUC = 0.1
#
# ROC-AUC = 0.5 → random classifier (coin flip)
# ROC-AUC = 0.1 → the model is CONSISTENTLY WRONG
#
# A model that is consistently wrong is actually very useful:
# just INVERT its predictions (swap 0s and 1s) → AUC becomes 1 - 0.1 = 0.9
#
# So we take Model B (AUC=0.1), invert predictions → effective AUC = 0.9

TASK1_ANSWER = """
Take the model with ROC-AUC = 0.1 and invert its predictions.
Inverted AUC = 1 - 0.1 = 0.9, which outperforms the 0.7 model.

Intuition: a model that is always wrong is as informative as one that
is always right — you just need to flip the output labels.
"""


# ── Task 2: Manual ROC-AUC Calculation ───────────────────────────────────────
# Given predicted probabilities and true labels, calculate ROC-AUC.
#
# Steps:
#   1. Sort samples by predicted probability (descending)
#   2. For each threshold, calculate TPR and FPR
#   3. Plot ROC curve points
#   4. Calculate area under the curve (trapezoid rule)
#
# TPR = TP / (TP + FN)  = true positive rate (sensitivity)
# FPR = FP / (FP + TN)  = false positive rate (1 - specificity)

def calculate_roc_auc(true_labels: list, probabilities: list) -> float:
    # Sort by probability descending
    pairs = sorted(zip(probabilities, true_labels), reverse=True)

    P = sum(true_labels)        # total positives
    N = len(true_labels) - P    # total negatives

    tps, fps = 0, 0
    roc_points = [(0.0, 0.0)]   # start at origin

    for prob, label in pairs:
        if label == 1:
            tps += 1
        else:
            fps += 1
        roc_points.append((fps / N, tps / P))

    # Area under curve via trapezoid rule
    auc = 0.0
    for i in range(1, len(roc_points)):
        x1, y1 = roc_points[i - 1]
        x2, y2 = roc_points[i]
        auc += (x2 - x1) * (y1 + y2) / 2

    return round(auc, 2)


# ── Task 3: Pearson Correlation ───────────────────────────────────────────────
# Measure linear relationship between cups of coffee and exam score.
#
# Formula:
#   r = Σ[(xi - x̄)(yi - ȳ)] / (std_x * std_y)
#
# r close to  1 → strong positive linear relationship
# r close to -1 → strong negative linear relationship
# r close to  0 → no linear relationship
#
# IMPORTANT: correlation ≠ causation.
# A third variable (e.g. sleep deprivation) may explain both.

def pearson_correlation(x: list, y: list) -> float:
    n = len(x)
    mean_x = sum(x) / n
    mean_y = sum(y) / n

    numerator = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(n))
    std_x = math.sqrt(sum((xi - mean_x) ** 2 for xi in x))
    std_y = math.sqrt(sum((yi - mean_y) ** 2 for yi in y))

    return round(numerator / (std_x * std_y), 2)


# ── Run & Print Answers ───────────────────────────────────────────────────────
if __name__ == "__main__":
    print("=" * 50)
    print("BLOCK 5: ML Base")
    print("=" * 50)

    print("\nTask 1 — Model Selection")
    print(TASK1_ANSWER)

    # Task 2 data
    true_labels  = [1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0]
    probabilities = [0.95, 0.9, 0.85, 0.8, 0.75, 0.7, 0.65, 0.6,
                     0.55, 0.5, 0.45, 0.4, 0.35, 0.3, 0.25]

    auc = calculate_roc_auc(true_labels, probabilities)
    print(f"Task 2 — Manual ROC-AUC")
    print(f"  ROC-AUC = {auc}")

    # Task 3 data
    coffee = [1, 1, 2, 2, 2, 2, 3, 3, 3, 4]
    scores = [85, 88, 79, 81, 84, 65, 67, 58, 76, 49]

    r = pearson_correlation(coffee, scores)
    print(f"\nTask 3 — Pearson Correlation")
    print(f"  r = {r}")
    print(f"  Interpretation: strong negative correlation.")
    print(f"  More coffee → lower exam score — but this is correlation, NOT causation.")
    print(f"  A confounding variable (e.g. lack of sleep) likely explains both.")
