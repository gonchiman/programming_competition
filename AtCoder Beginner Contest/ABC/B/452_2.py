N = int(input())
AB = [tuple(map(int, input().split())) for _ in range(N)]
M = int(input())
S = [input() for _ in range(M)]

can = [[set() for _ in range(10)] for _ in range(11)]

for s in S:
    L = len(s)
    for pos, c in enumerate(s):
        can[L][pos].add(c)

for s in S:
    if len(s) != N:
        print("No")
        continue

    ok = True

    for i, c in enumerate(s):
        A, B = AB[i]
        pos = B - 1

        if c not in can[A][pos]:
            ok = False
            break

    print("Yes" if ok else "No")