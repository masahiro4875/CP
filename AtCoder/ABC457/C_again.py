N, K = map(int, input().split())
L = []
A = []

for i in range(N):
    temp = list(map(int, input().split()))

    L.append(temp[0])
    A.append(temp[1:])

C = [int(x) for x in input().split()]

total = 0
for i in range(N):
    total += L[i] * C[i]

    if total >= K:
        offset = K - (total - L[i] * C[i])
        index = (offset - 1) % L[i]
        print(A[i][index])
        exit()
