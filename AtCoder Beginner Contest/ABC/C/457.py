N, K = map(int, input().split())

L = []
A = []
for _ in range(N):
    L_A = list(map(int, input().split()))
    L.append(L_A[0])
    A.append(L_A[1:])

C = list(map(int, input().split()))


b = []
for i, c in enumerate(C):
    b.append(A * c)


print(b)