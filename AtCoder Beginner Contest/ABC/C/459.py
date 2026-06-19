N, Q = map(int, input().split())
queries = [list(map(int, input().split())) for _ in range(Q)]


cols = []
for _ in range(N):
    cols.append(0)

sum = 0
for query in queries:
    if query[0] == 1:
        # 指定したマスにブロックを置く
        i = query[1] - 1
        cols[i] += 1
        # 初めてブロックがマスに置かれたらカウントする
        if cols[i] == 1:
            sum += 1
        # すべてのマスが埋まったら、1行削除する
        if sum == N:
            for i in range(N):
                cols[i] -= 1
                sum = 0
            for col in cols:
                if col > 0:
                    sum += 1
    else:
        count = 0
        for col in cols:
            if col >= query[1]:
                count += 1
        print(count)