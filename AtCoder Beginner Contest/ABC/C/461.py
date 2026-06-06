N, K, M = map(int, input().split())
C_V = [list(map(int, input().split())) for _ in range(N)]


max_values = {}

# init max_values
for i in range(N):
    if C_V[i][0] not in max_values.keys():
        max_values[C_V[i][0]] = 0

for i in range(N):
    if C_V[i][1] > max_values[C_V[i][0]]:
        max_values[C_V[i][0]] = C_V[i][1]


values = []

for c in max_values.keys():
    values = sorted(values)
    if len(values) < 3:
        values.append(max_values[c])
    else:
        if max_values[c] > min(values):
            values[0] = max_values[c]


print(max_values)
print(values)
print(sum(values))