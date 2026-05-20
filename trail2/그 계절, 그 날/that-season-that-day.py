Y, M, D = map(int, input().split())

# Please write your code here.

days = [0,31,29,31,30,31,30,31,31,30,31,30,31]

yoon = True

if Y % 4 == 0:
    yoon = True
    if Y % 100 == 0:
        yoon = False
        if Y % 400 == 0:
            yoon = True

else :
    yoon = False


if yoon == False and M == 2 and 29 <= D:
    print(-1)
else:
    if 3 <= M <= 5 :
        if D <= days[M]:
            print("Spring")
        else :
            print(-1)
    if 6 <= M <= 8 :
        if D <= days[M]:
            print("Summer")
        else :
            print(-1)
    if 9 <= M <= 11 :
        if D <= days[M]:
            print("Fall")
        else :
            print(-1)
    if M == 12 or 1<= M <= 2 :
        if D <= days[M]:    
            print("Winter")
        else :
            print(-1)

