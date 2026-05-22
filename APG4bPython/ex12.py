N = int(input())  # 生徒の数Nを読み込む
T = list(map(int, input().split()))  # 各生徒のゴールまでの時間を読み込む
# ここにプログラムを追記

fastest_time = None
fastest_time_index = None

for i, t in enumerate(T):
    if i == 0:
        fastest_time = t
        fastest_time_index = i + 1
        continue
    
    if t < fastest_time:
        fastest_time = t
        fastest_time_index = i + 1

print(fastest_time_index)