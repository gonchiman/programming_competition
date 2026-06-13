N = int(input())

fee_table = [[None for _ in range(N+2)] for _ in range(N+1)]
for i in range(N-1):
    row = list(map(int, input().split()))
    for j, fee in enumerate(row):
        i += 1
        j += i+1
        fee_table[i][j] = fee

print(fee_table)


# print(C)
# print(fee_table)