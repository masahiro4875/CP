n, x = map(str, input().split())
n = int(n)

if x == "A":
    sheetnum = 0
elif x == "B":
    sheetnum = 1
elif x == "C":
    sheetnum = 2
elif x == "D":
    sheetnum = 3
elif x == "E":
    sheetnum = 4

for i in range(n):
    s = list(input())
    for j in range(5):
        if j == sheetnum and s[j] == "o":
            print("Yes")
            exit()

print("No")
