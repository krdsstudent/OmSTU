import sys
import os
from PyQt5 import QtWidgets, QtCore
import PyQt5

os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = os.path.join(
    os.path.dirname(PyQt5.__file__), 'Qt5', 'plugins', 'platforms'
)


class TrackerApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):

        self.setWindowTitle('Вход в Трекер Привычек')
        self.resize(300, 150)


        self.label = QtWidgets.QLabel('Введите логин и пароль:', self)
        self.login_input = QtWidgets.QLineEdit(self)
        self.login_input.setPlaceholderText('Логин')

        self.pass_input = QtWidgets.QLineEdit(self)
        self.pass_input.setPlaceholderText('Пароль')
        self.pass_input.setEchoMode(QtWidgets.QLineEdit.Password)  # Скрываем пароль звездочками

        self.btn = QtWidgets.QPushButton('Войти', self)

        # Размещаем элементы друг под другом
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.login_input)
        layout.addWidget(self.pass_input)
        layout.addWidget(self.btn)
        self.setLayout(layout)

        self.btn.clicked.connect(self.login_action)

    def login_action(self):
        login = self.login_input.text()
        password = self.pass_input.text()


        if login == "Cristiano_Ronaldo" and password == "Siiiiiii":
            QtWidgets.QMessageBox.information(self, 'Успех', 'Добро пожаловать, Чемпион!')
        else:
            QtWidgets.QMessageBox.warning(self, 'Ошибка', 'Неверный логин или пароль!')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = TrackerApp()
    ex.show()
    sys.exit(app.exec_())