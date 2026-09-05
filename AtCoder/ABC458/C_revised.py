s = str(input())
n = len(s)

count = 0
for i, c in enumerate(s):
    if c == "C":
        count += min(i + 1, len(s) - i)

print(count)
