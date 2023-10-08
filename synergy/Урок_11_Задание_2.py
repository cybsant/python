from time import sleep
#from os import system, name

def create():
    print('---[ Добавить ]---------------------')
    ID = max(pets.keys(), default=0) + 1  
    add_pet(ID)

def update():
    ID = int(input("Введите ID питомца: "))
    print('---[ Изменить ]---------------------')
    if ID in pets:
        add_pet(ID)
    else:
        err("Питомец с таким ID не найден")

def delete():  
    print('---[ Удалить ]----------------------')
    ID = int(input("Введите ID питомца: "))
    if ID in pets:
        del pets[ID]
        print(f"<!> Пациент {ID} удален <!>")
    else:
        err("Питомец с таким ID не найден")

def read():
    ID = int(input("Введите ID питомца: "))
    print('---[ Пациент ]----------------------------------------------------------')
    if ID in pets:
        pet_info = pets[ID]
        print(f' Это {pet_info["Вид"]} по кличке {pet_info["Кличка"]}. Возраст: {pet_info["Возраст"]}. Владелец: {pet_info["Владелец"]}')
    else:
        err("Питомец с таким ID не найден")

def pets_list():
    print('---[ Список ]-----------------------------------------------------------')
    for ID, pet_info in pets.items():
        print(f' {ID}: {pet_info["Вид"]} по кличке {pet_info["Кличка"]}. Возраст: {pet_info["Возраст"]}. Владелец: {pet_info["Владелец"]}')

def add_pet(ID):
    subj = input("Вид: ")
    pet_name = input("Кличка: ")
    # Обработка ошибок при вводе возраста
    while True:
        try:
            age = int(input("Возраст: "))
            break
        except ValueError:
            err("Пожалуйста, введите число") 
    # Добавление приставки к возрасту
    age = f'{age} лет' if age > 4 else f'{age} год' if age == 1 else f'{age} года'
    owner = input("Владелец: ")
    pets[ID] = {
        "Кличка": pet_name,
        "Вид": subj,
        "Возраст": age,
        "Владелец": owner
    }

#def clear():
#    system('cls' if name == 'nt' else 'clear')

def err(msg):
    print('------------------------------------')
    print(f"<!> {msg} <!>")
    sleep(1) #; clear()

""" START """
pets = {}
while True:
    print('------------------------------------')
    print('[1] Добавить пациента')
    print('[2] Показать пациента')
    print('[3] Редактировать пациента')
    print('[4] Удалить пациента')
    print('[5] Показать список пациентов')
    print('[6] Выйти')
    print('------------------------------------')
    action = input("Выбирите действие по номеру: ")
    if action == "1":
        create()
    elif action == "2":
        read()
    elif action == "3":
        update()
    elif action == "4":
        delete()
    elif action == "5":
        pets_list()
    elif action == "6":
        break
    else:
        err("Некорректный выбор")
