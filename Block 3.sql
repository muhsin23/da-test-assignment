-- ============================================================
-- Block 3: SQL
-- ============================================================


-- ── Task 1: Applicant Rankings ───────────────────────────────
-- Rank applicants by their exam score (highest score = rank 1).
-- RANK() is used instead of ROW_NUMBER() so that tied scores
-- receive the same position (fair ranking).

SELECT
    id,
    scores,
    RANK() OVER (ORDER BY scores DESC) AS position
FROM examination;


-- ── Task 2: FULL JOIN Row Count Range ────────────────────────
-- Table A: 30 rows | Table B: 20 rows
--
-- MINIMUM (all keys match 1-to-1):
--   20 rows match perfectly → 20 joined rows
--   10 rows from A have no match → 10 rows with NULLs from B
--   Result: 30 rows
--
-- MAXIMUM (no keys match at all):
--   All 30 rows from A appear with NULLs
--   All 20 rows from B appear with NULLs
--   Result: 30 + 20 = 50 rows
--
-- Answer: minimum 30 and maximum 50 rows


-- ── Task 3: Purchases Last Month ─────────────────────────────
-- Find client IDs whose total purchases across ALL accounts
-- in the previous calendar month sum to less than 5000 RUB.
-- No subqueries or window functions allowed.

SELECT
    a.client_id
FROM account a
JOIN transaction t
    ON t.account_id = a.id
WHERE
    t.transaction_date >= DATE_TRUNC('month', CURRENT_DATE - INTERVAL '1 month')
    AND t.transaction_date <  DATE_TRUNC('month', CURRENT_DATE)
    AND t.type = 'buy'
GROUP BY
    a.client_id
HAVING
    SUM(t.amount) < 5000;

-- Note: DATE_TRUNC('month', ...) gives the first day of the month,
-- so the WHERE clause captures exactly the previous calendar month.
-- HAVING filters on the aggregated sum — this is why WHERE alone
-- cannot be used here (WHERE runs before GROUP BY).
