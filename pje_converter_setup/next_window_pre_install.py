# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\next_window_pre_install.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Pje_converter_setup_pre_install(object):
    def setupUi(self, Pje_converter_setup_pre_install):
        Pje_converter_setup_pre_install.setObjectName("Pje_converter_setup_pre_install")
        Pje_converter_setup_pre_install.resize(578, 396)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/TJRN/pjeMini.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Pje_converter_setup_pre_install.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(Pje_converter_setup_pre_install)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, -10, 581, 401))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.frame)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(350, 310, 191, 71))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontal_layout_buttons_next_install = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontal_layout_buttons_next_install.setContentsMargins(0, 0, 0, 0)
        self.horizontal_layout_buttons_next_install.setObjectName("horizontal_layout_buttons_next_install")
        self.button_back = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.button_back.setObjectName("button_back")
        self.horizontal_layout_buttons_next_install.addWidget(self.button_back)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontal_layout_buttons_next_install.addItem(spacerItem)
        self.button_next_for_install = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.button_next_for_install.setObjectName("button_next_for_install")
        self.horizontal_layout_buttons_next_install.addWidget(self.button_next_for_install)
        self.text_pre_install = QtWidgets.QLabel(self.frame)
        self.text_pre_install.setGeometry(QtCore.QRect(70, 69, 401, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.text_pre_install.setFont(font)
        self.text_pre_install.setObjectName("text_pre_install")
        self.label_directory_install = QtWidgets.QLabel(self.frame)
        self.label_directory_install.setGeometry(QtCore.QRect(70, 130, 131, 16))
        self.label_directory_install.setObjectName("label_directory_install")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.frame)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(70, 140, 431, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontal_layout_change_directory_install = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontal_layout_change_directory_install.setContentsMargins(0, 0, 0, 0)
        self.horizontal_layout_change_directory_install.setObjectName("horizontal_layout_change_directory_install")
        self.input_directory_install = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.input_directory_install.setObjectName("input_directory_install")
        self.horizontal_layout_change_directory_install.addWidget(self.input_directory_install)
        self.button_change_directory = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.button_change_directory.setObjectName("button_change_directory")
        self.horizontal_layout_change_directory_install.addWidget(self.button_change_directory)
        Pje_converter_setup_pre_install.setCentralWidget(self.centralwidget)

        self.retranslateUi(Pje_converter_setup_pre_install)
        self.button_back.clicked.connect(Pje_converter_setup_pre_install.close)
        QtCore.QMetaObject.connectSlotsByName(Pje_converter_setup_pre_install)

    def retranslateUi(self, Pje_converter_setup_pre_install):
        _translate = QtCore.QCoreApplication.translate
        Pje_converter_setup_pre_install.setWindowTitle(_translate("Pje_converter_setup_pre_install", "PJe Converter Setup"))
        self.button_back.setText(_translate("Pje_converter_setup_pre_install", "Voltar"))
        self.button_next_for_install.setText(_translate("Pje_converter_setup_pre_install", "Avançar"))
        self.text_pre_install.setText(_translate("Pje_converter_setup_pre_install", "Clique em instalar para prosseguir"))
        self.label_directory_install.setText(_translate("Pje_converter_setup_pre_install", "Local de Instalação"))
        self.button_change_directory.setText(_translate("Pje_converter_setup_pre_install", "Alterar"))
import resources_pje_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Pje_converter_setup_pre_install = QtWidgets.QMainWindow()
    ui = Ui_Pje_converter_setup_pre_install()
    ui.setupUi(Pje_converter_setup_pre_install)
    Pje_converter_setup_pre_install.show()
    sys.exit(app.exec_())
