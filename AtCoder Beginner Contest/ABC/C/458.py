S = input()


length = len(S)
count = 0
for i in range(0, length, 2):
    roop_num = length - i
    for j in range(roop_num):
        # print(f"(i, j) =  ({i}, {j})")
        # print()
        if S[j + (i // 2)] == "C":
            count += 1
            # print(i)
            # print(j)
            # print()

print(count)

# print(length)