# Ввод размера массива
N = int(input("Размер массива: "))
# Создание пустого массива
arr = []
# Наполнение массива
print("Наполним массив данными:")
for i in range(N):
    num = int(input())
    arr.append(num)
# Вывод
print("Дан массив")
print(arr)
print("Перевернем его 3мя разными способами")
# Переворачивание массива способ 1
print("Способ 1")
rra2 = arr[::-1]
print(rra2)
# Переворачивание массива способ 2 :)
print("Способ 2")
rra3 = list(reversed(arr))
print(rra3)
# Переворачивание массива способ 3 :))
print("Способ 3")
arr.reverse()
print(arr)