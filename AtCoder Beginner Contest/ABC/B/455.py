H, W = map(int, input().split())
S = [input().split() for _ in range(H)]


def is_symmetry(s: list[list]) -> bool:
    pass


# i, j は検査マスの大きさ
for i in range(H):
    for j in range(W):
        # k, l は検査回数
        K = H - i
        for k in range(K):
            L = W - j
            for l in range(L):
                block = [S[m][l:l+j]for m in range(k, k+i+1)]
                print(block)