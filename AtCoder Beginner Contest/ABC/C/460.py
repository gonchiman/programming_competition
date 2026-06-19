N, M = map(int, input().split())
A = list(map(int, input().split()))  # シャリの重さ
B = list(map(int, input().split()))  # ネタの重さ

A.sort()
B.sort()

count = 0
j = 0  # 次に見るネタの位置

for a in A:
    if j == M:
        break

    if B[j] <= 2 * a:
        count += 1
        j += 1

print(count)