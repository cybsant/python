from tkinter import *
from tkinter import ttk
from decimal import *

root = Tk()
root.title('Calculator')

buttons = (('1', '2', '3', '/', '4'),
           ('4', '5', '6', '*', '4'),
           ('7', '8', '9', '-', '4'),
           ('.', '0', '=', '+', '4')
           )

activeStr = ''
stack = []

def calculate():
    global stack
    global label
    result = 0
    operand2 = Decimal(stack.pop())
    operation = stack.pop()
    operand1 = Decimal(stack.pop())

    if operation == '+':
        result = operand1 + operand2
    if operation == '-':
        result = operand1 - operand2
    if operation == '/':
        result = operand1 / operand2
    if operation == '*':
        result = operand1 * operand2
    label.configure(text=str(result))

def click(text):
    global activeStr
    global stack
    if text == 'CE':
        stack.clear()
        activeStr = ''
        label.configure(text='0')
    elif '0' <= text <= '9':
        activeStr += text
        label.configure(text=activeStr)
    elif text == '.':
        if activeStr.find('.') == -1:
            activeStr += text
            label.configure(text=activeStr)
    else:
        if len(stack) >= 2:
            stack.append(label['text'])
            calculate()
            stack.clear()
            stack.append(label['text'])
            activeStr = ''
            if text != '=':
                stack.append(text)
        else:
            if text != '=':
                stack.append(label['text'])
                stack.append(text)
                activeStr = ''
                label.configure(text='0')

# Interface
#root.configure(bg="gray") # меняем цвет фона
ttk.Style().theme_use("clam")
label_style = ttk.Style()
label_style.configure("My.TLabel",
                    font="helvetica 14",
                    foreground="#004D40",
                    padding=4,
                    background="#B2DFDB",
                    border = True)

# фрейм для строки с дисплеем и кнопкой "CE"
frame = ttk.Frame(root)
frame.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=2, pady=2)

# дисплей на левую сторону фрейма
label = ttk.Label(frame, text='0', width=24, style="My.TLabel" )
label.grid(row=0, column=0, sticky="w", padx=2, pady=2)

# кнопку "CE" на правую сторону фрейма
button = ttk.Button(frame, text='CE', command=lambda text='CE': click(text), width=8)
button.grid(row=0, column=1, sticky="e", padx=2, pady=2)  # расстояние между кнопками

for row in range(4):
    for col in range(4):
        button_text = buttons[row][col]
        if button_text == '=':
            button = ttk.Button(root, text=button_text, command=lambda text=button_text: click(text), width=3)
        else:
            button = ttk.Button(root, text=button_text, command=lambda text=button_text: click(text), width=3)
        button.grid(row=row + 1, column=col, sticky="nsew", padx=2, pady=2)  # расстояние между кнопками

root.grid_rowconfigure(5, weight=1)
root.grid_columnconfigure(4, weight=1)

root.mainloop()