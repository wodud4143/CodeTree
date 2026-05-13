a, b = map(int, input().split())

# Please write your code here.

def three(n):
    while True:
        a = n // 10
        b = n % 10
        if b == 3 or b == 6 or b == 9 or a == 3 or a == 6 or a == 9:
            return True
        n = a
        if n < 10 :
            return False

cnt = 0
for i in range(a,b+1):
    if i % 3 == 0 or three(i) :
        cnt += 1

print(cnt)