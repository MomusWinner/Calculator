from backend.interface import Calculator

def run(backend: Calculator):
    while True:
        a = float(input("Input a: "))
        b = float(input("Input b: "))
        operation = input("Operation ('minus' or 'plus'): ")
        if operation == 'plus':
            print(backend.sum(a, b))
        elif operation == "minus":
            print(backend.minus(a, b))
        else:
            print("Invalid operation")