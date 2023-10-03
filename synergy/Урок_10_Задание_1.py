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
if age == 1:
    pets[name]["Возраст"] = str(pets[name]["Возраст"]) + " год"
elif 2 <= age <= 4:
    pets[name]["Возраст"] = str(pets[name]["Возраст"]) + " года"
else:
    pets[name]["Возраст"] = str(pets[name]["Возраст"]) + " лет"

""" А почему нельзя так? """
# print (f'Это {pets[name]["Вид"]} по кличке "{name}". Возраст: {pets[name]["Возраст"]}. Владелец: {pets[name]["Владелец"]}')
""" Этот вариант пришел в голову моментально """

""" Не придумал как тут применить keys(), но вот c использованием items() и values() """
pet_name, pet_info = list(pets.items())[0]
pet_subj, pet_age, pet_owner = pet_info.values()
print(f'Это {pet_subj} по кличке "{pet_name}". Возраст: {pet_age}. Владелец: {pet_owner}')
