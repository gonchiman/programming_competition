import sys
input = sys.stdin.readline


class Fenwick:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, i, x):
        while i <= self.n:
            self.bit[i] += x
            i += i & -i

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s


N, Q = map(int, input().split())

raw = [0] * N

# offset = 今までに全体から削除された回数
offset = 0

# cnt[h] = raw の値が h であるマスの個数
cnt = [0] * (Q + 1)
cnt[0] = N

# 実際の高さが 0 のマスの個数
# 実際の高さ = raw[i] - offset なので、
# 高さ0のマスは raw[i] == offset
zero_count = N

# raw の値ごとの個数を Fenwick Tree で管理する
# raw = h を index h+1 に入れる
fw = Fenwick(Q + 1)
fw.add(1, N)

ans = []

for _ in range(Q):
    t, a = map(int, input().split())

    if t == 1:
        i = a - 1

        old = raw[i]
        new = old + 1
        raw[i] = new

        cnt[old] -= 1
        cnt[new] += 1

        fw.add(old + 1, -1)
        fw.add(new + 1, 1)

        # もともと高さ0だったマスにブロックを置いたなら、
        # 高さ0のマスが1つ減る
        if old == offset:
            zero_count -= 1

        # すべてのマスに1個以上あるなら、全体から1個削除
        if zero_count == 0:
            offset += 1
            zero_count = cnt[offset]

    else:
        y = a

        # raw[i] - offset >= y
        # つまり raw[i] >= y + offset
        threshold = y + offset

        # raw の最大値は高々 Q
        if threshold > Q:
            ans.append("0")
        else:
            # raw < threshold の個数
            less = fw.sum(threshold)

            # raw >= threshold の個数
            ans.append(str(N - less))

print("\n".join(ans))