def main():
    while True:
        num = input("Enter a number: ")
        while not num.isnumeric():
            num = input("Enter a number: ")
        op = input("Enter an operation or type clear to finish: ")
        while op not in ('+', '-', '*', '/', '^', '%', 'clear'):
            op = input("Enter an operation or type clear to finish: ")
            if op == 'clear':
                exit()
            else:
                continue
        num2 = input("Enter a number: ")
        while not num.isnumeric():
            num2 = input("Enter a number: ")
        num, num2 = int(num), int(num2)
        calculate(num, op, num2)


def calculate(num, op, num2):
    if op.strip() == '+':
        ans = num + num2
        print(f"{num} plus {num2} equals {ans}")
    elif op.strip() == '-':
        ans = num - num2
        print(f"{num} minus {num2} equals {ans}")
    elif op.strip() == '*':
        ans = num * num2
        print(f"{num} times {num2} equals {ans}")
    elif op.strip() == '/':
        ans = num / num2
        print(f"{num} divided by {num2} equals {ans}")
    elif op.strip() == '^':
        ans = num ** num2
        print(f"{num} to the power of {num2} equals {ans}")
    elif op.strip() == '%':
        ans = num % num2
        print(f"{num} mod {num2} equals {ans}")


main()
