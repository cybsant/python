src = int(input("Введите число: "))
if (src == 0):
    print("Нулевое число")
elif (src >= 0) and (src % 2 == 0):
    print("Положительное четное число")
elif (src <= 0) and (src % 2 == 0):
    print("Отрицательное четное число")
else:
    print("Число не является четным")
