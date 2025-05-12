import unittest
from rpn_calculator import RPNCalculator, InvalidCommandError


class TestRPNCalculator(unittest.TestCase):
    def setUp(self):
        """
        Create an instance of the calculator before each test.
        """
        self.calculator = RPNCalculator()xw

    def test_addition(self):
        """
        Test the addition operation.
        """
        self.calculator.execute("3")
        self.calculator.execute("4")
        self.calculator.execute("+")
        self.assertEqual(self.calculator.stack[-1], 7.0)

    def test_subtraction(self):
        """
        Test the subtraction operation.
        """
        self.calculator.execute("10")
        self.calculator.execute("4")
        self.calculator.execute("-")
        self.assertEqual(self.calculator.stack[-1], 6.0)

    def test_multiplication(self):
        """
        Test the multiplication operation.
        """
        self.calculator.execute("2")
        self.calculator.execute("5")
        self.calculator.execute("*")
        self.assertEqual(self.calculator.stack[-1], 10.0)

    def test_division(self):
        """
        Test the division operation.
        """
        self.calculator.execute("10")
        self.calculator.execute("2")
        self.calculator.execute("/")
        self.assertEqual(self.calculator.stack[-1], 5.0)

    def test_division_by_zero(self):
        """
        Test that dividing by zero leaves the stack unchanged.
        """
        self.calculator.execute("10")
        self.calculator.execute("0")
        self.calculator.execute("/")
        self.assertEqual(len(self.calculator.stack), 2)
        self.assertEqual(self.calculator.stack[-2], 10.0)
        self.assertEqual(self.calculator.stack[-1], 0.0)

    def test_invalid_operator(self):
        """
        Test the case of an invalid operator.
        Should raise InvalidCommandError, and stack should remain unchanged.
        """
        self.calculator.execute("5")
        self.calculator.execute("3")
        with self.assertRaises(InvalidCommandError):
            self.calculator.execute("^")  # Invalid operator

        self.assertEqual(self.calculator.stack, [5.0, 3.0])

    def test_invalid_number(self):
        """
        Test invalid number input.
        Should raise InvalidCommandError, and stack should remain unchanged.
        """
        self.calculator.execute("5")
        with self.assertRaises(InvalidCommandError):
            self.calculator.execute("abc")  # Invalid number
        self.assertEqual(self.calculator.stack, [5.0])

    def test_multiple_operations(self):
        """
        Test a series of operations.
        """
        self.calculator.execute("5")
        self.calculator.execute("9")
        self.calculator.execute("1")
        self.calculator.execute("-")
        self.calculator.execute("/")
        self.assertEqual(self.calculator.stack[-1], 0.625)

    def test_empty_stack(self):
        """
        Test case when the stack is empty.
        Should print "Stack is empty."
        """
        self.calculator.get_result()

    def test_stack_command(self):
        """
        Test the 'stack' command to ensure it returns the correct stack state.
        """
        self.calculator.execute("3")
        self.calculator.execute("4")
        self.assertEqual(self.calculator.get_stack(), [3.0, 4.0])

    def test_insufficient_operands(self):
        """
        Test if trying to perform an operation with insufficient operands raises an error.
        """
        self.calculator.execute("5")
        with self.assertRaises(InvalidCommandError):
            self.calculator.execute("+")


if __name__ == "__main__":
    unittest.main()
