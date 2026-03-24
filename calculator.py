def get_number(prompt):
    """Read a floating-point number safely from user input."""
    while True:
        value = input(prompt).strip()
        try:
            return float(value)
        except ValueError:
            print("Invalid number. Please enter a valid numeric value.")


def show_menu():
    print("\n=== Python Calculator ===")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Modulo")
    print("7. Exit")


def calculator():
    while True:
        show_menu()
        choice = input("Choose an option (1-7): ").strip()

        if choice == "7":
            print("Thanks for using the calculator. Goodbye!")
            break

        if choice not in {"1", "2", "3", "4", "5", "6"}:
            print("Invalid choice. Please select a number from 1 to 7.")
            continue

        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")

        if choice == "1":
            result = num1 + num2
            operation = "+"
        elif choice == "2":
            result = num1 - num2
            operation = "-"
        elif choice == "3":
            result = num1 * num2
            operation = "*"
        elif choice == "4":
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
                continue
            result = num1 / num2
            operation = "/"
        elif choice == "5":
            result = num1 ** num2
            operation = "^"
        else:
            if num2 == 0:
                print("Error: Modulo by zero is not allowed.")
                continue
            result = num1 % num2
            operation = "%"

        print(f"Result: {num1} {operation} {num2} = {result}")


if __name__ == "__main__":
    calculator()
