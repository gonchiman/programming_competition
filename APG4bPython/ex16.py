N, K = map(int, input().split())
WORDS = input().split()


result = list()

for word in WORDS:
    if len(word) >= K:
        result.append(word)

print(" ".join(result))