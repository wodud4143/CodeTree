a, b = map(int, input().split())
n = input()

# Please write your code here.
num = int(str(n),int(a))
answer = ""
while num > 0:
   answer += str(num % int(b))
   num //= int(b)

print(answer[::-1]) 
