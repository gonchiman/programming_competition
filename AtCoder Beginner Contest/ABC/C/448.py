from collections import defaultdict
import heapq

n, q = map(int, input().split())
a = list(map(int, input().split()))
queries = list()
for _ in range(q):
    k = int(input())
    b = list(map(int, input().split()))
    queries.append((k, b))

a_dict = defaultdict(int)
for aa in a:
    a_dict[aa] += 1
# a_dict = dict(a_dict)
# print(a_dict)

a_set = set(a_dict.keys())
# print(a_set)

for k, b in queries:
    a_dict_copy = a_dict.copy()
    a_set_copy = a_set.copy()

    for bb in b:
        temp = a[bb-1]
        if a_dict_copy[temp] == 0:
            continue
        a_dict_copy[temp] -= 1
        if a_dict_copy[temp] == 0:
            a_set_copy.remove(temp)
    
    heap = list(a_set_copy)
    heapq.heapify(heap)
    heap: heapq
    print(heap[0])