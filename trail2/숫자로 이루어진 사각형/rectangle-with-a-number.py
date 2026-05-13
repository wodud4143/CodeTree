n = int(input())

# Please write your code here.


def matrix(n):
    num = 0
    for i in range(n):
        if i >= 1:
            print()
        for _ in range(n):
            if num == 9 :
                num = 0
            num += 1
            print(num, end=" ")

matrix(n)