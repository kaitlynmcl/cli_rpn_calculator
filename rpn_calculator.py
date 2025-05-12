class RPNCalculator:
    def __init__(self):
        self.stack = []
        self.operators = {
            "+": self.add,
            "-": self.subtract,
            "*": self.multiply,
            "/": self.divide,
        }

    def add(self):
        b = self.stack.pop()
        a = self.stack.pop()
        self.stack.append(a + b)

    def subtract(self):
        b = self.stack.pop()
        a = self.stack.pop()
        self.stack.append(a - b)

    def multiply(self):
        b = self.stack.pop()
        a = self.stack.pop()
        self.stack.append(a * b)

    def divide(self):
        b = self.stack.pop()
        a = self.stack.pop()
        if b == 0:
            print(f"Error: Cannot divide {a} by {b}. Reverting stack.")
            self.stack.append(a)  # put 'a' back on stack
            self.stack.append(b)  # put 'b' back on stack
        else:
            self.stack.append(a / b)

    def execute(self, command):
        try:
            if command in self.operators:
                self.operators[command]()
            else:
                self.stack.append(float(command))
        except ValueError:
            print(f"Error: Invalid command '{command}'")

    def get_result(self):
        if len(self.stack) == 0:
            print("Stack is empty.")
        else:
            print(f"Result: {self.stack[-1]}")


def main():
    calculator = RPNCalculator()
    print("Welcome to the CLI RPN Calculator!")
    print("Enter 'q' to quit or use any of the four basic operators (+, -, *, /).")

    while True:
        try:
            user_input = input("Enter command: ").strip()

            if user_input.lower() == "q":
                print("Exiting calculator.")
                break

            # Split the input into individual tokens and process each token
            commands = user_input.split()

            for command in commands:
                calculator.execute(command)

            calculator.get_result()

        except (EOFError, KeyboardInterrupt):
            # Gracefully handle EOF (Ctrl+D) and KeyboardInterrupt (Ctrl+C)
            print("\nExiting calculator.")
            break


if __name__ == "__main__":
    main()
