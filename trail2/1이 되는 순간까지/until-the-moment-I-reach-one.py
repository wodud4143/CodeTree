N = int(input())

# Please write your code here.

def tmp(N,cnt):
    
    if N == 1:
        return cnt
    
    if N % 2 == 0:
        N //= 2
        return tmp(N, cnt+1)
    else :
        N //= 3
        return tmp(N, cnt+1)



print(tmp(N,0))