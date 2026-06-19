N, M = map(int, input().split())
A = list(map(int, input().split())) # シャリの重さ
B = list(map(int, input().split())) # ネタの重さ


# B <= 2A

count = 0
sorted_a = sorted(A)
sorted_b = sorted(B)

for a in sorted_a:
    if sorted_b[0] <= 2 * a and len(sorted_b) != 0:
        count += 1
        del sorted_b[0]


print(count)