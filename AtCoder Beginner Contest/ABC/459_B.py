N = int(input())
S = input().split()


result = str()

for word in S:
    char = word[0]

    if char in ["a", "b", "c"]:
        result += "2"
    elif char in ["d", "e", "f"]:
        result += "3"
    elif char in ["g", "h", "i"]:
        result += "4"
    elif char in ["j", "k", "l"]:
        result += "5"
    elif char in ["m", "n", "o"]:
        result += "6"
    elif char in ["p", "q", "r", "s"]:
        result += "7"
    elif char in ["t", "u", "v"]:
        result += "8"
    elif char in ["w", "x", "y", "z"]:
        result += "9"

print(result)