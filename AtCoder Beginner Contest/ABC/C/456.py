s = input()


len_list = []
count = 0
last = str()
for i, c in enumerate(s):
    if c == last:
        len_list.append(count)
        count = 1
    else:
        count += 1
    last = c
len_list.append(count)

res = int(sum([(x * (x + 1)) / 2 for x in len_list]) % 998244353)


print(res)