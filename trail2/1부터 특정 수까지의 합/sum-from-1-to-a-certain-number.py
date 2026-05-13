n = int(input())

# Please write your code here.
def solve(n):
    num = 0
    for i in range(1,n+1):
        num += i
    print(num // 10)

solve(n)