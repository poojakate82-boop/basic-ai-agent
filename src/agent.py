def calculator():
    print("\n--- Calculator ---")

    try:
        a = float(input("Enter first number: "))
        op = input("Enter operator (+, -, *, /): ")
        b = float(input("Enter second number: "))

        if op == "+":
            print("Result:", a + b)

        elif op == "-":
            print("Result:", a - b)

        elif op == "*":
            print("Result:", a * b)

        elif op == "/":
            if b != 0:
                print("Result:", a / b)
            else:
                print("Cannot divide by zero.")

        else:
            print("Invalid operator.")

    except ValueError:
        print("Please enter valid numbers.")


def text_search():
    print("\n--- Text Search ---")

    text = input("Enter a sentence: ")
    word = input("Enter the word to search: ")

    if word.lower() in text.lower():
        print("Word found.")
    else:
        print("Word not found.")


def main():

    while True:

        print("\n===== BASIC AI AGENT =====")
        print("1. Calculator")
        print("2. Text Search")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            calculator()

        elif choice == "2":
            text_search()

        elif choice == "3":
            print("Thank you for using the Basic AI Agent.")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()