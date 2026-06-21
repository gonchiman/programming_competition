import sys
from bisect import bisect_right

input = sys.stdin.readline

N = int(input())

heights = []
leave_times = []

for _ in range(N):
    H, L = map(int, input().split())

    while heights and heights[-1] <= H:
        heights.pop()
        leave_times.pop()

    heights.append(H)
    leave_times.append(L)

Q = int(input())

queries = list(map(int, input().split()))

for T in queries:
    idx = bisect_right(leave_times, T)
    print(heights[idx])