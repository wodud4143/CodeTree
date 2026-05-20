n = int(input())

# Please write your code here.
def tmp(n):
    if n == 0 :
        return
    print("HelloWorld")
    tmp(n-1)

tmp(n)