src = int(input("Введите число: "))

if (src == o):
    print("Нулевое число")
elif (src >= 0) and (src % 2 == 0):
    print("Положительное четное число")
elif (src <= 0) and (src % 2 == 0):
    print("Отрицательное четное число")
elif (src >= 0) and (src % 2 != 0):
    print("Положительное нечетное число")
else:
    print("Отрицательное нечетное число")
