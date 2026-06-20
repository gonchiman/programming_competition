N, Q = map(int, input().split())


a = [int() for _ in range(N + 1)]
c = [int() for _ in range(Q + 1)]
mn = 0

for _ in range(Q):
    t, x = map(int, input().split())
    if t == 1:
        a[x] += 1
        c[a[x]] += 1
        if c[a[x]] == N:
            mn = a[x]
    if t == 2:
        if x + mn > Q:
            print(0)
        else:
            print(c[x + mn])