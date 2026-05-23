x = int(input())
q = int(input())

A = [0] * q
B = [0] * q

for i in range(q):
    A[i], B[i] = map(int, input().split())

num_list = []
num_list.append(x)

for i in range(q):
    num_list.append(A[i])
    num_list.append(B[i])
    sort_list = sorted(num_list)
    print(sort_list[((len(num_list) - 1) + 1 )// 2])
