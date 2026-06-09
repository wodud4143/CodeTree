N, T = map(int, input().split())
str = input()
board = [list(map(int, input().split())) for _ in range(N)]

# Please write your code here.
x, y = N // 2, N // 2
result = board[x][y]

dir = 0

for c in str:
    if c == 'L':
        dir  = (dir  - 90) % 360

    elif c == 'R':
        dir  = (dir  + 90) % 360

    elif c == 'F':
        if dir == 0:      
            nx, ny = x - 1, y
        elif dir == 90:   
            nx, ny = x, y + 1
        elif dir == 180:  
            nx, ny = x + 1, y
        else:                   
            nx, ny = x, y - 1

        if 0 <= nx < N and 0 <= ny < N:
            x, y = nx, ny
            result += board[x][y]

print(result)