class Tortuga:
    def __init__(self, x, y, s):
        self.x = x
        self.y = y
        self.s = s

    def go_up(self): # увеличивает y на s
        self.y += self.s

    def go_down(self): # уменьшает y на s
        self.y -= self.s

    def go_left(self): # уменьшает x на s
        self.x -= self.s

    def go_right(self): # увеличивает x на s
        self.x += self.s

    def evolve(self): # увеличивает s на 1
            self.s += 1

    def degrade(self): # уменьшает s на 1 или выкидывает ошибку, когда s может стать ≤ 0
        if self.s <= 1:
            return False
        else:
            self.s -= 1

    def count_moves(self, x2, y2): # количество действий, чтоб добраться до x2 y2 от текущей позиции
        dist_x = abs(x2 - self.x) 
        dist_y = abs(y2 - self.y)

        steps_x = dist_x // self.s
        """ Если целое колво шагов не покрывает расстояния добавляем еще шаг """
        if dist_x % self.s != 0:
            steps_x += 1
        steps_y = dist_y // self.s
        """ Если целое колво шагов не покрывает расстояния добавляем еще шаг """
        if dist_y % self.s != 0:
            steps_y += 1        

        return steps_x + steps_y