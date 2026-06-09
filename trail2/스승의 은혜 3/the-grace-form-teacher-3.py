from itertools import permutations
import copy

N, B = map(int, input().split())
gifts = [tuple(map(int, input().split())) for _ in range(N)]
P = [gift[0] for gift in gifts]
S = [gift[1] for gift in gifts]

# Please write your code here.
result = 0

for i in range(N):
    costs = []

    for j in range(N):
        p, s = gifts[j]

        if i == j:
            p //= 2

        costs.append(p + s)

    costs.sort()

    total = 0
    cnt = 0

    for cost in costs:
        if total + cost <= B:
            total += cost
            cnt += 1
        else:
            break

    result = max(result, cnt)

print(result)