N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]
M = int(input())
S = [input() for _ in range(M)]


is_satisfied = list()
for s in S:
    is_satisfied = True
    if len(s) == N:
        for i, c in enumerate(s):
            if c in [s2[AB[i][1]-1] if len(s2) >= AB[i][1] else None for s2 in S]:
                pass
            else:
                is_satisfied = False
                break
    else:
        is_satisfied = False

    print("Yes") if is_satisfied else print("No")