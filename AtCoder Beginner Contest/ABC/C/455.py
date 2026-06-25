import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))

a_dict = {}
for a in A:
    a_dict[a] = 0

for a in A:
    a_dict[a] += 1

min_x = 0
diff_list = []
for key in a_dict:
    diff = key * a_dict[key]
    diff_list.append(diff)

diff_list.sort(reverse=True)
res = 0
for i, diff in enumerate(diff_list):
    if i < K:
        continue
    else:
        res += diff


print(res)