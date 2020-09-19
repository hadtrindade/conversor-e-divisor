# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\main_window.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Pje_converter_setup(object):
    def setupUi(self, Pje_converter_setup):
        Pje_converter_setup.setObjectName("Pje_converter_setup")
        Pje_converter_setup.resize(578, 396)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/TJRN/pjeMini.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Pje_converter_setup.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(Pje_converter_setup)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, -1, 581, 401))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_pje_converter_center = QtWidgets.QLabel(self.frame)
        self.label_pje_converter_center.setGeometry(QtCore.QRect(10, 0, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_pje_converter_center.setFont(font)
        self.label_pje_converter_center.setObjectName("label_pje_converter_center")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.frame)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(350, 300, 191, 71))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.button_exit = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.button_exit.setObjectName("button_exit")
        self.horizontalLayout.addWidget(self.button_exit)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.button_next = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.button_next.setObjectName("button_next")
        self.horizontalLayout.addWidget(self.button_next)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.frame)
        self.plainTextEdit.setGeometry(QtCore.QRect(40, 70, 501, 181))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.frame)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 270, 501, 51))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.button_radio_accept = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.button_radio_accept.setObjectName("button_radio_accept")
        self.verticalLayout.addWidget(self.button_radio_accept)
        self.button_radio_not_accept = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.button_radio_not_accept.setChecked(True)
        self.button_radio_not_accept.setObjectName("button_radio_not_accept")
        self.verticalLayout.addWidget(self.button_radio_not_accept)
        self.termos_uso_label = QtWidgets.QLabel(self.frame)
        self.termos_uso_label.setGeometry(QtCore.QRect(40, 50, 91, 16))
        self.termos_uso_label.setObjectName("termos_uso_label")
        Pje_converter_setup.setCentralWidget(self.centralwidget)

        self.retranslateUi(Pje_converter_setup)
        self.button_exit.clicked.connect(Pje_converter_setup.close)
        self.button_radio_not_accept.clicked['bool'].connect(self.button_next.hide)
        self.button_radio_accept.toggled['bool'].connect(self.button_next.setVisible)
        QtCore.QMetaObject.connectSlotsByName(Pje_converter_setup)

    def retranslateUi(self, Pje_converter_setup):
        _translate = QtCore.QCoreApplication.translate
        Pje_converter_setup.setWindowTitle(_translate("Pje_converter_setup", "PJe Converter Setup"))
        self.label_pje_converter_center.setText(_translate("Pje_converter_setup", "PJe Converter Setup"))
        self.button_exit.setText(_translate("Pje_converter_setup", "Sair"))
        self.button_next.setText(_translate("Pje_converter_setup", "Avançar"))
        self.button_radio_accept.setText(_translate("Pje_converter_setup", "Aceitos os termos de uso."))
        self.button_radio_not_accept.setText(_translate("Pje_converter_setup", "Não aceito os termos de uso."))
        self.termos_uso_label.setText(_translate("Pje_converter_setup", "Termos de uso"))
import resources_pje_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Pje_converter_setup = QtWidgets.QMainWindow()
    ui = Ui_Pje_converter_setup()
    ui.setupUi(Pje_converter_setup)
    Pje_converter_setup.show()
    sys.exit(app.exec_())
