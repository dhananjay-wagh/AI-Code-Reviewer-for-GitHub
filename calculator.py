def add(a,b):
    x = a+b
    return x

def divide(a,b):
    return a/b

def calculate(operation,a,b):
    if operation == "add":
        return add(a,b)
    elif operation == "divide":
        return divide(a,b)

result = calculate("divide",10,0)
print(result)
