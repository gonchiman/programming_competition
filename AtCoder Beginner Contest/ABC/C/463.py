N = int(input())
HL = [list(map(int, input().split())) for _ in range(N)]
Q = int(input())
T = list(map(int, input().split()))


last_l = HL[N - 1][1]
max_heights = {}

for i in range(last_l + 1):
    max_heights[i] = list()

for hl in HL:
    n, l = hl
    max_heights[l].append(n)

H = [hl[0] for hl in HL]
sorted_h = sorted(H, reverse=True)

max = sorted_h[0]
look_at = 0


print(max_heights)
print(sorted_h)