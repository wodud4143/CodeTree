n, k = map(int, input().split())
commands = [tuple(map(int, input().split())) for _ in range(k)]

# Please write your code here.
tmp = [0] * n
for i in range(len(commands)):
    for j in range(commands[i][0],commands[i][1]+1):
        tmp[j-1] += 1

print(max(tmp))