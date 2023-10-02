# Ввод последовательности чисел
numbers = input("Введите числа через пробел: ").split()

# Создаем множество для отслеживания уникальных чисел
unique = set()

# Проходим по числам в последовательности
for num in numbers:
    num = int(num)
    if num in unique:
        print("YES")
    else:
        print("NO")
        unique.add(num)