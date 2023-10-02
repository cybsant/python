# Ввод данных
M = int(input("Грузоподьемность лодки: "))
N = int(input("Количество рыбаков: "))
fishers = []
for i in range(N):
    fisher = int(input(f"Рыбак{i+1}: "))
    fishers.append(fisher)

fishers.sort()  # Сортируем список рыбаков по весу

# Указатели на самого легкого и самого тяжелого рыбаков
left, right = 0, len(fishers) - 1
# признаюсь про указатели left, right - нагуглил, а не взял из учебных материалов.

# Считаем лодки
boats = 0    

while left <= right:
    if (fishers[left] + fishers[right]) <= M: # Если влезают 2 рыбака
        left += 1
        right -= 1
    else: # Если нет, добавляем одного
        right -= 1
    boats += 1

print("Количество лодок:", boats)