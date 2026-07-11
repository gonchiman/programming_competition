n, m = map(int, input().split())

c_dict = {}
for i in range(m):
    i = i + 1
    c_dict[i] = -1

for _ in range(n):
    c, s = map(int, input().split())
    if s > c_dict[c]:
        c_dict[c] = s


res = " ".join(list(map(str, c_dict.values())))
print(res)