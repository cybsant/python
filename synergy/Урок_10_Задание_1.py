""" Воод данных """
subj = input("Вид: ")
name = input("Кличка: ")
age = int(input("Возраст: "))
owner = input("Владелец: ")

""" Формирование словаря """
pets = {
    name : {
        "Вид" : subj,
        "Возраст" : age,
        "Владелец" : owner
    }
}

""" Добавляем к возрасту правильное слово """
pets[name]["Возраст"] = f'{pets[name]["Возраст"]} лет' if age > 4 else f'{pets[name]["Возраст"]} год' if age == 1 else f'{pets[name]["Возраст"]} года'

""" Не придумал как тут применить keys(), но вот c использованием items() и values() """
pet_name, pet_info = list(pets.items())[0]
pet_subj, pet_age, pet_owner = pet_info.values()
print(f'Это {pet_subj} по кличке "{pet_name}". Возраст: {pet_age}. Владелец: {pet_owner}')

""" А почему нельзя так? """
# print (f'Это {pets[name]["Вид"]} по кличке "{name}". Возраст: {pets[name]["Возраст"]}. Владелец: {pets[name]["Владелец"]}')
""" Этот ^^^ вариант пришел в голову моментально да и понятнее так. """
