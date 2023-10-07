import tkinter as tk
from tkinter import messagebox
import collections

class PetApp:
    def __init__(self, master):
        self.master = master
        self.master.geometry("555x520")
        self.master.title("Pet App")
        self.pets = collections.OrderedDict()

        # Вид и Кличка
        self.subj_entry = tk.Entry(self.master)
        self.subj_entry.place(x=115, y=10, width=320, height=30)
        tk.Label(self.master, text="[ Вид ]:").place(x=10, y=15)

        self.pet_name_entry = tk.Entry(self.master)
        self.pet_name_entry.place(x=115, y=45, width=320, height=30)
        tk.Label(self.master, text="[ Кличка ]:").place(x=10, y=50)

        # Возраст
        self.age_entry = tk.Entry(self.master)
        self.age_entry.place(x=115, y=80, width=320, height=30)
        tk.Label(self.master, text="[ Возраст ]:").place(x=10, y=85)

        # Владелец
        self.owner_entry = tk.Entry(self.master)
        self.owner_entry.place(x=115, y=115, width=320, height=30)
        tk.Label(self.master, text="[ Владелец ]:").place(x=10, y=120)

        # Выбор ID
        self.pet_ID_entry = tk.Entry(self.master)
        self.pet_ID_entry.place(x=115, y=150, width=320, height=30)
        tk.Label(self.master, text="[ Выбор ID ]:").place(x=10, y=155)

        # Кнопки
        tk.Button(self.master, text="Добавить", command=self.create).place(x=445, y=10, width=100, height=30)
        tk.Button(self.master, text="Cписок", command=self.show_list).place(x=445, y=45, width=100, height=30)
        tk.Button(self.master, text="Получить", command=self.read).place(x=445, y=80, width=100, height=30)
        tk.Button(self.master, text="Обновить", command=self.update).place(x=445, y=115, width=100, height=30)
        tk.Button(self.master, text="Удалить", command=self.delete).place(x=445, y=150, width=100, height=30)

        # Cписок питомцев и его скроллбар
        self.text_area = tk.Text(self.master)
        self.text_area.place(x=10, y=190, width=520, height=320)
        self.scroll = tk.Scrollbar(self.master)
        self.scroll.place(x=530, y=190, height=320)

        # Привязка скроллбара к текстовому полю
        self.scroll.config(command=self.text_area.yview)
        self.text_area.config(yscrollcommand=self.scroll.set)

    def show_list(self):
        self.text_area.delete(1.0, tk.END)
        for ID, pet_info in self.pets.items():
            self.text_area.insert(tk.END, f'{ID}. {pet_info["Вид питомца"]} по кличке {pet_info["pet_name"]}. Возраст: {pet_info["Возраст питомца"]}. Владелец: {pet_info["Имя владельца"]}\n')

    def create(self):
        show_list(self)
        # обработка возраста
        try:
            age = int(self.age_entry.get())
        except ValueError:
            messagebox.showerror("Ошибка", "Пожалуйста, введите челочисленное значение для возраста.")
            return
        # создание записи о питомце
        ID = max(self.pets.keys(), default=0) + 1
        self.pets[ID] = {
            "pet_name": self.pet_name_entry.get(),
            "Вид питомца": self.subj_entry.get(),
            "Возраст питомца": age,
            "Имя владельца": self.owner_entry.get()
        }

    def delete(self):  
        ID = self.pet_ID_entry.get()
        if ID in self.pets:
            del self.pets[ID]
            messagebox.showerror(f"<!> {ID} удален <!>")
        else:
            messagebox.showerror("Ошибка!", "Питомец с таким ID не найден")

    def read(self):
        ID = self.pet_ID_entry.get()
        if ID in self.pets:
            self.text_area.delete(1.0, tk.END)
            pet_info = self.pets[ID]
            self.text_area.insert(tk.END, f'{ID}. {pet_info["Вид питомца"]} по кличке {pet_info["pet_name"]}. Возраст: {pet_info["Возраст питомца"]}. Владелец: {pet_info["Имя владельца"]}\n')
        else:
            messagebox.showerror("Ошибка!", "Питомец с таким ID не найден")

    def update(self):
        ID = self.pet_ID_entry.get()
        if ID in self.pets:
            del self.pets[ID]
            self.pets[ID] = {
                "pet_name": self.pet_name_entry.get(),
                "Вид питомца": self.subj_entry.get(),
                "Возраст питомца": self.age_entry.get(),
                "Имя владельца": self.owner_entry.get()
            }
        else:
            messagebox.showerror("Ошибка!", "Питомец с таким ID не найден")

# ---[ start ]---
root = tk.Tk()
app = PetApp(root)
root.mainloop()
