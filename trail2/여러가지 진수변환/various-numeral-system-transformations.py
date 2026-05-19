N, B = map(int, input().split())

# Please write your code here.

answer =""

while True:
    if N == 0 :
        break
    answer += str(N % B)
    N = N//B



print(answer[::-1])


