n, q = map(int, input().split())
a = list(map(int, input().split()))

# (値, インデックス) を値の小さい順に並べる
sorted_a = sorted((value, index) for index, value in enumerate(a))

for _ in range(q):
    k = int(input())
    removed = {index - 1 for index in map(int, input().split())}

    for value, index in sorted_a:
        if index not in removed:
            print(value)
            break