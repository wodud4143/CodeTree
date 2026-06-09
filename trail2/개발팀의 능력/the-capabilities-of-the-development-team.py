from itertools import combinations, permutations

arr = list(map(int, input().split()))

# Please write your code here.

combi = list(combinations(arr, 2))

result = []
idx = range(5)
for team1 in combinations(idx, 2):
    remain1 = [i for i in idx if i not in team1]

    for team2 in combinations(remain1, 2):
        one = [i for i in remain1 if i not in team2]

        score1 = arr[team1[0]] + arr[team1[1]]
        score2 = arr[team2[0]] + arr[team2[1]]
        score3 = arr[one[0]]

        scores = [score1, score2, score3]

        if len(set(scores)) == 3:
            result.append(max(scores) - min(scores))

if len(result) == 0:
    print(-1)
else:
    print(min(result))

