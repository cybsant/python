import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QGridLayout, QLineEdit, QTextEdit, QScrollArea, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIntValidator

class PetApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("VetPet")
        self.setGeometry(500, 500, 500, 400)
        self.pets = {}

        self.layout = QVBoxLayout()

        self.top_layout = QGridLayout()
        self.middle_layout = QGridLayout()
        self.bottom_layout = QGridLayout()

        self.subj_entry = QLineEdit(self)
        self.pet_name_entry = QLineEdit(self)
        self.age_entry = QLineEdit(self)
        self.age_entry.setValidator(QIntValidator(0, 100))  # выбран ограничитель для числовой ввода возраста
        self.owner_entry = QLineEdit(self)

        self.top_layout.addWidget(QLabel("[ Вид ]"), 0, 0)
        self.top_layout.addWidget(self.subj_entry, 0, 1)
        self.top_layout.addWidget(QLabel("[ Кличка ]"), 1, 0)
        self.top_layout.addWidget(self.pet_name_entry, 1, 1)
        self.top_layout.addWidget(QLabel("[ Возраст ]"), 2, 0)
        self.top_layout.addWidget(self.age_entry, 2, 1)
        self.top_layout.addWidget(QLabel("[ Владелец ]"), 3, 0)
        self.top_layout.addWidget(self.owner_entry, 3, 1)
        self.top_layout.addWidget(QPushButton("Добавить", clicked=self.create), 4, 1)

        self.pet_id_entry = QLineEdit(self)
        self.middle_layout.addWidget(QLabel("[ Выбор ID ]"), 0, 0)
        self.middle_layout.addWidget(self.pet_id_entry, 0, 1)
        self.middle_layout.addWidget(QPushButton("Найти", clicked=self.read), 0, 2)
        self.middle_layout.addWidget(QPushButton("Правка", clicked=self.update), 0, 3)
        self.middle_layout.addWidget(QPushButton("Удалить", clicked=self.delete), 0, 4)
        self.middle_layout.addWidget(QPushButton("Вывести список", clicked=self.show_list), 0, 5)

        self.text_area = QTextEdit(self)
        self.text_area.setReadOnly(True)
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidget(self.text_area)
        self.scroll_area.setWidgetResizable(True)
        self.bottom_layout.addWidget(self.scroll_area, 0, 0)

        self.layout.addLayout(self.top_layout)
        self.layout.addLayout(self.middle_layout)
        self.layout.addLayout(self.bottom_layout)

        self.setLayout(self.layout)

    def show_list(self):
        self.text_area.clear()
        for ID, pet_info in self.pets.items():
            self.text_area.append(f' {ID}. {pet_info["Вид питомца"]} по кличке {pet_info["pet_name"]}. Возраст: {pet_info["Возраст питомца"]}. Владелец: {pet_info["Имя владельца"]}\n')

    def create(self):
        try:
            age = int(self.age_entry.text())
        except ValueError:
            QMessageBox.warning(self, "Ошибка", "Пожалуйста, введите целочисленное значение для возраста.")
        ID = max(self.pets.keys(), default=0) + 1
        self.pets[ID] = {
            "pet_name": self.pet_name_entry.text(),
            "Вид питомца": self.subj_entry.text(),
            "Возраст питомца": age,
            "Имя владельца": self.owner_entry.text()
        }

    def delete(self):
        try:
            ID = int(self.pet_id_entry.text())
            if ID in self.pets:
                del self.pets[ID]
                QMessageBox.information(self, 'Удалено', f'{ID} удален')
            else:
                QMessageBox.warning(self, "Ошибка!", "Питомец с таким ID не найден")
        except ValueError:
            QMessageBox.warning(self, "Ошибка!", "Питомец с таким ID не найден")

    def read(self):
        try:
            ID = int(self.pet_id_entry.text())
            if ID in self.pets:
                self.text_area.clear()
                pet_info = self.pets[ID]
                self.text_area.append(f' {ID}. {pet_info["Вид питомца"]} по кличке {pet_info["pet_name"]}. Возраст: {pet_info["Возраст питомца"]}. Владелец: {pet_info["Имя владельца"]}\n')
            else:
                QMessageBox.warning(self, "Ошибка!", "Питомец с таким ID не найден")
        except ValueError:
            QMessageBox.warning(self, "Ошибка!", "Питомец с таким ID не найден")

    def update(self):
        try:
            ID = int(self.pet_id_entry.text())
            if ID in self.pets:
                del self.pets[ID]
                self.pets[ID] = {
                    "pet_name": self.pet_name_entry.text(),
                    "Вид питомца": self.subj_entry.text(),
                    "Возраст питомца": self.age_entry.text(),
                    "Имя владельца": self.owner_entry.text()
                }
            else:
                QMessageBox.warning(self, "Ошибка!", "Питомец с таким ID не найден")
        except ValueError:
            QMessageBox.warning(self, "Ошибка!", "Питомец с таким ID не найден")


# ---[ start ]---
app = QApplication(sys.argv)
ex = PetApp()
ex.show()
sys.exit(app.exec_())