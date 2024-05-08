import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QListWidget


class AddressBook(QWidget):
    def __init__(self):
        super().__init__()

        self.contacts = {}

        self.setWindowTitle("Address Book")
        self.setGeometry(100, 100, 400, 300)

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.name_label = QLabel("Name:")
        self.name_input = QLineEdit()
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_input)

        self.phone_label = QLabel("Phone:")
        self.phone_input = QLineEdit()
        layout.addWidget(self.phone_label)
        layout.addWidget(self.phone_input)

        self.add_button = QPushButton("Add Contact")
        self.add_button.clicked.connect(self.add_contact)
        layout.addWidget(self.add_button)

        self.delete_button = QPushButton("Delete Contact")
        self.delete_button.clicked.connect(self.delete_contact)
        layout.addWidget(self.delete_button)

        self.contacts_list = QListWidget()
        layout.addWidget(self.contacts_list)

        self.setLayout(layout)

    def add_contact(self):
        name = self.name_input.text()
        phone = self.phone_input.text()

        if name and phone:
            self.contacts[name] = phone
            self.contacts_list.addItem(f"{name}: {phone}")
            self.name_input.clear()
            self.phone_input.clear()
        else:
            QMessageBox.warning(self, "Warning", "Please enter both name and phone number.")

    def delete_contact(self):
        selected_contact = self.contacts_list.currentItem()
        if selected_contact:
            name, _ = selected_contact.text().split(":")
            del self.contacts[name]
            self.contacts_list.takeItem(self.contacts_list.row(selected_contact))
        else:
            QMessageBox.warning(self, "Warning", "Please select a contact to delete.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AddressBook()
    window.show()
    sys.exit(app.exec_())