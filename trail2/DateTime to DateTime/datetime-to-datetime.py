a, b, c = map(int, input().split())

# Please write your code here.
day, hour, min = 11, 11, 11

start = 11 * 24 * 60 + 11 * 60 + 11
end = a * 24 * 60 + b * 60 + c

if end - start < 0 :
    print(-1)
else :
    print(end - start)
