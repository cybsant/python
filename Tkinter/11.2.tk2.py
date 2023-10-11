import tkinter as tk
from tkinter import messagebox
import collections

def entry_with_label(master, label_text, row, column):
    tk.Label(master, text=label_text).grid(row=row, column=0, padx=5, sticky="e")
    entry = tk.Entry(master)
    entry.grid(row=row, column=column, ipady=3, sticky="ew")
    return entry

def button(master, text, command, row, column):
    return tk.Button(master, text=text, command=command).grid(row=row, column=column, sticky="ew")

class PetApp:
    def __init__(self, master):
        self.master = master
        self.master.title("VetPet")
        self.pets = collections.OrderedDict()

        # Создаем фреймы
        top_frame = tk.Frame(master)
        mod_frame = tk.Frame(master)
        bottom_frame = tk.Frame(master)
        top_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=False)
        mod_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=False)
        bottom_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        # Вид
        self.subj_entry = entry_with_label(top_frame, "[ Вид ]", 0, 1)
        # Кличка
        self.pet_name_entry = entry_with_label(top_frame, "[ Кличка ]", 1, 1)
        # Возраст
        self.age_entry = entry_with_label(top_frame, "[ Возраст ]", 2, 1)
        # Владелец
        self.owner_entry = entry_with_label(top_frame, "[ Владелец ]", 3, 1)
        # Кнопка Добавить
        button(top_frame, "Добавить", self.create, 3, 2)
        # Кнопка списка
        button(top_frame, "Вывести список", self.show_list, 3, 3)

        # Выбор ID
        self.pet_ID_entry = entry_with_label(mod_frame, "[ Выбор ID ]", 0, 1)
        # Кнопки правки
        button(mod_frame, "Найти", self.read, 0, 2)
        button(mod_frame, "Правка", self.update, 0, 3)
        button(mod_frame, "Удалить", self.delete, 0, 4)
        
        """ СПИСОК """
        # Cписок питомцев и его скроллбар
        self.text_area = tk.Text(bottom_frame)
        self.text_area.grid(row=0, column=0, sticky="nsew")
        self.scroll = tk.Scrollbar(bottom_frame)
        self.scroll.grid(row=0, column=1, sticky="ns")
        # Привязка скролл-бара к текстовому полю
        self.text_area.config(yscrollcommand=self.scroll.set)
        self.scroll.config(command=self.text_area.yview)
        # Растяжение фрейма bottom_frame
        bottom_frame.grid_rowconfigure(0, weight=1)
        bottom_frame.grid_columnconfigure(0, weight=1)

    def show_list(self):
        self.text_area.delete(1.0, tk.END)
        for ID, pet_info in self.pets.items():
            self.text_area.insert(tk.END, f' {ID}. {pet_info["Вид питомца"]} по кличке {pet_info["pet_name"]}. Возраст: {pet_info["Возраст питомца"]}. Владелец: {pet_info["Имя владельца"]}\n')

    def create(self):
        # обработка возраста
        try:
            age = int(self.age_entry.get())
        except ValueError:
            messagebox.showerror("Ошибка", "Пожалуйста, введите целочисленное значение для возраста.")
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
            self.text_area.insert(tk.END, f' {ID}. {pet_info["Вид питомца"]} по кличке {pet_info["pet_name"]}. Возраст: {pet_info["Возраст питомца"]}. Владелец: {pet_info["Имя владельца"]}\n')
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

root = tk.Tk()
root.geometry("720x600")
app = PetApp(root)
root.mainloop()