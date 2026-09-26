Q = int(input())
S = str(input())
T = str(input())

for i in range(Q):
    L, R = map(int, input().split())
    S_delete = S[L - 1 : R]

    if T in S_delete:
        print("Yes")
    else:
        print("No")
