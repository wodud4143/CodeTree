n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
tmp = {}
for x1,x2 in segments:
    for j in range(x1,x2):
        tmp[j] = tmp.get(j,0) + 1

print(max(tmp.values()))

