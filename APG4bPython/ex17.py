N, M = map(int, input().split())
AB = [list(map(int, input().split())) for i in range(M)]

# ここにコードを追記する

result = [["-" for _ in range(N)] for _ in range(N)]

for ab in AB:
    result[ab[0]-1][ab[1]-1] = "o"
    result[ab[1]-1][ab[0]-1] = "x"

for row in result:
    print(" ".join(row))