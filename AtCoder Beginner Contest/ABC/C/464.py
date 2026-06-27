N, M = map(int, input().split())

day_dict = {}
for i in range(M):
    day = i + 1
    day_dict[day] = []
# print(day_dict)

color_dict = {}
for i in range(N):
    color = i + 1
    color_dict[color] = 0

for _ in range(N):
    a, d, b = map(int, input().split())
    if a == b:
        color_dict[a] += 1
        continue
    day_dict[d].append([a, b])
    if d == 1:
        a = b
    color_dict[a] += 1
# print(day_dict)
# print(color_dict)

res = 0
for k, v in color_dict.items():
    if color_dict[k] != 0:
        res += 1
# print(res)

for k, v in day_dict.items():
    # print(f"day {k}")
    if k == 1:
        print(res)
        continue
    if not v:
        print(res)
        continue
    for vv in v:
        a, b = vv
        color_dict[a] -= 1
        if color_dict[a] == 0:
            res -= 1
        color_dict[b] += 1
        if color_dict[b] == 1:
            res += 1
    print(res)
