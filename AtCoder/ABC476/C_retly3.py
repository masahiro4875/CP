N = int(input())
A = [int(x) for x in input().split()]

a, b, c, d = sorted(A[:4], reverse=True)
print(d)

for x in A[4:]:
    if x > a:
        a, b, c, d = x, a, b, c
    elif x > b:
        b, c, d = x, b, c
    elif x > c:
        c, d = x, c
    elif x > d:
        d = x

    print(d)
