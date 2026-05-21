n = int(input())
a = int(input())
inputs = list()


class Operands:
    ADD = "+"
    SUB = "-"
    MUL = "*"
    DIV = "/"


class Calculator:
    @classmethod
    def calculate(cls, operand: str, a: int, b: int) -> int:
        match operand:
            case Operands.ADD:
                return cls.add(a, b)
            case Operands.SUB:
                return cls.sub(a, b)
            case Operands.MUL:
                return cls.mul(a, b)
            case Operands.DIV:
                return cls.div(a, b)
                
    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def sub(a, b):
        return a - b
    
    @staticmethod
    def mul(a, b):
        return a * b
    
    @staticmethod
    def div(a, b):            
        return int(a / b)
    

for _ in range(n):
    operand, value = input().split()
    inputs.append([operand, int(value)])

for i, input in enumerate(inputs):
    if input[0] == Operands.DIV and input[1] == 0:
        print("error")
        break
    a = Calculator.calculate(input[0], a, input[1])
    print(f"{i+1} {a}")
