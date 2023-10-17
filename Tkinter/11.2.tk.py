import tkinter as tk
from tkinter import messagebox
import collections

class PetApp:
    def __init__(self, master):
        self.master = master
        self.master.title("VetPet")
        self.pets = collections.OrderedDict()

        # Создаем верхний и нижний фреймы
        top_frame = tk.Frame(master)
        mod_frame = tk.Frame(master)
        bottom_frame = tk.Frame(master)
        top_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=False)
        mod_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=False)
        bottom_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        """ ВВОД """
        # Вид
        tk.Label(top_frame, text="[ Вид ]").grid(row=0, column=0, padx=5, sticky="e")
        self.subj_entry = tk.Entry(top_frame)
        self.subj_entry.grid(row=0, column=1, ipady=3, sticky="ew")
        # Кличка
        tk.Label(top_frame, text="[ Кличка ]").grid(row=1, column=0, padx=5, sticky="e")
        self.pet_name_entry = tk.Entry(top_frame)
        self.pet_name_entry.grid(row=1, column=1, ipady=3, sticky="ew")
        # Возраст
        tk.Label(top_frame, text="[ Возраст ]").grid(row=2, column=0, padx=5, sticky="e")
        self.age_entry = tk.Entry(top_frame)
        self.age_entry.grid(row=2, column=1, ipady=3, sticky="ew")
        # Владелец
        tk.Label(top_frame, text="[ Владелец ]").grid(row=3, column=0, padx=5, sticky="e")
        self.owner_entry = tk.Entry(top_frame)
        self.owner_entry.grid(row=3, column=1, ipady=3, sticky="ew")
        # Кнопка Добавить
        tk.Button(top_frame, text="Добавить", command=self.create).grid(row=3, column=3, sticky="ew")
        # Фиксированный размер top_frame
        top_frame.grid_rowconfigure(0, weight=1)
        top_frame.grid_rowconfigure(1, weight=1)
        top_frame.grid_rowconfigure(2, weight=1)
        top_frame.grid_rowconfigure(3, weight=1)
        top_frame.grid_rowconfigure(4, weight=1)
        top_frame.grid_columnconfigure(1, weight=1)

        """ ПРАВКА """
        # Выбор ID
        tk.Label(mod_frame, text="[ Выбор ID ]").grid(row=0, column=0, padx=5, sticky="w")
        self.pet_ID_entry = tk.Entry(mod_frame)
        self.pet_ID_entry.grid(row=0, column=1, padx=0, ipady=3, sticky="ew")
        # Кнопки правки
        tk.Button(mod_frame, text="Найти", command=self.read).grid(row=0, column=2, pady=0, ipady=0, sticky="ew")
        tk.Button(mod_frame, text="Правка", command=self.update).grid(row=0, column=3, pady=0, ipady=0, sticky="ew")
        tk.Button(mod_frame, text="Удалить", command=self.delete).grid(row=0, column=4, pady=0, ipady=0, sticky="ew")
        # ХЗ, пригодится
        tk.Label(mod_frame, text="").grid(row=0, column=5, padx=40, sticky="w")
        # Кнопка списка
        tk.Button(mod_frame, text="Вывести список", command=self.show_list).grid(row=0, column=6, pady=0, ipady=0, sticky="e")
        
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

# ---[ S T A R T ]---
root = tk.Tk()
root.geometry("720x600")
app = PetApp(root)
root.mainloop()
