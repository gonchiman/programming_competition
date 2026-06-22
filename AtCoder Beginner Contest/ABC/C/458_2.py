S = input()


cent_ind = (len(S) - 1) / 2
max_cnt = round(cent_ind + 1)
count = 0
for i, s in enumerate(S):
    if s == "C":
        count += max_cnt - abs(round(cent_ind - i))

print(count)