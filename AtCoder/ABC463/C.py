import heapq

n = int(input())
takahashi = [[0, 0]] * n
for i in range(n):
    takahashi[i][0], takahashi[i][1] = map(int, input().split())
q = int(input())

for t in input().split():

