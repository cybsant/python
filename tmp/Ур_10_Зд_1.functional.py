""" Добавляем пациента в базу """
def add_pet():
    """ Воод данных """
    subj, name, age, owner = input("Вид: "), input("Кличка: "), int(input("Возраст: ")), input("Владелец: ")
    """ Формирование словаря """    pets[name] = {
        "Вид" : subj,
        "Возраст" : age,
        "Владелец" : owner
    }
    """ приставка к возрасту """
    pets[name]["Возраст"] = f'{pets[name]["Возраст"]} лет' if age > 4 else f'{pets[name]["Возраст"]} год' if age == 1 else f'{pets[name]["Возраст"]} года'

""" Посмотреть список пациентов"""
def display_pets():
    for name, pet_info in pets.items():
        print(f'Это {pet_info["Вид"]} по кличке "{name}". Возраст: {pet_info["Возраст"]}. Владелец: {pet_info["Владелец"]}')

""" НАЧАЛО """
pets = {} 
while True:
    action = input("Выбирите номер действия [ 1: Добавить пациента, 2: Показать список, 3: Выйти ]: ")
    if action == "1":
        add_pet()
    elif action == "2":
        display_pets()
    elif action == "3":
        break
    else:
        print("Некорректный выбор!")