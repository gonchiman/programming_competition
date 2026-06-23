N, K = map(int, input().split())

A = []
for _ in range(N):
    L_A = input().split()
    A.append("".join(L_A[1:]))

C = list(map(int, input().split()))

for i in range(N):
    length = len(A[i]) * C[i]

    if K > length:
        K -= length
    else:
        print(A[i][(K - 1) % len(A[i])])
        break