N, K, M = map(int, input().split())

class Jewelry:
    def __init__(self, c, v, i):
        self.category = c
        self.value = v
        self.index = i

C_V = list()

for j in range(N):
    c, v = map(int, input().split())
    C_V.append(Jewelry(c, v, j))

# {category: [index, value]}
max_values = {}

for j, jew in enumerate(C_V):
    jew: Jewelry
    if jew.category not in max_values.keys():
        max_values[jew.category] = [j, jew.value]
    elif jew.value > max_values[jew.category][1]:
        max_values[jew.category] = [j, jew.value]

selected_jews = []

for key in max_values:
    index = max_values[key][0]
    jew = C_V[index]
    if len(selected_jews) < M:
        selected_jews.append(jew)
    else:
        values = [jew.value for jew in selected_jews]
        if jew.value > min(values):
            for j, selected_jew in enumerate(selected_jews):
                if selected_jew.value == min(values):
                    selected_jews[j] = jew

selected_jews_2 = []
selected_jews_index = [x.index for x in selected_jews]

if (K - M) > 0:
    for i, jew in enumerate(C_V): 
        if i in selected_jews_index:
            continue
        else:
            if len(selected_jews_2) < (K - M):
                selected_jews_2.append(jew)
            else:
                values = [jew.value for jew in selected_jews_2]
                if jew.value > min(values):
                    for j, selected_jew in enumerate(selected_jews_2):
                        if selected_jew.value == min(values):
                            selected_jews_2[j] = jew


sum_1 = sum([x.value for x in selected_jews])
sum_2 = sum([x.value for x in selected_jews_2])

print(sum_1+sum_2)