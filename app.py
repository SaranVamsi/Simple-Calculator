def display_calculator():
    print("\n" + "=" * 25)
    print(" " * 7 + "CLI Calculator")
    print("=" * 25)
    print("Enter calculations in the format:")
    print("    <number> <operator> <number>")
    print("Supported operators: +, -, *, /")
    print("Type 'exit' to quit.")
    print("=" * 25)


def perform_calculation(expression):
    try:
        # Split and validate the input
        parts = expression.split()
        if len(parts) != 3:
            return "Invalid input format. Use: <number> <operator> <number>."

        num1, operator, num2 = parts
        num1 = float(num1)
        num2 = float(num2)

        # Perform the appropriate operation
        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 == 0:
                return "Error: Division by zero is not allowed."
            result = num1 / num2
        else:
            return "Invalid operator. Please use +, -, *, or /."

        return f"Result: {result}"
    except ValueError:
        return "Invalid numbers. Please enter valid numeric values."


def main():
    while True:
        display_calculator()
        user_input = input("Enter calculation or 'exit': ").strip()

        if user_input.lower() == "exit":
            print("Exiting Calculator. Goodbye!")
            break

        result = perform_calculation(user_input)
        print("\n" + "-" * 25)
        print(result)
        print("-" * 25)
       
if __name__ == "__main__":
    main()
