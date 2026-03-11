# Data Analyst Test Assignment — Solutions

> **Candidate:** Mukhtar Muhsin  
> **Stack:** Python · SQL  
> **Date:** March 2026

---

## Repository Structure

```
├── block1/   Probability Theory & Logic
├── block2/   Python Algorithms
├── block3/   SQL
├── block4/   Statistics & A/B Tests
└── block5/   ML Base
```

---

## Block 1 — Probability Theory

| Task | Method | Answer |
|------|--------|--------|
| Farmer (expected distinct species) | Indicator variables + linearity of expectation | **3.99** |
| Cooking competition (expected winners) | Independent events, linearity of expectation | **20.0** |
| Lonely road (car probability) | Exponential scaling of no-event probability | **63.2%; 93.3%** |

---

## Block 2 — Python Algorithms

| Task | Time Complexity | Space Complexity |
|------|----------------|-----------------|
| Isomorphic strings | O(n) | O(k), k = alphabet size |
| Missing number | O(n) | O(1) |
| Prime factorization | O(√n) | O(log n) |

**Run all solutions:**
```bash
python block2/solutions.py
```

---

## Block 3 — SQL

| Task | Key Concept |
|------|-------------|
| Applicant ranking | `RANK() OVER (ORDER BY scores DESC)` |
| FULL JOIN row range | Minimum 30, maximum 50 rows |
| Purchases last month | `JOIN` + `GROUP BY` + `HAVING SUM(...) < 5000` |

---

## Block 4 — Statistics & A/B Tests

| Task | Answer |
|------|--------|
| Samokat rollout | Statements 2, 3, 4 are correct — test is not nationally representative |
| p-value definition | Probability of observing this result (or more extreme), given H₀ is true |
| t-test on lognormal | ✅ Yes — Central Limit Theorem applies at n > 5,000,000 |

---

## Block 5 — ML Base

| Task | Answer |
|------|--------|
| Model with AUC = 0.1 | Take it, invert predictions → effective AUC = **0.9** |
| Manual ROC-AUC | **0.75** |
| Pearson correlation (coffee vs score) | **−0.85** — strong negative, but correlation ≠ causation |

---

## How to Run

```bash
# Clone the repo
git clone https://github.com/<your-username>/da-test-assignment
cd da-test-assignment

# No external libraries required — only Python standard library
python block1/solutions.py
python block2/solutions.py
python block4/solutions.py
python block5/solutions.py

# SQL solutions are in block3/solutions.sql
```

---

## Notes

- All Python solutions use **only the standard library** — no external dependencies.
- SQL dialect: **PostgreSQL** (`DATE_TRUNC`, `INTERVAL`).
- Each solution file contains inline comments explaining the reasoning and complexity analysis.
