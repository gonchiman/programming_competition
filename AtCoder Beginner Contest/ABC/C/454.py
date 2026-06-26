import random
import sys
input = sys.stdin.readline


N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]
# candidate = [x for x in range(1, N + 1)]
# AB = list()
# for _ in range(M):
#     a, b = random.sample(candidate, 2)
#     AB.append([a, b])

# print(AB)

item_dict = {}
for i in range(N):
    item_dict[i + 1] = []

for ab in AB:
    a, b = ab
    item_dict[a].append(b)

item_set = set()
def item_counter(x):
    if x in item_set:
        return
    children = item_dict[x]
    if len(children) != 0:
        for child in item_dict[x]:
            item_counter(child)
        item_set.update(children)

item_counter(1)
item_set.add(1)

res = len(item_set)


# print(item_dict)
# print(item_set)
print(res)