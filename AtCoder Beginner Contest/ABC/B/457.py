N = int(input())
L = list()
A = list()
for _ in range(N):
    row = input().split()
    L.append(row[0])
    A.append(row[1:])
X, Y = map(int, input().split())


print(A[X-1][Y-1])