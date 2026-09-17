S = str(input())
S = list(S)

count_B = 0
count = 0

for x in S:
    if x == "B":
        count_B += 1
    else:
        count += count_B

print(count)
