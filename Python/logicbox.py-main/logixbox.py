while True:
    print()
    print("Welcome to the Pattern Generator and Number Analyzer!")
    print("Select an option:")
    print("1. Right-angled Triangle")
    print("2. Pyramid Pattern")
    print("3. Left-angled Triangle")
    print("4. Analyze a Range of Numbers")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1" or choice == "2" or choice == "3":

        rows = int(input("Enter the number of rows for the pattern: "))

        if rows <= 0:
            print("Invalid number of rows. Program stopped.")
            break

        print()
        print("Pattern:")
        print()

        if choice == "1":
            for i in range(1, rows + 1):
                for j in range(i):
                    print("*", end="")
                print()

        elif choice == "2":
            for i in range(1, rows + 1):
                for space in range(rows - i):
                    print(" ", end="")
                for star in range(2 * i - 1):
                    print("*", end="")
                print()

        elif choice == "3":
            for i in range(1, rows + 1):
                for space in range(rows - i):
                    print(" ", end="")
                for star in range(i):
                    print("*", end="")
                print()

    elif choice == "4":

        start = int(input("Enter the start of the range: "))
        end = int(input("Enter the end of the range: "))

        if end <= start:
            print("End number must be greater than start number.")
            continue

        total = 0

        for num in range(start, end + 1):

            if num < 0:
                pass
            elif num % 2 == 0:
                print("Number", num, "is Even")
            else:
                print("Number", num, "is Odd")

            total = total + num

        print("Sum of all numbers from", start, "to", end, "is:", total)

    elif choice == "5":
        print("Thank you for using the program. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
