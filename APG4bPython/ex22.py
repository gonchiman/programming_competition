N = int(input())
inputs = list()

for i in range(N):
    inputs.append(list(map(int, input().split())))

second_nums = [input[1] for input in inputs]
min = min(second_nums)
max = max(second_nums)

sorted = list()

for i in range(min, max + 1):
    for input in inputs:
        if input[1] == i:
            print(f"{input[0]} {input[1]}")