n = int(input())
A = list(map(int, input().split()))

# Please write your code here.
result = []
for i in range(len(A)):
    sum = 0
    for j in range(len(A)):
        if i == j :
            continue
        sum += A[j] * abs(j-i)
    result.append(sum)

        
print(min(result))
