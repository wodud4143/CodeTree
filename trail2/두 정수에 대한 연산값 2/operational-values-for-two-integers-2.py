a, b = map(int, input().split())

# Please write your code here.

if a > b :
    a *= 2
    b += 10
else :
    b *=2
    a +=10

print(a,b)