N = int(input())
A = map(int, input().split())

counts = dict() # {num, count}
most_frequent_num = int()
most_frequent_count = 0

for a in A:
    if a not in counts:
        counts[a] = 1
    else:
        counts[a] += 1
    
    if counts[a] > most_frequent_count:
        most_frequent_num = a
        most_frequent_count = counts[a]

print(f"{most_frequent_num} {most_frequent_count}")