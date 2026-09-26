N, M, C = map(int, input().split())
B = [int(x) for x in input().split()]

A = []

count = 0

for i in range(N):
    A = [int(x) for x in input().split()]
    result = 0

    for j in range(M):
        result += A[j] * B[j]

    if result + C > 0:
        count += 1

print(count)
