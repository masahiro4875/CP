N, K, M = map(int, input().split())
jewel_list = [[] for _ in range(N + 1)]

for i in range(N):
    C, V = map(int, input().split())
    jewel_list[C].append(V)

top_jewel = []
tail_jewel = []

for l in jewel_list:
    if len(l) > 0:
        l.sort(reverse=True)
        top_jewel.append(l[0])
        tail_jewel += l[1:]

top_jewel.sort(reverse=True)
tail_jewel+=top_jewel[M:]
tail_jewel.sort(reverse=True)

print(sum(top_jewel[:M]) + sum(tail_jewel[: K - M]))
