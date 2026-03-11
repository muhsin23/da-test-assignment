"""
Block 2: Python Algorithms
====================================
Task 1 - Isomorphic Strings
Task 2 - Missing Number
Task 3 - Prime Factorization
"""


# ── Task 1: Isomorphic Strings ────────────────────────────────────────────────
# Two strings are isomorphic if characters in s can be replaced to get t,
# with a strict one-to-one mapping (no two chars map to the same char).
#
# Approach: maintain two dicts — s->t and t->s — for bidirectional mapping.
# Time:  O(n)  — single pass through both strings
# Space: O(k)  — where k = alphabet size (constant for ASCII, max 256)

def is_isomorphic(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    s_to_t = {}
    t_to_s = {}

    for cs, ct in zip(s, t):
        if cs in s_to_t:
            if s_to_t[cs] != ct:        # mapping conflicts
                return False
        else:
            if ct in t_to_s:            # another char already maps to ct
                return False
            s_to_t[cs] = ct
            t_to_s[ct] = cs

    return True


# ── Task 2: Missing Number ────────────────────────────────────────────────────
# Find the single missing number in the sequence 1, 2, ..., n.
#
# Approach: expected sum of 1..n = n*(n+1)/2. Subtract actual sum.
# Time:  O(n)  — one pass for sum()
# Space: O(1)  — no extra data structures

def missing_number(nums: list) -> int:
    n = len(nums) + 1                   # full sequence would have n elements
    expected_sum = n * (n + 1) // 2
    return expected_sum - sum(nums)


# ── Task 3: Prime Factorization ───────────────────────────────────────────────
# Decompose a natural number n into its prime factors.
#
# Approach: trial division up to sqrt(n). Divide out each factor completely,
# then move to the next candidate. Any remainder > 1 is itself prime.
# Time:  O(sqrt(n))
# Space: O(log n)  — number of prime factors is at most log2(n)

def prime_factors(n: int) -> list:
    factors = []
    d = 2

    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1

    if n > 1:                           # n itself is prime
        factors.append(n)

    return factors


# ── Run & Print Answers ───────────────────────────────────────────────────────
if __name__ == "__main__":
    print("=" * 50)
    print("BLOCK 2: Python Algorithms")
    print("=" * 50)

    print("\nTask 1 — Isomorphic Strings")
    print(f"  is_isomorphic('paper', 'title') = {is_isomorphic('paper', 'title')}")  # True
    print(f"  is_isomorphic('foo', 'bar')     = {is_isomorphic('foo', 'bar')}")      # False
    print(f"  is_isomorphic('ab', 'aa')       = {is_isomorphic('ab', 'aa')}")        # False

    print("\nTask 2 — Missing Number")
    nums = [1, 2, 3, 4, 5, 6, 8, 9, 10, 11]
    print(f"  missing_number({nums}) = {missing_number(nums)}")  # 7

    print("\nTask 3 — Prime Factorization")
    print(f"  prime_factors(56)  = {prime_factors(56)}")    # [2, 2, 2, 7]
    print(f"  prime_factors(100) = {prime_factors(100)}")   # [2, 2, 5, 5]
    print(f"  prime_factors(13)  = {prime_factors(13)}")    # [13]
