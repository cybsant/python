class Human(object):
    name = "Ivan"
    height = 175
    age = 25

    def __init__(self, n, h, a):
        self.name = n
        self.height = h
        self.age = a

    def privet(self):
        print(f'Hello, my name is {self.name} and I am {self.age} years old!')
    
    def get_older(self):
        self.age += 5

    def goodbye(self):
        print('Goodbye')

# Создаем обьекты класса
h1 = Human('Anton', 120, 12)
h1 = Human('Dima', 190, 23)
# Вызываем методы
h1.privet()
h1.get_older()
h1.privet()