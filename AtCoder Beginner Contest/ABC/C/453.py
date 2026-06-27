N = int(input())
L = list(map(int, input().split()))


x = 0.5
pre_x = 0.5
count = 0

for l in L:
    if x > 0:
        x = x - l
    elif x < 0:
        x = x + l
    if x * pre_x < 0:
        count += 1
    pre_x = x

print(count) 