N = int(input())

n = int(N / 1.08)

if int(n * 1.08) == N:
    print(n)
elif int((n + 1) * 1.08) == N:
    print(n + 1)
else:
    print(":(")
