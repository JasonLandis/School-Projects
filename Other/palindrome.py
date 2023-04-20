def main():
    value = input("Enter anything: ")
    print(' ')
    new = value[::-1]
    if new == value:
        print(f"{new} is a palindrome!\n")
        main()
    else:
        print(f"{value} is not a palindrome\n")
        main()


main()
