N, M = map(int, input().split())

day_dict = {}
for i in range(M):
    day = i + 1
    day_dict[day] = []
# print(day_dict)

color_set = set()
for _ in range(N):
    a, d, b = map(int, input().split())
    if a == b:
        continue
    day_dict[d].append([a, b])
    if d == 1:
        a = b
    color_set.add(a)
print(day_dict)
# print(color_set)

for k, v in day_dict.items():
    print(f"day {k}")
    if k == 1:
        print(len(color_set))
        print(color_set)
        continue
    if not v:
        print(len(color_set))
        print(color_set)
        continue
    for vv in v:
        a, b = vv
        color_set.remove(a)
        color_set.add(b)
    print(len(color_set))
    print(color_set)
