def make_file(name):
    with open(name, "w") as file:
        file.write("File created successfully.\n")
    
    print("File created successfully.")


def show_file(name):
    try:
        with open(name, "r") as file:
            print("\nFile Content:")
            print(file.read())
    except FileNotFoundError:
        print("File not found!")


def save_content(name, text):
    with open(name, "w") as file:
        file.write(text)
    
    print("Content written successfully.")


def add_content(name, text):
    with open(name, "a") as file:
        file.write(text)
    
    print("Content appended successfully.")
