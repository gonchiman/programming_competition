N = int(input())
# KA = [list(map(int, input().split())) for _ in range(N)]


# people: [sender]
gift_count = {}
for i in range(N):
    i += 1
    gift_count[i] = []

for i in range(N):
    i += 1
    row = list(map(int, input().split()))
    for j, value in enumerate(row):
        if j == 0:
            continue
        else:
            gift_count[value].append(str(i))

for key in gift_count:
    print(f"{len(gift_count[key])} {" ".join(gift_count[key])}")