m1, d1, m2, d2 = map(int, input().split())
A = input()

# Please write your code here.

days = ['Mon', 'Tue','Wed','Thu','Fri','Sat','Sun']

month = [0,31,29,31,30,31,30,31,31,30,31,30,31]

day1 = sum(month[:m1]) + d1
day2 = sum(month[:m2]) + d2

day1 = day1 + days.index(A)
diff = day2 - day1
if diff < 0:
    print(0)
elif diff == 0 :
    print(1)
else :
    print((diff // 7)+1)



