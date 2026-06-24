import sys
input = sys.stdin.readline

n, k = map(int, input().split())
k -= 1
a = []
for i in range(n):
    aa = list(map(int, input().split()))[1:]
    a.append(aa)
c = list(map(int, input().split()))
for i in range(n):
    if k < c[i] * len(a[i]):
        print(a[i][k % len(a[i])])
        break
    k -= c[i] * len(a[i])
