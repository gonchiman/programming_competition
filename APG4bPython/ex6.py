def raise_error():
    print("error")


A, op, B = input().split()
A = int(A)
B = int(B)

if op == "+":
    print(A + B)
elif op == "-":
    print(A - B)
elif op == "*":
    print(A * B)
elif op == "/":
    if B == 0:
        raise_error()
    else:
        print(A // B)
elif op == "?" or op == "=" or op == "!":
    raise_error()