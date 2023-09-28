# Ввод первого списка чисел
list1 = set()
n1 = int(input("Длина списка 1: "))
print("Введите числа:")
for _ in range(n1):
    num = int(input())
    list1.add(num)

# Ввод второго списка чисел
list2 = set()
n2 = int(input("Длина списка 2: "))
print("Введите числа:")
for i in range(n2):
    num = int(input())
    list2.add(num)

# Находим общие элементы
common = list1.intersection(list2)

# Выводим количество общих элементов
print(f"Количество одинаковых чисел в списках: {len(common)}")