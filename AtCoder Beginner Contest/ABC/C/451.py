q = int(input())
queries = [list(map(int, input().split())) for _ in range(q)]


max_height = 0
for query in queries:
    x, y = query
    if x == 1:
        if y > max_height:
            max_height = y
# print(max_height)

tree_dict_by_height = {}
for i in range(max_height):
    i = i + 1
    tree_dict_by_height[i] = 0
# print(tree_dict_by_height)

for query in queries:
    x, y = query
    if x == 1:
        tree_dict_by_height[y] += 1
# print(tree_dict_by_height)

threshold = 0
for query in queries:
    x, y = query
    if x == 2:
        if y > threshold:
            threshold = y
print(threshold)