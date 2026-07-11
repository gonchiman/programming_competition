n = int(input())
x = list(map(int, input().split()))

res = False
for xx in x:
    if xx >= 0:
        res = True
        break

if res:
    print("No")
else:
    print("Yes")