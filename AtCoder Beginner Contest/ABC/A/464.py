S = input()


east_cnt = 0
west_cnt = 0

for s in S:
    if s == "E":
        east_cnt += 1
    else:
        west_cnt += 1

result = str()
if east_cnt > west_cnt:
    result = "East"
else:
    result = "West"

print(result)