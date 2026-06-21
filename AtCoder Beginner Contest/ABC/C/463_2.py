import sys
from bisect import bisect_right

input = sys.stdin.readline

N = int(input())

H = []
L = []

for _ in range(N):
    h, l = map(int, input().split())
    H.append(h)
    L.append(l)

# suffix_max[i] = i番目以降の身長の最大値
suffix_max = [0] * (N + 1)

for i in range(N - 1, -1, -1):
    suffix_max[i] = max(H[i], suffix_max[i + 1])

Q = int(input())
T = list(map(int, input().split()))

for t in T:
    # L_i <= t の人は退室済み
    # L_i > t となる最初の位置を探す
    idx = bisect_right(L, t)
    print(suffix_max[idx])