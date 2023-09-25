N = int(input("Количество чисел: ")) # Количество чисел
count = 0
for i in range(N):
    num = int(input("Введите число: ")) # Вводим число
    if num == 0: # Считаем нули
        count += 1
print("Количество нолей:", count) # Результат