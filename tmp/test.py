import collections
from time import sleep

def err(msg):
    print('------------------------------------')
    print(f"<!> {msg} <!>")
    print('------------------------------------')
    sleep(1)
def create():
    print('--[ Добавить ]----------------------')
    ID = max(pets.keys(), default=0) + 1  
    # Ввод данных
    subj = input("Вид: ")
    pet_name = input("Кличка: ")
    # Обработка ошибок при вводе возраста
    while True:
        try:
            age = int(input("Возраст: "))
            break
        except ValueError:
            err("Пожалуйста, введите число") 
    owner = input("Владелец: ")
    pets[ID] = {
        "pet_name": pet_name,
        "Вид питомца": subj,
        "Возраст питомца": age,
        "Имя владельца": owner
    }
    print('------------------------------------')

def update():
    ID = int(input("Введите ID питомца: "))
         #'------------------------------------'
    print('--[ Изменить ]----------------------')
    if ID in pets:
        subj = input("Вид: ")
        pet_name = input("Кличка: ")
        # Обработка ошибок при вводе возраста
        while True:
            try:
                age = int(input("Возраст: "))
                break
            except ValueError:
                err("Пожалуйста, введите число.")
        owner = input("Владелец: ")
        # Данные питомца обновлены
        pets[ID] = {
            "pet_name": pet_name,
            "Вид питомца": subj,
            "Возраст питомца": age,
            "Имя владельца": owner
        }
    else:
        err("Питомец с таким ID не найден")
    print('------------------------------------')

def read():
    ID = int(input("Введите ID питомца: "))
    print('------------------------------------------------------------------------')
    if ID in pets:
        pet_info = pets[ID]
        print(f'Это {pet_info["Вид питомца"]} по кличке {pet_info["pet_name"]}. Возраст: {pet_info["Возраст питомца"]}. Владелец: {pet_info["Имя владельца"]}')
        print('------------------------------------------------------------------------')
    else:
        err("Питомец с таким ID не найден")

def delete():  
    print('--[ Удалить ]-----------------------')
    ID = int(input("Введите ID питомца: "))
    if ID in pets:
        del pets[ID]
        print(f"<!> {ID} удален <!>")
        print('------------------------------------')
    else:
        err("Питомец с таким ID не найден")

def pets_list():
    print('------------------------------------------------------------------------')
    for ID, pet_info in pets.items():
        print(f'{ID}: {pet_info["Вид питомца"]} по кличке {pet_info["pet_name"]}. Возраст: {pet_info["Возраст питомца"]}. Владелец: {pet_info["Имя владельца"]}')
    print('------------------------------------------------------------------------')

### Start
print('------------------------------------')
pets = collections.OrderedDict()
while True:
    print('[1] Добавить пациента')
    print('[2] Редактировать пациента')
    print('[3] Показать пациента по номеру')
    print('[4] Удалить пациента по номеру')
    print('[5] Показать список пациентов')
    print('[6] Выйти')
    print('------------------------------------')
    action = input("Выбирите действие по номеру: ")
    if action == "1":
        create()
    elif action == "2":
        update()
    elif action == "3":
        read()
    elif action == "4":
        delete()
    elif action == "5":
        pets_list()
    elif action == "6":
        break
    else:
        err("Некорректный выбор")
