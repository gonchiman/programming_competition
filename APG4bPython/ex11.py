S = input()
# ここにプログラムを追記

result = 1

for c in S:
    match c:
        case "+":
            result += 1
        case "-":
            result -= 1
        case _:
            continue

print(result)