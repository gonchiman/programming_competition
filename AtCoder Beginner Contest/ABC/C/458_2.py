S = input()


cent_ind = (len(S) - 1) / 2
most_left = 0
most_right = len(S) - 1
count = 0
for i, s in enumerate(S):
    if s == "C":
        if i == cent_ind:
            count += 1 + i
        elif i < cent_ind:
            count += 1 + i
        else:
            count += 1 + (most_right - i)

print(count)