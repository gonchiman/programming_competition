T, X = map(int, input().split())
A = list(map(int, input().split()))


saved = int()
for i in range(len(A)):
    if i == 0 or abs(A[i] - saved) >= X:
        saved = A[i]
        print(f"{i} {saved}")