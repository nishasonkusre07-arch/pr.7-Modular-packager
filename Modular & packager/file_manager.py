def make_file():
    name = input("Enter file name: ")

    try:
        with open(name, "w") as file:
            file.write("")

        print("File created successfully!")

    except OSError as error:
        print("Error:", error)


def write_file():
    name = input("Enter file name: ")
    text = input("Enter data to write: ")

    try:
        with open(name, "w") as file:
            file.write(text)

        print("Data written successfully!")

    except OSError as error:
        print("Error:", error)


def read_file():
    name = input("Enter file name: ")

    try:
        with open(name, "r") as file:
            text = file.read()

        print("File Content:")
        print(text)

    except FileNotFoundError:
        print("File not found!")

    except OSError as error:
        print("Error:", error)


def add_to_file():
    name = input("Enter file name: ")
    text = input("Enter data to append: ")

    try:
        with open(name, "a") as file:
            file.write(text)

        print("Data appended successfully!")

    except OSError as error:
        print("Error:", error)


def menu():
    while True:
        print("\nFile Operations:")
        print("1. Create a new file")
        print("2. Write to a file")
        print("3. Read from a file")
        print("4. Append to a file")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice  == "1":
            make_file()
        elif choice  == "2":
            write_file()
        elif choice == "3":
            read_file()
        elif choice  == "4":
            add_to_file()
        elif choice  == "5":
            break
        else:
            print("Invalid choice!")
