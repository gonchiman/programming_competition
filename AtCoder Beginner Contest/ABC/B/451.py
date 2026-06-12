N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)] 


# 部署番号：人数
current_count = dict()
next_year_count = dict()

for m in range(M):
    m += 1
    current_count[m] = 0
    next_year_count[m] = 0

for ab in AB:
    a, b = ab
    current_count[a] += 1
    next_year_count[b] += 1

for m in range(M):
    m += 1
    diff = next_year_count[m] - current_count[m]
    print(diff)