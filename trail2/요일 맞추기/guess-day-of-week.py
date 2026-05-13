m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.
days = [0,31,28,31,30,31,30,31,31,30,31,30,31]
T = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']

day1 = sum(days[:m1]) + d1
day2 = sum(days[:m2]) + d2
diff = day2 - day1
print(T[diff % 7])

