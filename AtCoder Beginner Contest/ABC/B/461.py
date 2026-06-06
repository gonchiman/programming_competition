N = int(input())
A = input().split()
B = input().split()


is_yes = True

for i in range(N):
    if i+1 == int(B[int(A[i])-1]):
        continue
    else:
        is_yes = False

if is_yes:
    print("Yes")
else:
    print("No")