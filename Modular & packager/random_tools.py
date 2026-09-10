import random
import string


def random_number():
    try:
        minimum = int(input("Enter minimum number: "))
        maximum = int(input("Enter maximum number: "))

        if minimum > maximum:
            print("Minimum cannot be greater than maximum.")
            return

        value = random.randint(minimum, maximum)
        print("Random Number:", value)

    except ValueError:
        print("Invalid input!")


def random_list():
    try:
        count = int(input("Enter list size: "))
        minimum = int(input("Enter minimum number: "))
        maximum = int(input("Enter maximum number: "))

        if count < 0 or minimum > maximum:
            print("Invalid range or size.")
            return

        values = []
        for i in range(count):
            values.append(random.randint(minimum, maximum))

        print("Random List:", values)

    except ValueError:
        print("Invalid input!")


def random_password():
    try:
        length = int(input("Enter password length: "))

        if length <= 0:
            print("Length must be positive.")
            return

        characters = string.ascii_letters + string.digits + string.punctuation
        password = ""

        for i in range(length):
            password += random.choice(characters)

        print("Generated Password:", result)

    except ValueError:
        print("Invalid input!")


def random_otp():
    digits = string.digits
    otp = "".join(random.choices(digits, k=6))
    print("Generated OTP:", otp)


def random_menu():
    while True:
        print("\nRandom Data Generation:")
        print("1. Generate Random Number")
        print("2. Generate Random List")
        print("3. Create Random Password")
        print("4. Generate Random OTP")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice== "1":
            random_number()
        elif choice == "2":
            random_list()
        elif choice == "3":
            random_password()
        elif choice == "4":
            random_otp()
        elif choice == "5":
            break
        else:
            print("Invalid choice!")
