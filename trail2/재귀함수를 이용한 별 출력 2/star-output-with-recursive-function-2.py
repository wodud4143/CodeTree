n = int(input())

# Please write your code here.
def tmp(n):
    if n == 0 :
        return
    print("* "*n)
    tmp(n-1)
    print("* "*n)

tmp(n)