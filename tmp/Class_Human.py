class Human(object):
    # Статические атрибуты
    name = "Ivan"
    height = 175
    age = 25

    def __init__(self, n, h, a):
        # Динамические атрибуты
        self.name = n
        self.height = h
        self.age = a

    # Методы класса
    def privet(self):
        print(f'Hello, my name is {self.name} and I am {self.age} years old!')

    def get_older(self):
        self.age += 5

    def goodbye(self):
        print('Goodbye')

# Обьекты класса
h1 = Human('Anton', 120, 12)
h1 = Human('Dima', 190, 23)

# Вызов методов
h1.privet()
h1.get_older()
h1.privet()