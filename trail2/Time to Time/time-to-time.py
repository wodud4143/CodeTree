a, b, c, d = map(int, input().split())

# Please write your code here.

hour = a
min = b

elapsed_time = 0

while True :
    if hour == c and min == d :
        break
    min += 1

    if min == 60:
        hour += 1
        min = 0

    elapsed_time += 1

print(elapsed_time)