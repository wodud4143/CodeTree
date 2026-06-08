from itertools import combinations, permutations
import sys

N, S = map(int, input().split())
arr = list(map(int, input().split()))

result = sys.maxsize
# Please write your code here.
combi = list(combinations(arr, N-2))

for i in combi:
    x = abs(S - sum(i))
    result = min(result, x)


print(result)

