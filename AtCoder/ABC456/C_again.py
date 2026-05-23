S = list(str(input()))

answer = 0
count = 0
for i in range(len(S)):
    count += 1

    if i + 1 == len(S):
        answer += count * (count + 1) // 2
    elif S[i] == S[i + 1]:
        answer += count * (count + 1) // 2
        count = 0

print(answer % 998244353)
