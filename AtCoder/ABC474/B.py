N = int(input())

P = [x for x in map(int, input().split())]

ans = True
count = 0

for i in range(len(P)):
    count = i // 10 + 1
    if not max((count - 1) * 10, 1) <= P[i] <= count * 10:
        ans = False
        break

if ans:
    print("Yes")
else:
    print("No")
