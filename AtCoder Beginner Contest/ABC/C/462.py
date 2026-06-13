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

p_compare = list()
for xy in XY:
    x, y = xy
    if x >= p_of_min_x[0] and x <= p_of_min_y[0] and y >= p_of_min_y[1] and y <= p_of_min_x[1]:
        p_compare.append(xy)

# print(p_compare)

min_x = p_of_min_x[0]
min_y = p_of_min_y[1]
result = 0
if p_of_min_x == p_of_min_y:
    result = 1
else:
    for xy in XY:
        x, y = xy
        if x <= min_x:
            result += 1
        elif y <= min_y:
            result += 1
        elif x <= p_of_min_y[0] and y <= p_of_min_x[1]:
            for p in p_compare:
                x2, y2 = p
                if x <= x2 and y <= y2:
                    result += 1


print(result)