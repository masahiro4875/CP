S = list(input())

b_count = 0
ans = 0

for c in S:
    if c == "B":
        b_count += 1
    else:
        ans += b_count

print(ans)
