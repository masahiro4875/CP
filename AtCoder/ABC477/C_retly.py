Q = int(input())
S = input()
T = input()

N = len(S)
M = len(T)

match = [0] * N

for i in range(N - M + 1):
    if S[i : i + M] == T:
        match[i] = 1

cum = [0] * (N + 1)

for i in range(N):
    cum[i + 1] = cum[i] + match[i]

for _ in range(Q):
    L, R = map(int, input().split())

    if R - L + 1 < M:
        print("No")
        continue

    left = L - 1
    right = R - M

    count = cum[right + 1] - cum[left]

    if count > 0:
        print("Yes")
    else:
        print("No")
