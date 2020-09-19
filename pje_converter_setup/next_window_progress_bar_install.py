# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\next_window_progress_bar_install.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Pje_converter_setup_install_progress_bar(object):
    def setupUi(self, Pje_converter_setup_install_progress_bar):
        Pje_converter_setup_install_progress_bar.setObjectName("Pje_converter_setup_install_progress_bar")
        Pje_converter_setup_install_progress_bar.resize(578, 396)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/TJRN/pjeMini.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Pje_converter_setup_install_progress_bar.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(Pje_converter_setup_install_progress_bar)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, -10, 581, 401))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.frame)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(310, 310, 251, 71))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontal_layout_buttons_next_install = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontal_layout_buttons_next_install.setContentsMargins(0, 0, 0, 0)
        self.horizontal_layout_buttons_next_install.setObjectName("horizontal_layout_buttons_next_install")
        self.button_back_pre_install = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.button_back_pre_install.setObjectName("button_back_pre_install")
        self.horizontal_layout_buttons_next_install.addWidget(self.button_back_pre_install)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontal_layout_buttons_next_install.addItem(spacerItem)
        self.button_close = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.button_close.setObjectName("button_close")
        self.horizontal_layout_buttons_next_install.addWidget(self.button_close)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontal_layout_buttons_next_install.addItem(spacerItem1)
        self.button_install = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.button_install.setObjectName("button_install")
        self.horizontal_layout_buttons_next_install.addWidget(self.button_install)
        self.progress_bar_install = QtWidgets.QProgressBar(self.frame)
        self.progress_bar_install.setGeometry(QtCore.QRect(90, 150, 411, 31))
        self.progress_bar_install.setProperty("value", 0)
        self.progress_bar_install.setObjectName("progress_bar_install")
        Pje_converter_setup_install_progress_bar.setCentralWidget(self.centralwidget)

        self.retranslateUi(Pje_converter_setup_install_progress_bar)
        self.button_back_pre_install.clicked.connect(Pje_converter_setup_install_progress_bar.close)
        QtCore.QMetaObject.connectSlotsByName(Pje_converter_setup_install_progress_bar)

    def retranslateUi(self, Pje_converter_setup_install_progress_bar):
        _translate = QtCore.QCoreApplication.translate
        Pje_converter_setup_install_progress_bar.setWindowTitle(_translate("Pje_converter_setup_install_progress_bar", "PJe Converter Setup"))
        self.button_back_pre_install.setText(_translate("Pje_converter_setup_install_progress_bar", "Voltar"))
        self.button_close.setText(_translate("Pje_converter_setup_install_progress_bar", "Finalizar"))
        self.button_install.setText(_translate("Pje_converter_setup_install_progress_bar", "Instalar"))
import resources_pje_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Pje_converter_setup_install_progress_bar = QtWidgets.QMainWindow()
    ui = Ui_Pje_converter_setup_install_progress_bar()
    ui.setupUi(Pje_converter_setup_install_progress_bar)
    Pje_converter_setup_install_progress_bar.show()
    sys.exit(app.exec_())
