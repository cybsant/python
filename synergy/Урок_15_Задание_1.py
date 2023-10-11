class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

# Создаем объект класса Transport
autobus = Transport('Renault Logan', 180, 12)

# Вывод
print(f'Название автомобиля: {autobus.name}, Скорость: {autobus.max_speed}. Пробег: {autobus.mileage}.')
