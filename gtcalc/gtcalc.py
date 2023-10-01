import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Pango
from gi.repository import Gdk
from decimal import Decimal

class Calculator(Gtk.Window):
    def __init__(self):
        super(Calculator, self).__init__(title="Calculator")
        self.set_default_size(400, 400)
        self.connect("destroy", Gtk.main_quit)

        self.active_str = ''
        self.stack = []

        self.grid = Gtk.Grid()
        self.grid.set_column_spacing(3)  # горизонтальный 
        self.grid.set_row_spacing(3)     # вертикальный 
        self.add(self.grid)

        self.create_display()
        self.create_buttons()

    def create_display(self):
        display = Gtk.Entry()
        display.set_name("display")
        display.set_text("")
        display.set_hexpand(True)
        display.set_editable(False)
        display.set_alignment(1.0)
        display.set_halign(Gtk.Align.START)
        display.modify_font(Pango.FontDescription("monospace 20"))
        display.set_margin_top(3)  # Отступ сверху
        display.set_margin_bottom(3)  # Отступ снизу
        display.set_margin_left(3)  # Отступ слева
        display.set_margin_right(3)  # Отступ справа
        self.grid.attach(display, 0, 0, 4, 1)
        self.display = display

    def create_buttons(self):
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            'CE',  # Перенести кнопку "CE" вверх?
        ]

        button_row = 1
        button_col = 0

        for label in buttons:
            button = Gtk.Button(label)
            button.set_size_request(80, 40)
            button.connect("clicked", self.on_button_clicked, label)
            button.set_margin_left(3)   # Устанавливаем левый отступ
            button.set_margin_right(3)  # Устанавливаем правый отступ
            button.set_margin_top(3)    # Отступ сверху
            button.set_margin_bottom(3) # Отступ снизу
            self.grid.attach(button, button_col, button_row, 1, 1)
            button_col += 1
            if button_col > 3:
                button_col = 0
                button_row += 1

    def calculate(self):
        result = 0
        operand2 = Decimal(self.stack.pop())
        operation = self.stack.pop()
        operand1 = Decimal(self.stack.pop())

        if operation == '+':
            result = operand1 + operand2
        if operation == '-':
            result = operand1 - operand2
        if operation == '/':
            result = operand1 / operand2
        if operation == '*':
            result = operand1 * operand2

        self.display.set_text(str(result))

    def on_button_clicked(self, widget, data=None):
        if data == 'CE':
            self.stack.clear()
            self.active_str = ''
            self.display.set_text('0')
        elif '0' <= data <= '9':
            self.active_str += data
            self.display.set_text(self.active_str)
        elif data == '.':
            if self.active_str.find('.') == -1:
                self.active_str += data
                self.display.set_text(self.active_str)
        else:
            if len(self.stack) >= 2:
                self.stack.append(self.display.get_text())
                self.calculate()
                self.stack.clear()
                self.stack.append(self.display.get_text())
                self.active_str = ''
                if data != '=':
                    self.stack.append(data)
            else:
                if data != '=':
                    self.stack.append(self.display.get_text())
                    self.stack.append(data)
                    self.active_str = ''
                    self.display.set_text('0')

if __name__ == "__main__":
    win = Calculator()
    
    # Добавляем стиль для выделения дисплея
    css_provider = Gtk.CssProvider()
    css_provider.load_from_data(b"#display { background-color: #B2DFDB; }")
    screen = Gdk.Screen.get_default()
    context = Gtk.StyleContext()
    context.add_provider_for_screen(screen, css_provider, Gtk.STYLE_PROVIDER_PRIORITY_USER)
    
    win.show_all()
    Gtk.main()
