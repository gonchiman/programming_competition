import statistics


N = int(input())
# ここにプログラムを追記


inputs = list(map(int, input().split()))

average = int(statistics.mean(inputs))

for input in inputs:
    print(abs(input - average))