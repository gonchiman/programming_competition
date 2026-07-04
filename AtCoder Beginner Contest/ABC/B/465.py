x, y, l, r, a, b = map(int, input().split())

res = 0
for i in range(a, b):
    if i < l or i >= r:
        res += y
    else:
        res += x
    # print(i)
    # print(res)
    # print()

print(res)