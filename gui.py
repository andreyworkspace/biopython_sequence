#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QFileDialog, QMainWindow, QTextEdit, QHBoxLayout, QVBoxLayout, QPushButton
from seqParser import seq_parser


class Example(QMainWindow):
    log_out = None

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # параметры окна
        self.setWindowTitle('sequence parser')
        self.resize(500, 300)
        self.center()

        # создаём центральный виджет
        wid = QWidget(self)
        self.setCentralWidget(wid)

        # лэйаут
        hbox = QHBoxLayout()
        wid.setLayout(hbox)

        # поле для текста
        self.log_out = QTextEdit(self)
        self.log_out.setReadOnly(True)
        self.log_out.setLineWrapMode(QTextEdit.NoWrap)
        font = self.log_out.font()
        font.setFamily("Courier")
        font.setPointSize(10)

        # кнопка выбора файла
        button_file_select = QPushButton('выбрать файл', self)
        button_file_select.clicked.connect(self.open_file_names_dialog)

        # кнопка очистки текстового поля
        button_clear = QPushButton('очистить', self)
        button_clear.clicked.connect(self.log_out.clear)

        # лэйаут для кнопок
        vbox = QVBoxLayout()

        # добавляем элементы
        hbox.addWidget(self.log_out)
        hbox.addLayout(vbox)
        vbox.addWidget(button_file_select)
        vbox.addWidget(button_clear)
        self.show()

    # центрирует окно
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    # вызывается окно выбора файла
    def open_file_names_dialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        files, _ = QFileDialog.getOpenFileNames(self, "select sequence files", ".", "All Files (*)", options=options)
        if files:
            for fileName in files:
                seq_parser(fileName, self.log_out.append)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
