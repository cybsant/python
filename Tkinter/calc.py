from tkinter import *
from tkinter import ttk
from decimal import Decimal

class Calculator:
    def __init__(self):
        self.active_str = ''
        self.stack = []

    def click_number(self, number):
        self.active_str += number
        return self.active_str

    def click_decimal_point(self):
        if self.active_str.find('.') == -1:
            self.active_str += '.'
        return self.active_str

    def clear(self):
        self.stack.clear()
        self.active_str = ''
        return '0'

    def calculate(self):
        try:
            self.stack.append(self.active_str)
            result = self._perform_calculation()
            self.stack.clear()
            self.active_str = str(result)
            return result
        except ZeroDivisionError:
            return 'Error: Division by zero'
        except:
            return 'Error: Calculation error'

    def _perform_calculation(self):
        result = Decimal(self.stack[0])

        for i in range(1, len(self.stack), 2):
            operation = self.stack[i]
            operand = Decimal(self.stack[i + 1])

            if operation == '+':
                result += operand
            elif operation == '-':
                result -= operand
            elif operation == '*':
                result *= operand
            elif operation == '/':
                if operand != 0:
                    result /= operand
                else:
                    raise ZeroDivisionError("Division by zero")
            else:
                raise ValueError("Invalid operation")

        return result


class CalculatorUI:
    def __init__(self, root, calculator):
        self.calculator = calculator
        self.root = root
        self.setup_ui()

    def setup_ui(self):
        self.root.title('Calculator')
        buttons = (('1', '2', '3', '/'),
                   ('4', '5', '6', '*'),
                   ('7', '8', '9', '-'),
                   ('.', '0', '=', '+')
                   )

        ttk.Style().theme_use("clam")
        label_style = ttk.Style()
        label_style.configure("My.TLabel",
                              font="helvetica 14",
                              foreground="#004D40",
                              padding=4,
                              background="#B2DFDB")

        frame = ttk.Frame(self.root)
        frame.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=2, pady=2)

        self.label = ttk.Label(frame, text='0', width=18, style="My.TLabel")
        self.label.grid(row=0, column=0, sticky="w", padx=3, pady=2)

        button = ttk.Button(frame, text='CE', command=self.click_ce, width=6)
        button.grid(row=0, column=1, sticky="e")

        for row in range(4):
            for col in range(4):
                button_text = buttons[row][col]
                button = ttk.Button(self.root,
                                    text=button_text,
                                    command=lambda text=button_text: self.click(text),
                                    width=2)
                button.grid(row=row + 1, column=col, sticky="nsew", padx=2, pady=2)

    def click(self, text):
        if text == '=':
            result = self.calculator.calculate()
            self.label.configure(text=str(result))
            return result
        elif '0' <= text <= '9':
            result = self.calculator.click_number(text)
            self.label.configure(text=result)
            return result
        elif text == '.':
            result = self.calculator.click_decimal_point()
            self.label.configure(text=result)
            return result

        self.calculator.stack.append(self.calculator.active_str)
        self.calculator.stack.append(text)
        self.calculator.active_str = ''
        return self.calculator.active_str

    def click_ce(self):
        result = self.calculator.clear()
        self.label.configure(text=result)


def main():
    root = Tk()
    calculator = Calculator()
    CalculatorUI(root, calculator)
    root.mainloop()


if __name__ == "__main__":
    main()