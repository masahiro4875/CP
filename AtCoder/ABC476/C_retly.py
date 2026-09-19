N = int(input())
A = [int(x) for x in input().split()]

a, b, c = sorted(A[:3], reverse=True)
print(c)

for x in A[3:]:
    if x > a:
        a, b, c = x, a, b
    elif x > b:
        b, c = x, b
    elif x > c:
        c = x

    print(c)
