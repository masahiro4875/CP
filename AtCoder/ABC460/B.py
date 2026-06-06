from decimal import Decimal

t = int(input())


for i in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    x = str((x1 - x2) ** 2 + (y1 - y2) ** 2)
    d = Decimal(x)**Decimal(0.5)

    if d == abs(r1 - r2) or abs(r1 - r2) < d < r1 + r2 or d == r1 + r2:
        print("Yes")
    else:
        print("No")
