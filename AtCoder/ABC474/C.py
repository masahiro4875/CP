N, Q = map(int, input().split())
P = dict([[x, 1] for x in map(int, input().split())])

for i in range(Q):
    a = int(input())
    del P[a]
    P[a] = 1

print(*P.keys())
