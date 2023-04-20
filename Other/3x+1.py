def main():
    num = input("Enter a positive number: ")
    print(' ')
    try:
        num = int(num)
        if num < 0:
            print("Number must be positive!\n")
            main()
        else:
            math(num)
    except ValueError:
        print("Please enter a natural number!\n")
        main()


def math(num):
    value = 0
    while num != 1:
        if num == 0:
            break
        elif num % 2 == 0:
            num /= 2
            value += 1
        else:
            num = num * 3 + 1
            value += 1
    print(f"The number of iterations is {value}\n")
    main()


main()
