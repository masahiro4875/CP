N, Q = map(int, input().split())
P = [x for x in map(int, input().split())]
A = []

for i in range(Q):
    A.append(int(input()))

seen = set()
tail = []

for a in reversed(A):
    if a not in seen:
        seen.add(a)
        tail.append(a)

tail.reverse()

ans = []

for x in P:
    if x not in seen:
        ans.append(x)

ans.extend(tail)

print(*ans)
