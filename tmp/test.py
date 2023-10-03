subject = input("Вид: ")
name = input("Кличка: ")
age = int(input("Возраст: "))
owner = input("Владелец: ")

pets = {
    name : {
        "Вид" : subject,
        "Возраст" : age,
        "Владелец" : owner
    }
}

# if age == 1:
#     print(f"Возраст питомца: {age} год")
# elif 2 <= age <= 4:
#     print(f"Возраст питомца: {age} года")
# else:
#     print(f"Возраст питомца: {age} лет")

print(pets.values())
