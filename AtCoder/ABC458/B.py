n, w = map(int, input().split())

x = [[0] * w for _ in range(n)]

for i in range(n):
    for j in range(w):
        for k in range(n):
            for l in range(w):
                if abs(i - k) + abs(j - l) == 1:
                    x[i][j] += 1

for i in range(n):
    print(*x[i])
