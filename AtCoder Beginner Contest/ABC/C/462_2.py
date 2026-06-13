N = int(input())
XY = list()

p_of_min_x = []
p_of_min_y = []

for i in range(N):
    x, y = map(int, input().split())
    XY.append([x, y])

    if i == 0:
        p_of_min_x = [x, y]
        p_of_min_y = [x, y]
    else:
        min_x = p_of_min_x[0]
        if x < min_x:
            p_of_min_x = [x, y]

        min_y = p_of_min_y[1]
        if y < min_y:
            p_of_min_y = [x, y]

# print(p_of_min_x)
# print(p_of_min_y)

x1, y1 = p_of_min_x
x2, y2 = p_of_min_y

if not p_of_min_x == p_of_min_y:
    a = (y2-y1)/(x2-x1)
    b = y1 - (y2-y1)/(x2-x1)

# print(a)
# print(b)

min_x = p_of_min_x[0]
min_y = p_of_min_y[1]
result = 0
if p_of_min_x == p_of_min_y:
    result = 1
else:
    for xy in XY:
        x, y = xy
        if xy == p_of_min_x or xy == p_of_min_y:
            result += 1
        elif x <= min_x:
            result += 1
        elif y <= min_y:
            result += 1
        elif (-a)*x+y <= b:
            result += 1


print(result)