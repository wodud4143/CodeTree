n, m = map(int, input().split())

# Please write your code here.

min_ = 1

for i in range(2,min(n,m)+1):
    if n % i ==0 and m % i == 0:
        min_ = i

print((n*m)//(min_))