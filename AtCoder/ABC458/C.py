s = str(input())

count = 0

if "C" not in s:
    print(0)
    exit()
else:
    for i in range(len(s)):
        if s[i] == "C":
            count += min(i + 1, len(s) - i)

print(count)
