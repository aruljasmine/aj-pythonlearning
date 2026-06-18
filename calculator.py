def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Error"
    return a / b

print(add(5, 3))
print(sub(5, 3))
print(mul(4, 2))
print(div(10, 2))