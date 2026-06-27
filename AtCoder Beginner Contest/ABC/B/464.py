H, W = map(int, input().split())
C = [input() for _ in range(H)]


k1 = 0
k2 = 0
k3 = 0
k4 = 0

for i in range(H):
    all_white = True
    for j in range(W):
        if C[i][j] == "#":
            all_white = False
            break
    if all_white:
        k1 += 1
    else:
        break

for i in range(H-1, -1, -1):
    all_white = True
    for j in range(W):
        if C[i][j] == "#":
            all_white = False
            break
    if all_white:
        k2 += 1
    else:
        break

for j in range(W):
    all_white = True
    for i in range(H):
        if C[i][j] == "#":
            all_white = False
            break
    if all_white:
        k3 += 1
    else:
        break

for j in range(W-1, -1, -1):
    all_white = True
    for i in range(H):
        if C[i][j] == "#":
            all_white = False
            break
    if all_white:
        k4 += 1
    else:
        break

for i in range(k1, H - k2):
    print(C[i][k3:W - k4])