n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
arr.sort()


mul1 = arr[0] * arr[1] * arr[-1]
mul2 = arr[-3] * arr[-2] * arr[-1]

print(max(mul1,mul2))


