"""
Block 1: Probability Theory & Logic
====================================
Task 1 - Farmer
Task 2 - Cooking Competition
Task 3 - Lonely Road
"""

import math


# ── Task 1: Farmer ────────────────────────────────────────────────────────────
# A farmer enters a barn 6 times per day. There are 6 different animal species.
# Each visit, he sees one animal at random.
# What is the expected number of DISTINCT species seen?
#
# Method: Indicator variables.
# For each species, P(seen at least once) = 1 - (5/6)^6
# By linearity of expectation: E = 6 * (1 - (5/6)^6)

def farmer_expected_species(num_species: int, num_visits: int) -> float:
    p_seen = 1 - ((num_species - 1) / num_species) ** num_visits
    return round(num_species * p_seen, 2)


# ── Task 2: Cooking Competition ───────────────────────────────────────────────
# 80 chefs, 2 rounds of random pairs, stronger chef always wins.
# Winners = those who win BOTH rounds.
# P(win round 1) = 1/2, P(win round 2) = 1/2 (independent)
# E = 80 * (1/2) * (1/2)

def cooking_expected_winners(num_chefs: int, num_rounds: int) -> float:
    p_win_all = (1 / 2) ** num_rounds
    return round(num_chefs * p_win_all, 1)


# ── Task 3: Lonely Road ───────────────────────────────────────────────────────
# P(car appears in 30 min) = 0.95
# Find P(appears in 10 min) and P(appears in 27 min)
#
# Logic: P(no car in 30 min) = 0.05
# Since arrivals are a continuous process:
# P(no car in t min) = 0.05^(t/30)
# P(car in t min)    = 1 - 0.05^(t/30)

def road_probability(p_in_base: float, base_minutes: int, query_minutes: int) -> float:
    p_no_car_base = 1 - p_in_base
    p_no_car_t = p_no_car_base ** (query_minutes / base_minutes)
    return round((1 - p_no_car_t) * 100, 1)


# ── Run & Print Answers ───────────────────────────────────────────────────────
if __name__ == "__main__":
    print("=" * 50)
    print("BLOCK 1: Probability Theory")
    print("=" * 50)

    ans1 = farmer_expected_species(num_species=6, num_visits=6)
    print(f"\nTask 1 — Farmer")
    print(f"  E[distinct species] = {ans1}")

    ans2 = cooking_expected_winners(num_chefs=80, num_rounds=2)
    print(f"\nTask 2 — Cooking Competition")
    print(f"  E[winners] = {ans2}")

    ans3_10 = road_probability(p_in_base=0.95, base_minutes=30, query_minutes=10)
    ans3_27 = road_probability(p_in_base=0.95, base_minutes=30, query_minutes=27)
    print(f"\nTask 3 — Lonely Road")
    print(f"  P(10 min) = {ans3_10}%")
    print(f"  P(27 min) = {ans3_27}%")
