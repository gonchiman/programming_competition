import sys
input = sys.stdin.readline

N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]
M = int(input())
S = list(input() for _ in range(M))

slen_dict = {}
for i in range(10):
    slen_dict[i + 1] = [set() for _ in range(10+1)]
# print(slen_dict)

for s in S:
    s = s.strip()
    length = len(s)
    for i, c in enumerate(s):
        slen_dict[length][i + 1].add(c)
# print(slen_dict)

for s in S:
    s = s.strip()
    is_exist = True
    if len(s) != N:
        print("No")
        continue
    for i, c in enumerate(s):
        a, b = AB[i]
        if c in slen_dict[a][b]:
            continue
        else:
            is_exist = False
            break
    if is_exist:
        print("Yes")
    else:
        print("No")