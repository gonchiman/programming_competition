N, K = map(int, input().split())

<<<<<<< HEAD
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
=======
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
>>>>>>> 17bf5b694fb95cd6fa7b73e4c557fc250049d260
