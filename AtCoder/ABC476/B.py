N = int(input())
S = list(str(input()))
T = list(str(input()))

T_not_ast = [x for x in T if x != "*"]

is_ok = False
count = 0

for i in range(N):
    if T[i] != "*":
        if S[i] != T[i]:
            break
        else:
            count += 1

if count == len(T_not_ast):
    is_ok =True

if is_ok:
    print("Yes")
else:
    print("No")
