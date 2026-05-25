N = int(input())

# Please write your code here.
sum = 0
while N > 0:
    sum += (N % 10) ** 2
    N = N // 10

print(sum)
