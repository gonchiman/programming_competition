H, W = map(int, input().split())
S = [input() for _ in range(H)]


def check_symmetry(block: list) -> bool:
    for i in range(len(block)):
        for j in range(len(block[0])):
            if block[i][j] == block[-i-1][-j-1]:
                continue
            else:
                return False
    return True


count = 0

# i, j は検査マスの大きさ
for i in range(H):
    for j in range(W):
        # k, l は検査回数
        K = H - i
        for k in range(K):
            L = W - j
            for l in range(L):
                block = [S[m][l:l+j+1] if l != l+j else S[m][l] for m in range(k, k+i+1)]
                if check_symmetry(block):
                    count += 1
                # print(f"i, j, k, l = {i}, {j}, {k}, {l}")
                # print(block)
                # print()

print(count)