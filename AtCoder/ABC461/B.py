n = int(input())

A=[int(x) for x in input().split()]
B=[int(x) for x in input().split()]

kikori=[[0,0]]*n
megami=[[0,0]]*n

result=True

for i in range(n):
    kikori[i]=[i,A[i]-1]
    megami[i]=[B[i]-1,i]

for i in range(n):
    if kikori[i] not in megami:
        result=False
        break

if result:
    print("Yes")
else:
    print("No")
