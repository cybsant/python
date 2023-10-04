def create():
    """ Воод данных """
    subj, name, age, owner = input("Вид: "), input("Кличка: "), int(input("Возраст: ")), input("Владелец: ")
    """ Формирование словаря """
    pets[name] = {
        "Вид" : subj,
        "Возраст" : age,
        "Владелец" : owner
    }
    """ приставка к возрасту """
    pets[name]["Возраст"] = f'{pets[name]["Возраст"]} лет' if age > 4 else f'{pets[name]["Возраст"]} год' if age == 1 else f'{pets[name]["Возраст"]} года'

def read():
    return pets
def update():
    return pets
def delete():
    return pets

""" НАЧАЛО """
pets = {} 
