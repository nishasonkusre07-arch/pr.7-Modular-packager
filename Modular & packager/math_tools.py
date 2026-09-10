import math


def find_factorial():
    try:
        number = int(input("Enter a number: "))

        if number < 0:
            print("Factorial is not defined for negative numbers.")
            return

        result = math.factorial(number)
        print("Factorial:", result)

    except ValueError:
        print("Invalid input!")


def calculate_compound_interest():
    try:
        principal = float(input("Enter principal amount: "))
        rate = float(input("Enter rate of interest (in %): "))
        years = float(input("Enter time (in years): "))

        final_amount = principal * ((1 + rate / 100) ** years)
        interest = final_amount - principal

        print("Compound Interest:", round(interest, 2))
        print("Total Amount:", round(final_amount, 2))

    except ValueError:
        print("Invalid input!")


def calculate_trigonometry():
    try:
        degree = float(input("Enter angle in degrees: "))
        angle = math.radians(degree)

        sine = math.sin(angle)
        cosine = math.cos(angle)
        tangent = math.tan(angle)

        print("Sin:", round(sine, 4))
        print("Cos:", round(cosine, 4))
        print("Tan:", round(tangent, 4))

    except ValueError:
        print("Invalid input!")


def calculate_shape_area():
    print("\nArea of Geometric Shapes:")
    print("1. Circle")
    print("2. Rectangle")
    print("3. Triangle")

    choice = input("Enter your choice: ")

    try:
        if choice  == "1":
            r = float(input("Enter radius: "))
            area = math.pi * (r ** 2)
            print("Area of Circle:", round(area, 2))

        elif choice == "2":
            l = float(input("Enter length: "))
            w = float(input("Enter width: "))
            print("Area of Rectangle:", l * w)

        elif choice  == "3":
            b = float(input("Enter base: "))
            h = float(input("Enter height: "))
            print("Area of Triangle:", (b * h) / 2)

        else:
            print("Invalid choice!")

    except ValueError:
        print("Invalid input!")


def math_menu():
    while True:
        print("\nMathematical Operations:")
        print("1. Calculate Factorial")
        print("2. Solve Compound Interest")
        print("3. Trigonometric Calculations")
        print("4. Area of Geometric Shapes")
        print("5. Back to Main Menu")

        option = input("Enter your choice: ")

        if option == "1":
            find_factorial()
        elif option == "2":
            calculate_compound_interest()
        elif option == "3":
            calculate_trigonometry()
        elif option == "4":
            calculate_shape_area()
        elif option == "5":
            break
        else:
            print("Invalid choice!")
