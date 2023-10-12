class Tortuga:
    def __init__(self, x, y, s):
        self.x = x
        self.y = y
        self.s = s

    def go_up(self, y, s): # увеличивает y на s
        self.y = y + s

    def go_down(self, y, s): # уменьшает y на s
        self.y = y - s

    def go_left(self, x, s): # уменьшает x на s
        self.y = y + s

    def go_right(self, x, s): # увеличивает x на s
        self.y = y + s

    def evolve(self, s): # увеличивает s на 1
            self.s += s

    def degrade(self): # уменьшает s на 1 или выкидывает ошибку, когда s может стать ≤ 0
        if self.s <= 0:
            return False
        else:
            self.s -= s

    def count_moves(x2, y2): # возвращает минимальное количество действий, за которое черепашка сможет добраться до x2 y2 от текущей позиции
        