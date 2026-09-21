import heapq

N, K = map(int, input().split())
A = [int(x) for x in input().split()]

heap = A[:K]
heapq.heapify(heap)

for x in A[K:]:
    if x > heap[0]:
        heapq.heapreplace(heap, x)

    print(heap[0])
