import itertools
import math
def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
def combinations_with_replacement_count(n, r):
    return combinations_count(n + r - 1, r)
ans = 0
n = int(input())
n = n-12
print(combinations_with_replacement_count(12, n))