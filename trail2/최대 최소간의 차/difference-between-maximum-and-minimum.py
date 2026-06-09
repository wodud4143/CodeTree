n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.


cost = []
for i in range(min(arr), max(arr)-k+1):
    min_ = i
    max_ = i + k

    sum = 0
    for j in arr:
        if j > max_:
            sum += j - max_ 
        if j < min_ :
            sum += min_ - j
    cost.append(sum)

print(min(cost))   
        




