n, t = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
cnt = 0
max_= 0
for i in range(len(arr)) :
    if arr[i] > t :
        cnt += 1
    else :
        if cnt > max_:
            max_ = cnt
        cnt = 0
if max_ == 0 and cnt:
    max_ = cnt
print(max_)
