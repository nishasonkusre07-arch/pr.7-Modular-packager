from datetime import datetime
import time


def show_datetime():
    current = datetime.now()
    print("Current Date and Time:",
          current.strftime("%Y-%m-%d %H:%M:%S"))


def date_difference():
    try:
        date1 = input("Enter the first date (YYYY-MM-DD): ")
        date2 = input("Enter the second date (YYYY-MM-DD): ")

        first_date = datetime.strptime(first_input, "%Y-%m-%d")
        second_date = datetime.strptime(second_input, "%Y-%m-%d")

        days = abs((second_date - first_date).days)

        print("Difference:", days, "days")

    except ValueError:
        print("Invalid date format!")


def change_date_format():
    try:
        user_date = input("Enter date (YYYY-MM-DD): ")
        converted_date = datetime.strptime(user_date, "%Y-%m-%d")

        print("Custom Format:",
              converted_date.strftime("%d-%m-%Y"))

    except ValueError:
        print("Invalid date format!")


def stopwatch():
    input("Press Enter to start stopwatch...")
    begin = time.time()

    input("Press Enter to stop stopwatch...")
    end = time.time()

    elapsed = round(end - begin, 2)
    print("Elapsed Time:", elapsed, "seconds")


def countdown():
    try:
        count = int(input("Enter countdown seconds: "))

        if count < 0:
            print("Enter a positive number.")
            return

        for seconds_left in range(count, 0, -1):
            print("Time Left:", seconds_left, "seconds")
            time.sleep(1)

        print("Time's up!")

    except ValueError:
        print("Invalid input!")


def time_menu():
    while True:
        print("\nDatetime and Time Operations:")
        print("1. Display current date and time")
        print("2. Calculate difference between two dates/times")
        print("3. Format date into custom format")
        print("4. Stopwatch")
        print("5. Countdown Timer")
        print("6. Back to Main Menu")

        option = input("Enter your choice: ")

        if option == "1":
            show_datetime()
        elif option == "2":
            date_difference()
        elif option == "3":
            change_date_format()
        elif option == "4":
            stopwatch()
        elif option == "5":
            countdown()
        elif option == "6":
            break
        else:
            print("Invalid choice!")            
