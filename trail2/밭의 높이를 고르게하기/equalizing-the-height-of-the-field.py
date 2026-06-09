N, H, T = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.

cost = [abs(x - H) for x in arr]

result = 10000000000000000000

for i in range(N-T+1):
    sum = 0
    for j in range(i,i+T):
        sum += cost[j]

    result = min(result, sum)

print(result)

        