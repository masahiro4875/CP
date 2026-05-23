n = int(input())

s = [str(x) for x in input().split()]
c = []

for string in s:
    if string[0] == "a" or string[0] == "b" or string[0] == "c":
        c.append(2)
    elif string[0] == "d" or string[0] == "e" or string[0] == "f":
        c.append(3)
    elif string[0] == "g" or string[0] == "h" or string[0] == "i":
        c.append(4)
    elif string[0] == "j" or string[0] == "k" or string[0] == "l":
        c.append(5)
    elif string[0] == "m" or string[0] == "n" or string[0] == "o":
        c.append(6)
    elif string[0] == "p" or string[0] == "q" or string[0] == "r" or string[0] == "s":
        c.append(7)
    elif string[0] == "t" or string[0] == "u" or string[0] == "v":
        c.append(8)
    else:
        c.append(9)

print(*c, sep="")
