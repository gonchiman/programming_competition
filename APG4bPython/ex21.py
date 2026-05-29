A, B = map(int, input().split())

def to_binary(x: int) -> str:
    binary = str()

    while x > 0:
        if x % 2 == 0:
            binary = "0" + binary
        else:
            binary = "1" + binary

        x = int(x / 2)

    return to_8_digits(binary)

def to_8_digits(x: str) -> str:
    return "0" * (8 - len(x)) + x

binary_a = to_binary(A)
binary_b = to_binary(B)
binary_c = str()
C = int()

for i in range(8):
    if binary_a[i] == binary_b[i]:
        binary_c += "0"
    else:
        binary_c += "1"

for i in range(8):
    if binary_c[i] != "0":
        C += 2 ** (7 - i)

print(C)