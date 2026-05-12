m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.
num_days = [31,28,31,30,31,30,31,31,30,31,30,31]

day1 = sum(num_days[:m1-1]) + d1

day2 = sum(num_days[:m2-1]) + d2

print(day2 - day1 + 1)

