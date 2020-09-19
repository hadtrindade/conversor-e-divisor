# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\main_window_template.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Pje_converter_setup_template_window(object):
    def setupUi(self, Pje_converter_setup_template_window):
        Pje_converter_setup_template_window.setObjectName("Pje_converter_setup_template_window")
        Pje_converter_setup_template_window.resize(578, 396)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/TJRN/pjeMini.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Pje_converter_setup_template_window.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(Pje_converter_setup_template_window)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, -10, 581, 401))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        Pje_converter_setup_template_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(Pje_converter_setup_template_window)
        QtCore.QMetaObject.connectSlotsByName(Pje_converter_setup_template_window)

    def retranslateUi(self, Pje_converter_setup_template_window):
        _translate = QtCore.QCoreApplication.translate
        Pje_converter_setup_template_window.setWindowTitle(_translate("Pje_converter_setup_template_window", "PJe Converter Setup"))
import resources_pje_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Pje_converter_setup_template_window = QtWidgets.QMainWindow()
    ui = Ui_Pje_converter_setup_template_window()
    ui.setupUi(Pje_converter_setup_template_window)
    Pje_converter_setup_template_window.show()
    sys.exit(app.exec_())
