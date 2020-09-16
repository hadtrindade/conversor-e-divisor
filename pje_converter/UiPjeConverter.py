# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\pje-converter.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import resources_pje_rc
from pathlib import Path


class UiPjeConverter:
    def setupUi(self, PjeConverter):
        PjeConverter.setObjectName("PjeConverter")
        PjeConverter.resize(723, 379)
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap(":/TJRN/pjeMini.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off
        )
        PjeConverter.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(PjeConverter)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.grid_layout_main = QtWidgets.QFrame(self.centralwidget)
        self.grid_layout_main.setStyleSheet(
            "image: url(:/newPrefix/bn-poder-judiciario.png);\n" ""
        )
        self.grid_layout_main.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.grid_layout_main.setFrameShadow(QtWidgets.QFrame.Raised)
        self.grid_layout_main.setObjectName("grid_layout_main")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.grid_layout_main)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(80, 190, 561, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontal_layout_search_file = QtWidgets.QHBoxLayout(
            self.horizontalLayoutWidget
        )
        self.horizontal_layout_search_file.setContentsMargins(0, 0, 0, 0)
        self.horizontal_layout_search_file.setObjectName(
            "horizontal_layout_search_file"
        )
        self.input_file = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.input_file.setObjectName("input_file")
        self.horizontal_layout_search_file.addWidget(self.input_file)
        self.search_file_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.search_file_button.setObjectName("search_file_button")
        self.horizontal_layout_search_file.addWidget(self.search_file_button)

        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.grid_layout_main)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(260, 280, 221, 80))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontal_layout_start = QtWidgets.QHBoxLayout(
            self.horizontalLayoutWidget_2
        )
        self.horizontal_layout_start.setContentsMargins(0, 0, 0, 0)
        self.horizontal_layout_start.setObjectName("horizontal_layout_start")
        self.start_progress_button = QtWidgets.QPushButton(
            self.horizontalLayoutWidget_2
        )
        self.start_progress_button.setObjectName("start_progress_button")
        self.horizontal_layout_start.addWidget(self.start_progress_button)

        self.logo_tjrn = QtWidgets.QFrame(self.grid_layout_main)
        self.logo_tjrn.setGeometry(QtCore.QRect(180, 30, 361, 111))
        self.logo_tjrn.setStyleSheet("image: url(:/TJRN/bn-poder-judiciario.png);")
        self.logo_tjrn.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.logo_tjrn.setFrameShadow(QtWidgets.QFrame.Raised)
        self.logo_tjrn.setObjectName("logo_tjrn")
        self.gridLayout.addWidget(self.grid_layout_main, 0, 0, 1, 1)
        PjeConverter.setCentralWidget(self.centralwidget)

        self.retranslateUi(PjeConverter)
        self.start_progress_button.clicked.connect(self.input_file.copy)
        QtCore.QMetaObject.connectSlotsByName(PjeConverter)

    def retranslateUi(self, PjeConverter):
        _translate = QtCore.QCoreApplication.translate
        PjeConverter.setWindowTitle(_translate("PjeConverter", "PJE Converter"))
        self.search_file_button.setText(_translate("PjeConverter", "Procurar"))
        self.start_progress_button.setText(_translate("PjeConverter", "Iniciar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PjeConverter = QtWidgets.QMainWindow()
    ui = UiPjeConverter()
    ui.setupUi(PjeConverter)
    PjeConverter.show()
    sys.exit(app.exec_())
