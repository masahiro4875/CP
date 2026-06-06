n, m = map(int, input().split())

count = 0
x = m
for i in range(n):
    x = n % x
    count += 1
    if x == 0:
        break

print(count)
