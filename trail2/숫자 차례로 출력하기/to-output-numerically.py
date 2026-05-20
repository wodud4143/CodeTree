n = int(input())

# Please write your code here.
def tmp(n):
    if n == 0:
        return
    tmp(n-1)
    print(n, end =" ") 

def tmp2(n):
    if n == 0:
        return
    print(n, end =" ") 
    tmp2(n-1)

tmp(n)
print()
tmp2(n)