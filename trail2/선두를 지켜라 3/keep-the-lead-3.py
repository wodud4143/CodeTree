N, M = map(int, input().split())

# Process A's movements
v = []
t = []
for _ in range(N):
    vi, ti = map(int, input().split())
    v.append(vi)
    t.append(ti)

# Process B's movements
v2 = []
t2 = []
for _ in range(M):
    vi, ti = map(int, input().split())
    v2.append(vi)
    t2.append(ti)

# Please write your code here.

A = [x for x, y in zip(v, t) for _ in range(y)]
B = [x for x, y in zip(v2, t2) for _ in range(y)]
Max = ''
cnt = 0
a_dist, b_dist = 0, 0

for idx, (a,b) in enumerate(zip(A,B)):
    a_dist += a
    b_dist += b
    if a_dist == b_dist and Max !='AB':
        Max = 'AB'
        cnt += 1
    elif a_dist > b_dist and Max !='A':
        Max = 'A'
        cnt +=1
    elif a_dist < b_dist and Max !='B':
        Max ='B'
        cnt +=1

print(cnt)
