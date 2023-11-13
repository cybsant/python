import random

n = 50
arr = list()
for i in range(n):
    number = random.randint(1, 100)
    arr.append(number)

print("Notsorted:")
print(arr)
print("------")

#############################
### Bubble sort algorithm

# Вот что пишет лектор
for i in range(n):
    for j in range(n-1):
        left = arr[j]
        right = arr[j+1]
        if left > right:
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp
# Вот что пишу я
for i in range(n):
    for j in range(n-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

# Плохочитаемо?
# Так не принято в питоне?
# Может я не понимаю пока, чем это черевато?
# Почему лектор использует более громоздкий вариант?

print("Sorted:")
print(arr)
