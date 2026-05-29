N = int(input())
inputs = list()

for i in range(N):
    inputs.append(list(map(int, input().split())))

def quick_sort(x: list[list]) -> list[list]:
    if len(x) <= 1:
        return x

    pivot_index = int((len(x)) / 2)
    pivot = x[pivot_index][1]

    left = list()
    center = list()
    right = list()

    for row in x:
        if row[1] < pivot:
            left.append(row)
        elif row[1] > pivot:
            right.append(row)
        else:
            center.append(row)

    return quick_sort(left) + center + quick_sort(right)

sorted = quick_sort(inputs)

for row in sorted:
    print(f"{row[0]} {row[1]}")