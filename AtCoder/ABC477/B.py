N, D = map(int, input().split())
X = [int(x) for x in input().split()]

count = 0
P = []

for i in range(N):
    count_j = 0
    for j in range(N):
        if i != j and abs(X[i] - X[j]) >= D:
            count_j += 1

    if count_j == N - 1:
        count += 1
        P.append(i + 1)

print(count)
print(*P)
