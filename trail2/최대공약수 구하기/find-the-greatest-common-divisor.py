n, m = map(int, input().split())

# Please write your code here.
max_ = 1



for i in range(2, max(n,m)+1):
    if n % i == 0 and m % i == 0:
        max_  = i
print(max_)