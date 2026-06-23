N, K = map(int, input().split())

A = []
for _ in range(N):
    L_A = input().split()
    A.append("".join(L_A[1:]))

C = list(map(int, input().split()))
res = ""
for i, c in enumerate(C):
    res += A[i] * c


print(res[K-1])