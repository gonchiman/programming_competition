H, W = map(int, input().split())
S = [input().split() for _ in range(H)]


def is_symmetry(s: list[list]) -> bool:



for i in range(H):
    for j in range(W):
        for k in range(int(H/i)):
            for l in range(int())