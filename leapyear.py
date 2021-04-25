while True:

    num=int(input("Enter a number: "))
    if num%4 != 0:
        print(num, "is not a leap year.")
    else:
        if num%100 == 0:
            if num%400 == 0:
                print(num, "is a leap year.")
            else:
                print(num, "is not a leap year.")
        else:
            print(num, "is a leap year.")

    new=int(input("Would you like to check another number? (0: No / 1: Yes): "))

    if new == 0:
        print("Goodbye")
        break
