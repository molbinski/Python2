#tester@tester-m:~/spotkanie2/unitest$ cat calculator.py


def calculate(a, b, operacja):
    if operacja == "+":
        return a + b
    elif operacja == "-":
        return a - b
    elif operacja == "*":
        return a * b
    elif operacja == "/":
        return a / b

def str_calculator(a, b, operacja):
    if operacja == 'concat':
        return a + b
    if operacja == "in":
        return a in b
