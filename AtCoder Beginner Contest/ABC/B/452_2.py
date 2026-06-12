N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]
M = int(input())
S = [input() for _ in range(M)]

candidate_sets = []

for i in range(N):
    b = AB[i][1] - 1
    chars = {s2[b] for s2 in S if len(s2) > b}
    candidate_sets.append(chars)

for s in S:
    if len(s) != N:
        print("No")
        continue

    is_satisfied = True

    for i, c in enumerate(s):
        if c not in candidate_sets[i]:
            is_satisfied = False
            break

    print("Yes" if is_satisfied else "No")