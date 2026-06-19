import numpy as np


N, Q = map(int, input().split())
queries = [list(map(int, input().split())) for _ in range(Q)]


cols = np.zeros(N, dtype=np.int64)

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
            cols -= 1
            # ブロックがあるマスを数える
            sum = np.sum(cols > 0)
    else:
        count = 0
        count = int(np.count_nonzero(cols >= query[1]))
        print(count)