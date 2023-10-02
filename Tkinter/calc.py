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

# Для составления чисел при нажатии кнопок
activeStr = ''
# Стэк для хранения операций и операндов
stack = []

# Арифметика
def calculate():
    global stack
    global label
    operand1 = Decimal(stack.pop())
    operand2 = Decimal(stack.pop())
    operation = stack.pop()
    result = 0

    if operation == '+':
        result = operand1 + operand2
    if operation == '-':
        result = operand1 - operand2
    if operation == '/':
        result = operand1 / operand2
    if operation == '*':
        result = operand1 * operand2
    # Обновляем текст на дисплее 
    label.configure(text=str(result))

# Функция для обработки нажатия кнопок
def click(text):
    global activeStr
    global stack
    # Если "CE" очищаем activeStr и стэк, выводим '0' на дисплее 
    if text == 'CE':
        stack.clear()
        activeStr = ''
        label.configure(text='0')
    # Нажимаем на цифровую кнопку
    elif '0' <= text <= '9':
        activeStr += text
        label.configure(text=activeStr)
    # Нажимаем точку
    elif text == '.':
        # Не ставим вторую точку
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

# Задаем стиль интерфейса
ttk.Style().theme_use("clam")

# Создаем объект стиля для настройки виджетов
label_style = ttk.Style()
# Создаем стиль для дисплея
label_style.configure("My.TLabel",
                    font="helvetica 14",
                    foreground="#004D40",
                    padding=4,
                    background="#B2DFDB")

# Создаем фрейм для дисплея и кнопки "CE"
frame = ttk.Frame(root)
frame.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=2, pady=2)

# Создаем дисплей
label = ttk.Label(frame, text='0', width=18, style="My.TLabel")
label.grid(row=0, column=0, sticky="w", padx=3, pady=2)

# Создаем кнопку "CE"
button = ttk.Button(frame, text='CE', command=lambda text='CE': click(text), width=6)
button.grid(row=0, column=1, sticky="e")

# Создаем кнопки калькулятора
for row in range(4):
    for col in range(4):
        button_text = buttons[row][col]
        button = ttk.Button(root, text=button_text, command=lambda text=button_text: click(text), width=2)
        button.grid(row=row + 1, column=col, sticky="nsew", padx=2, pady=2)

root.mainloop()
