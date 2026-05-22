data = [int(c) for c in input().split()]
# dataの中で隣り合う等しい要素が存在するなら"YES"を出力し、そうでなければ"NO"を出力する
# ここにプログラムを追記

pre_value = None
flag = False

for value in data:
    if value == pre_value:
        print("YES")
        flag = True
        break
    pre_value = value

if not flag:
    print("NO")