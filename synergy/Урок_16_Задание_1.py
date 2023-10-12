class Kassa:
    def __init__(self, cass):
        self.cass = cass

    def top_up(self, x): # пополнить на X
        self.cass += x

    def count_1000(self): # сколько целых тысяч осталось в кассе
        print(f'В кассе {self.cass // 1000} тысяч')

    def take_away(self, x): # забрать X из кассы, либо вывести ошибку
        if self.cass >= x:
            self.cass -= x
        else:
            print("Недостаточно денег в кассе")
