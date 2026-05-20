N = int(input())

# Please write your code here.
sum = 0

def tmp(N):
    global sum
    if N == 0:
        return
    tmp(N-1)
    sum += N
    return sum

print(tmp(N))

