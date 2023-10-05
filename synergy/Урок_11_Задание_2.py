import collections
from time import sleep

def clear():  
    from os import system, name
    system('cls' if name == 'nt' else 'clear')

def create(ID):
    # Последний пациент в списке
    last = collections.deque(pets, maxlen=1)[0]
    # Ввод данных
    subj, pet_name, age, owner = input("Вид: "), input("Кличка: "), int(input("Возраст: ")), input("Владелец: ")
    # Шаблон БД =)
    pets = {
        ID:
            {
                pet_name: {
                "Вид питомца": subj,
                "Возраст питомца": age,
                "Имя владельца": owner
                },
            },
    }

def read():
    for pet_name, pet_info in pets.items():
        print(f'Это {pet_info["Вид"]} по кличке "{pet_name}". Возраст: {pet_info["Возраст"]}. Владелец: {pet_info["Владелец"]}')

def update():
    return
def delete():
    return

def get_pet(ID):
    # функция, с помощью которой вы получите информацию о питомце в виде словаря
    return pets[ID] if ID in pets.keys() else False

def get_suffix(age,pet_name): 
    pets[pet_name]["Возраст"] = f'{pets[pet_name]["Возраст"]} лет' if age > 4 else f'{pets[pet_name]["Возраст"]} год' if age == 1 else f'{pets[pet_name]["Возраст"]} года'
    return age

def pets_list():
    # Эта функция будет создана для удобства отображения всего списка питомцев
    # Информацию по каждому питомцу можно вывести с помощью цикла for
    return

### НАЧАЛО ###
pets = {} 
while True:
    print('[1] Добавить пациента')
    print('[2] Редактировать пациента')
    print('[3] Показать пациента по номеру')
    print('[4] Показать список пациентов')
    print('[5] Выйти')
    action = input("Выбирите действие по номеру: ")
    if action == "1":
        create()
    elif action == "2":
        update()
    elif action == "3":
        read()
    elif action == "4":
        pets_list()
    elif action == "5":
        break
    else:
        clear(); print("!!! Некорректный выбор !!!"); sleep(1); clear()