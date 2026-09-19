import heapq

N = int(input())
A = [int(x) for x in input().split()]

result = []
a = 0
b = 0
c = 0
for k in range(2, N):
    if k == 2:
        result = sorted(A[: k + 1], reverse=True)
        a = result[0]
        b = result[1]
        c = result[2]
        print(c)
    else:
        if c >= A[k]:
            print(c)
        elif b >= A[k] and A[k] > c:
            c = A[k]
            print(c)
        elif a >= A[k] and A[k] > b:
            c = b
            b = A[k]
            print(c)
        elif A[k] > a:
            c = b
            b = a
            a = A[k]
            print(c)
