N, K, M = map(int, input().split())
GEMS = list()


reps = {}

for i in range(N):
    gem = tuple(map(int, input().split()))
    GEMS.append(gem)

    color, value = gem
    if color not in reps.keys():
        reps[color] = (value, i)
    else:
        rep_value = reps[color][0]
        if value > rep_value:
            reps[color] = (value, i)

ignore_index = list()
reps_temp = list(reps.values())

reps_temp.sort(key=lambda x: x[0], reverse=True)
for i in range(M):
	index = reps_temp[i][1]
	ignore_index.append(index)

selected = list()
if (K - M) > 0:
    for i, gem in enumerate(GEMS):
        if i in ignore_index:
            continue
        
        value = gem[1]
        selected.sort()
        if len(selected) < (K - M) :
            selected.append(value)
        else:
            if value > selected[0]:
                selected[0] = value
			
sum_value = sum(selected)
for i in ignore_index:
	value = GEMS[i][1]
	sum_value += value


print(sum_value)