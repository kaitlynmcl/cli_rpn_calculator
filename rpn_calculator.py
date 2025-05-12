class InvalidCommandError(Exception):
    """Custom exception for invalid calculator input."""

    pass


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
        self._require_operands(2)
        b = self.stack.pop()
        a = self.stack.pop()
        self.stack.append(a + b)

    def subtract(self):
        self._require_operands(2)
        b = self.stack.pop()
        a = self.stack.pop()
        self.stack.append(a - b)

    def multiply(self):
        self._require_operands(2)
        b = self.stack.pop()
        a = self.stack.pop()
        self.stack.append(a * b)

    def divide(self):
        self._require_operands(2)
        b = self.stack.pop()
        a = self.stack.pop()
        if b == 0:
            print(f"Error: Cannot divide {a} by {b}. Reverting stack.")
            self.stack.append(a)
            self.stack.append(b)
        else:
            self.stack.append(a / b)

    def _require_operands(self, count):
        if len(self.stack) < count:
            raise InvalidCommandError(
                f"Error: Not enough operands for operation (need {count}, have {len(self.stack)})."
            )

    def execute(self, command):
        if command in self.operators:
            self.operators[command]()
        else:
            try:
                self.stack.append(float(command))
            except ValueError:
                raise InvalidCommandError(f"Invalid input: '{command}'")

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
                try:
                    calculator.execute(command)
                except InvalidCommandError as e:
                    print(e)

            for command in commands:
                calculator.execute(command)

            calculator.get_result()

        except (EOFError, KeyboardInterrupt):
            # Gracefully handle EOF (Ctrl+D) and KeyboardInterrupt (Ctrl+C)
            print("\nExiting calculator.")
            break


if __name__ == "__main__":
    main()
