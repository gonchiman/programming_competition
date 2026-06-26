import sys
input = sys.stdin.readline


N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]

item_dict = {}
for i in range(N):
    item_dict[i + 1] = []

for ab in AB:
    a, b = ab
    item_dict[a].append(b)

item_set = set()
item_set.add(1)
for key in item_dict:
    item_set.update(item_dict[key])

res = len(item_set)


print(res)