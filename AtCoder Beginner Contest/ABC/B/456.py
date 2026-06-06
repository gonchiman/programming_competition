A = [input().split() for _ in range(3)]


cases = [
    [4, 5, 6],
    [4, 6, 5],
    [5, 4, 6],
    [5, 6, 4],
    [6, 4, 5],
    [6, 5, 4]
]


def get_comb(a: list, x: int):
    count = 0
    for i in range(6):
        if int(a[i]) == x:
            count += 1
    return count


count = 0

for case in cases:
    count += get_comb(A[0], case[0]) * get_comb(A[1], case[1]) * get_comb(A[2], case[2])

result = count / 216

print(result)