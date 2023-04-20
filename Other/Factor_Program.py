def main():
    num = input("Enter a number between 1 and 1 million: ")
    print(' ')
    try:
        num = int(num)
        if num not in range(1, 1000001):
            print("Number must be between 1 and 1 million.\n")
            main()
        else:
            factor(num)
    except ValueError:
        print("Please enter a number!\n")
        main()


def factor(num):
    List = []
    for i in range(1, 1000001):
        if num % i == 0:
            List.append(i)
    if len(List) <= 2:
        print(
            f"The number {num} is prime!\n")
        main()
    Last = List[-1]
    List = List[:-1]
    final = ', '.join(str(e) for e in List)
    print(
        f"The common factors of the number {num} include {final} and {Last}.\n")
    main()


main()
