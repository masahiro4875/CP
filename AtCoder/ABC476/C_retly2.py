N = int(input())
A = [int(x) for x in input().split()]

a, b = sorted(A[:2], reverse=True)
print(b)

for x in A[2:]:
    if x > a:
        a, b = x, a
    elif x > b:
        b = x

    print(b)
