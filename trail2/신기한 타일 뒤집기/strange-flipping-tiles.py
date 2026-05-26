n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []
for num, direction in commands:
    x.append(int(num))
    dir.append(direction)

# Please write your code here.

tiles = {}

cur = 0

for a,b in zip(x,dir):

    if b == 'R':
        for i in range(a):
            tiles[cur + i] = 'B'
        cur += (a-1)

    if b == 'L':
        for i in range(a):
            tiles[cur - i] = 'W'
        cur -= (a-1)

W,B = 0,0

for c in tiles.values():
    if c == 'W':
        W += 1
    else:
        B += 1

print(W, B)


