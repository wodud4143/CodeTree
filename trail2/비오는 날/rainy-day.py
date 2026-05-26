n = int(input())
date = []
day = []
weather = []
result = []

for i in range(n):
    d, dy, w = input().split()
    date.append(d)
    day.append(dy)
    weather.append(w)
    result.append([d,dy,w])

# Please write your code here.
result.sort()

for i in range(len(result)):
    if result[i][2] == 'Rain' :
        print(*result[i])
        break