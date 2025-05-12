# CLI RPN Calculator

## Description

The CLI RPN (Reverse Polish Notation) Calculator is a command-line tool that allows users to perform arithmetic calculations using RPN. This calculator evaluates mathematical expressions by reading numbers and operators in a post-fix notation format. The operations supported are addition (`+`), subtraction (`-`), multiplication (`*`), and division (`/`). The calculator's state is maintained on a stack, with operands pushed onto the stack and results returned to the top of the stack.

The tool is designed for simplicity and functionality, providing a user-friendly CLI for quick calculations. It includes additional commands like `stack` (to view the current stack) and `help` (to show usage instructions), making it easy for users to understand and interact with the calculator.

## Features

- **Basic Arithmetic Operations**: Supports addition, subtraction, multiplication, and division.
- **Error Handling**: Handles errors like division by zero and insufficient operands.
- **Stack-based Calculation**: Operands and results are managed in a stack, making it easy to perform consecutive operations.
- **Help Command**: Displays instructions on how to use the calculator.
- **Stack Command**: Displays the current state of the stack.
- **Graceful Exit**: Supports `Ctrl+C` and `Ctrl+D` to exit gracefully.

## Architecture and Design Decisions

### Core Logic

- **Class-Based Architecture**: The design is centered around a class-based structure. The `RPNCalculator` class encapsulates all the core functionality, such as stack management, executing operations, and handling errors. This modular approach makes the calculator easy to maintain, extend, and test, allowing for clear separation of concerns. Each operation (addition, subtraction, etc.) is encapsulated as a method within the class, improving readability and reusability.

- **RPN Calculation**: The RPNCalculator class performs arithmetic operations using a stack. Each number or operator is processed in sequence, and the results are pushed back onto the stack. The operations are executed using methods like `add`, `subtract`, `multiply`, and `divide`.
  
- **Command Handling**: Commands are processed one by one. If the command is a number, it's converted and pushed onto the stack. If it's an operator, the appropriate method is invoked (e.g., `add()` for `+`). The calculator also gracefully handles invalid commands by raising custom errors (`InvalidCommandError`).

- **Error Handling**: The system checks for common errors such as insufficient operands for an operation (e.g., trying to add two numbers with only one operand on the stack), invalid operators, or invalid number input.

### Technical Choices

1. **Python Standard Libraries**: 
    - **unittest** for testing: This provides a structured way to verify the behavior of the calculator and its edge cases.

2. **Command-line Interface (CLI)**: 
    - **Interactive Mode**: The program continuously asks for user input and processes each command until the user decides to quit (with the `q` command).
    - **Input Parsing**: User input is split into tokens (e.g., numbers and operators) and processed one by one, providing flexibility for multiple commands per line.

3. **Error Handling**: Custom exceptions (like `InvalidCommandError`) are used to clearly communicate errors like invalid inputs or insufficient operands. This makes the code more maintainable, and allows error messages to supply more information. 

### Trade-offs and Decisions

- **Command Validation**: The current approach assumes that the user enters a well-formed sequence of commands, and it gracefully handles invalid commands by printing errors. However, if the user enters invalid input multiple times, the program will print multiple error messages but will continue running. In a production system, one might choose to add a retry mechanism or allow users to reset the calculator state.
  
- **No Persistent State**: The calculator does not store results between sessions. Once the user exits, the stack is cleared. Adding persistent storage (like saving the current state to a file or database) would be a useful feature if the project were extended further.

- **Testing**: The testing strategy uses unit tests to verify individual components (like arithmetic operations, invalid commands, and stack operations). In future cases, mocking user input and output with `unittest.mock` could make it possible to test interactive features (e.g., `help` command) without requiring a real user to interact with the CLI.

### What Could Be Improved

- **Advanced Features**: If additional time were available, I might implement features such as:
  - **Support for parentheses**: Handling more complex expressions with nested operations.
  - **Error Recovery**: Instead of simply printing errors and continuing, we could add a mechanism to allow the user to correct their mistake.
  - **Persistent Session**: Allow users to save and load the stack, so they can continue their calculations across sessions.

- **Testing of Interactive Commands**: A more comprehensive testing suite could be implemented to simulate longer user interactions.

### Future Enhancements

- **Alternate Interfaces**: We could consider implementing additional interfaces such as WebSocket, file-based input/output, or TCP socket communication. These interfaces would allow for integration with other systems or tools, providing more flexibility in how users interact with the calculator.
  - **WebSocket**: Implementing a WebSocket interface would allow the calculator to interact with web-based clients in real time, enabling remote access to the calculator from browsers or other web applications.
  - **File-Based Input/Output**: A file-based interface could allow users to provide input through files (e.g., `.txt` or `.csv`) and retrieve output in a file format. This would make it easier to automate calculations and integrate the calculator into workflows where input and output are stored in files.
  - **TCP Socket Communication**: Supporting TCP socket communication would allow the calculator to be used in networked environments where commands are sent over a network. This could be useful for integrating the calculator into server-side applications, IoT devices, or other distributed systems.

- **Extended Command Set**: Future versions of the calculator could include a wider range of commands to further extend its capabilities.
  - **Additional Operators**: In addition to the four basic arithmetic operations, the calculator could include advanced operators such as exponentiation (`^`), modulus (`%`), and trigonometric functions (`sin`, `cos`, `tan`, etc.).
  - **User-Defined Operations**: The ability to define custom operations on the fly would provide a great deal of flexibility for users. For example, a user might want to define a custom operation like `sqrt` for square root calculation or a `pow` operation for exponentiation.
  - **Conditional Operations**: Adding support for conditional operations, like `if` or `switch`, could allow the calculator to handle more complex logic directly in the command line interface. This would help with tasks that involve conditional calculations based on certain thresholds or criteria.

- **Improved Error Handling and User Interaction**: While the current error handling is functional, a more advanced user interaction system could improve the user experience.
  - **Clearer Error Messages**: Improve error messaging by providing more context, such as where in the input the error occurred or suggestions for correcting the input.
  - **Undo/Redo Functionality**: Implementing an undo/redo feature would allow users to revert to previous states of the stack, providing more control over their calculations. This could be useful if a user accidentally performs an operation they didn't intend.

- **User Interface Enhancements**: A more sophisticated user interface could be implemented to enhance the command-line experience. Features could include:
  - **Auto-completion**: Enable auto-completion for commands, operators, and variables to reduce typing errors and make the interface more user-friendly.
  - **Colored Output**: Use colors to differentiate between errors, results, and instructions, improving the visual clarity of the output.

By addressing these potential improvements, we could further enhance the functionality, usability, and versatility of the CLI RPN Calculator, making it suitable for a wider range of use cases and more adaptable to future needs.

## Installation

### Prerequisites

- **Python** (Python 3.x recommended) must be installed on your system. You can download it from the official Python website: [https://www.python.org/downloads/](https://www.python.org/downloads/).

- **Git** must be installed to clone the repository. If you don't have Git, you can install it from [https://git-scm.com/](https://git-scm.com/).

### To Run the Code

1. **Clone the Repository**:

   First, clone the repository to your local machine. Open your terminal and run the following command:

   ```bash
   git clone git@github.com:kaitlynmcl/cli_rpn_calculator.git


2. **Run the Program**:

   Based on your version of Python, you can run run the program using the following command:

   <pre> ```bash python3 rpn_calculator.py ``` </pre>


3. **Run Tests**:

   If you'd like to run tests locally, you can run them using the following command:


   <pre> ```bash python3 test_rpn_calculator.py ``` </pre>

