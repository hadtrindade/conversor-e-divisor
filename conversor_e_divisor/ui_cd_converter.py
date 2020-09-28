# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_pje_converter.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_cd_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QSize(800, 600))
        MainWindow.setMaximumSize(QSize(800, 600))
        icon = QIcon()
        icon.addFile(u":/MainIcon/cil-media-play.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.centralwidget)
        self.content.setObjectName(u"content")
        self.content.setStyleSheet(u"background-color: rgb(235, 240, 243);")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.content)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu = QFrame(self.content)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        self.frame_left_menu.setMinimumSize(QSize(0, 0))
        self.frame_left_menu.setMaximumSize(QSize(70, 16777215))
        self.frame_left_menu.setStyleSheet(u"background-color: rgb(0, 120, 170);")
        self.frame_left_menu.setFrameShape(QFrame.StyledPanel)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_top_menus = QFrame(self.frame_left_menu)
        self.frame_top_menus.setObjectName(u"frame_top_menus")
        self.frame_top_menus.setFrameShape(QFrame.StyledPanel)
        self.frame_top_menus.setFrameShadow(QFrame.Raised)
        self.layout_menu_top = QVBoxLayout(self.frame_top_menus)
        self.layout_menu_top.setSpacing(0)
        self.layout_menu_top.setObjectName(u"layout_menu_top")
        self.layout_menu_top.setContentsMargins(0, 0, 0, 0)
        self.button_toggle = QPushButton(self.frame_top_menus)
        self.button_toggle.setObjectName(u"button_toggle")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_toggle.sizePolicy().hasHeightForWidth())
        self.button_toggle.setSizePolicy(sizePolicy)
        self.button_toggle.setMinimumSize(QSize(70, 40))
        self.button_toggle.setStyleSheet(u"QPushButton {\n"
"	color: rgb(235, 240, 243);\n"
"	background-color: rgb(0, 120, 170);	\n"
"	border: 0px solid;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(0, 130,180 );	\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/MenuIcon/cil-menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_toggle.setIcon(icon1)
        self.button_toggle.setIconSize(QSize(50, 40))

        self.layout_menu_top.addWidget(self.button_toggle, 0, Qt.AlignLeft)

        self.button_page_1 = QPushButton(self.frame_top_menus)
        self.button_page_1.setObjectName(u"button_page_1")
        sizePolicy.setHeightForWidth(self.button_page_1.sizePolicy().hasHeightForWidth())
        self.button_page_1.setSizePolicy(sizePolicy)
        self.button_page_1.setMinimumSize(QSize(70, 40))
        self.button_page_1.setStyleSheet(u"QPushButton {\n"
"	color: rgb(235, 240, 243);\n"
"	background-color: rgb(0, 120, 170);	\n"
"	border: 0px solid;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(0, 130,180 );	\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/menu_CC/cil-movie.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_page_1.setIcon(icon2)
        self.button_page_1.setIconSize(QSize(50, 40))

        self.layout_menu_top.addWidget(self.button_page_1, 0, Qt.AlignLeft)

        self.button_page_2 = QPushButton(self.frame_top_menus)
        self.button_page_2.setObjectName(u"button_page_2")
        self.button_page_2.setMinimumSize(QSize(70, 40))
        self.button_page_2.setStyleSheet(u"QPushButton {\n"
"	color: rgb(235, 240, 243);\n"
"	background-color: rgb(0, 120, 170);	\n"
"	border: 0px solid;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(0, 130,180 );	\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/menu_C/cil-view-module.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_page_2.setIcon(icon3)
        self.button_page_2.setIconSize(QSize(50, 40))

        self.layout_menu_top.addWidget(self.button_page_2, 0, Qt.AlignLeft)


        self.verticalLayout_3.addWidget(self.frame_top_menus, 0, Qt.AlignLeft|Qt.AlignTop)

        self.frame_botton_menus = QFrame(self.frame_left_menu)
        self.frame_botton_menus.setObjectName(u"frame_botton_menus")
        self.frame_botton_menus.setFrameShape(QFrame.StyledPanel)
        self.frame_botton_menus.setFrameShadow(QFrame.Raised)
        self.layout_menu_botton = QVBoxLayout(self.frame_botton_menus)
        self.layout_menu_botton.setSpacing(0)
        self.layout_menu_botton.setObjectName(u"layout_menu_botton")
        self.layout_menu_botton.setContentsMargins(0, 0, 0, 0)
        self.button_settings = QPushButton(self.frame_botton_menus)
        self.button_settings.setObjectName(u"button_settings")
        self.button_settings.setMinimumSize(QSize(70, 40))
        self.button_settings.setStyleSheet(u"QPushButton {\n"
"	color: rgb(235, 240, 243);\n"
"	background-color: rgb(0, 120, 170);	\n"
"	border: 0px solid;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(0, 130,180 );	\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/Menu_Settings/cil-options-horizontal.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_settings.setIcon(icon4)
        self.button_settings.setIconSize(QSize(70, 40))

        self.layout_menu_botton.addWidget(self.button_settings, 0, Qt.AlignLeft)


        self.verticalLayout_3.addWidget(self.frame_botton_menus, 0, Qt.AlignLeft|Qt.AlignBottom)


        self.horizontalLayout_2.addWidget(self.frame_left_menu)

        self.frame_pages = QFrame(self.content)
        self.frame_pages.setObjectName(u"frame_pages")
        self.frame_pages.setStyleSheet(u"background-color: rgb(235, 240, 243);")
        self.frame_pages.setFrameShape(QFrame.NoFrame)
        self.frame_pages.setFrameShadow(QFrame.Raised)
        self.stackedWidget = QStackedWidget(self.frame_pages)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 0, 730, 570))
        self.stackedWidget.setMinimumSize(QSize(550, 570))
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.page_1.setStyleSheet(u"background-color: rgb(235, 240, 243);")
        self.vboxLayout = QVBoxLayout(self.page_1)
        self.vboxLayout.setSpacing(0)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.vboxLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_top_page = QFrame(self.page_1)
        self.frame_top_page.setObjectName(u"frame_top_page")
        self.frame_top_page.setMinimumSize(QSize(0, 100))
        self.frame_top_page.setMaximumSize(QSize(16777215, 150))
        self.frame_top_page.setFrameShape(QFrame.StyledPanel)
        self.frame_top_page.setFrameShadow(QFrame.Raised)
        self.label_convert_split = QLabel(self.frame_top_page)
        self.label_convert_split.setObjectName(u"label_convert_split")
        self.label_convert_split.setGeometry(QRect(10, 10, 331, 41))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(24)
        self.label_convert_split.setFont(font)
        self.label_convert_split.setStyleSheet(u"color: rgb(69, 69, 69);")
        self.radio_button_normal = QRadioButton(self.frame_top_page)
        self.radio_button_normal.setObjectName(u"radio_button_normal")
        self.radio_button_normal.setGeometry(QRect(30, 110, 91, 17))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(14)
        self.radio_button_normal.setFont(font1)
        self.radio_button_normal.setStyleSheet(u"QRadioButton::indicator{\n"
"	color: rgb(69, 69, 69);\n"
"	width: 15px;\n"
"	heidght: 15px;\n"
"}")
        self.radio_button_normal.setChecked(True)
        self.radio_button_low = QRadioButton(self.frame_top_page)
        self.radio_button_low.setObjectName(u"radio_button_low")
        self.radio_button_low.setGeometry(QRect(140, 110, 82, 17))
        self.radio_button_low.setFont(font1)
        self.radio_button_low.setStyleSheet(u"QRadioButton::indicator{\n"
"	color: rgb(69, 69, 69);\n"
"	width: 15px;\n"
"	heidght: 15px;\n"
"}")
        self.check_box_split = QCheckBox(self.frame_top_page)
        self.check_box_split.setObjectName(u"check_box_split")
        self.check_box_split.setGeometry(QRect(30, 80, 121, 17))
        self.check_box_split.setFont(font1)
        self.check_box_split.setStyleSheet(u"QCheckBox::indicator{\n"
"	color: rgb(69, 69, 69);\n"
"	width: 15px;\n"
"	heidght: 15px;\n"
"	\n"
"}")
        self.check_box_split.setChecked(False)

        self.vboxLayout.addWidget(self.frame_top_page)

        self.frame = QFrame(self.page_1)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame_start = QFrame(self.frame)
        self.frame_start.setObjectName(u"frame_start")
        self.frame_start.setGeometry(QRect(240, 10, 242, 224))
        self.frame_start.setStyleSheet(u"")
        self.frame_start.setFrameShape(QFrame.StyledPanel)
        self.frame_start.setFrameShadow(QFrame.Raised)
        self.circular_progress_bar_base = QFrame(self.frame_start)
        self.circular_progress_bar_base.setObjectName(u"circular_progress_bar_base")
        self.circular_progress_bar_base.setGeometry(QRect(25, 10, 190, 190))
        self.circular_progress_bar_base.setFrameShape(QFrame.NoFrame)
        self.circular_progress_bar_base.setFrameShadow(QFrame.Raised)
        self.circular_progress = QFrame(self.circular_progress_bar_base)
        self.circular_progress.setObjectName(u"circular_progress")
        self.circular_progress.setGeometry(QRect(10, 10, 170, 170))
        self.circular_progress.setStyleSheet(u"QFrame {\n"
"	border-radius: 85px;\n"
"	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.749 rgba(217, 237, 247, 0), stop:0.750 rgba(0, 120, 170, 255));\n"
"\n"
"}")
        self.circular_progress.setFrameShape(QFrame.NoFrame)
        self.circular_progress.setFrameShadow(QFrame.Raised)
        self.circular_bg = QFrame(self.circular_progress_bar_base)
        self.circular_bg.setObjectName(u"circular_bg")
        self.circular_bg.setGeometry(QRect(10, 10, 170, 170))
        self.circular_bg.setStyleSheet(u"QFrame{\n"
"	border-radius: 85px;\n"
"	background-color: rgb(217, 237, 247);\n"
"}")
        self.circular_bg.setFrameShape(QFrame.NoFrame)
        self.circular_bg.setFrameShadow(QFrame.Raised)
        self.container = QFrame(self.circular_progress_bar_base)
        self.container.setObjectName(u"container")
        self.container.setGeometry(QRect(20, 20, 150, 150))
        self.container.setStyleSheet(u"QFrame {\n"
"	border-radius: 75px;\n"
"	background-color: rgb(150, 215, 247);\n"
"}")
        self.container.setFrameShape(QFrame.NoFrame)
        self.container.setFrameShadow(QFrame.Raised)
        self.button_start = QPushButton(self.container)
        self.button_start.setObjectName(u"button_start")
        self.button_start.setGeometry(QRect(30, 30, 91, 91))
        self.button_start.setMinimumSize(QSize(70, 70))
        self.button_start.setMaximumSize(QSize(100, 100))
        self.button_start.setStyleSheet(u"QPushButton {\n"
"	color:  rgb(235, 240, 243);\n"
"	border: 0px solid;\n"
"	border-radius: 5px;\n"
"	background-position: center;\n"
"	background-color: rgb(0, 120, 170);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border: 2px solid  rgb(235, 240, 243);\n"
"	background-color: rgb(0, 130,180 );\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	color: rgb(69, 69, 69);\n"
"	background-color: rgb(217, 237, 247);\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/button_start/cil-media-play.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_start.setIcon(icon5)
        self.button_start.setIconSize(QSize(100, 100))
        self.circular_bg.raise_()
        self.circular_progress.raise_()
        self.container.raise_()
        self.button_output_file = QPushButton(self.frame)
        self.button_output_file.setObjectName(u"button_output_file")
        self.button_output_file.setGeometry(QRect(550, 70, 100, 100))
        self.button_output_file.setMinimumSize(QSize(70, 70))
        self.button_output_file.setMaximumSize(QSize(100, 100))
        self.button_output_file.setStyleSheet(u"QPushButton {\n"
"	color:  rgb(235, 240, 243);\n"
"	border: 0px solid;\n"
"	border-radius: 5px;\n"
"	background-position: center;\n"
"	background-color: rgb(0, 120, 170);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border: 2px solid  rgb(235, 240, 243);\n"
"	background-color: rgb(0, 130,180 );\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	color: rgb(69, 69, 69);\n"
"	background-color: rgb(217, 237, 247);\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/button_output_file/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_output_file.setIcon(icon6)
        self.button_output_file.setIconSize(QSize(100, 100))
        self.button_source_file = QPushButton(self.frame)
        self.button_source_file.setObjectName(u"button_source_file")
        self.button_source_file.setGeometry(QRect(70, 70, 100, 100))
        self.button_source_file.setMinimumSize(QSize(70, 70))
        self.button_source_file.setMaximumSize(QSize(100, 100))
        self.button_source_file.setStyleSheet(u"QPushButton {\n"
"	color:  rgb(235, 240, 243);\n"
"	border: 0px solid;\n"
"	border-radius: 5px;\n"
"	background-position: center;\n"
"	background-color: rgb(0, 120, 170);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border: 2px solid  rgb(235, 240, 243);\n"
"	background-color: rgb(0, 130,180 );\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	color: rgb(69, 69, 69);\n"
"	background-color: rgb(217, 237, 247);\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/button_search_file/cil-movie.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_source_file.setIcon(icon7)
        self.button_source_file.setIconSize(QSize(100, 100))
        self.button_stop = QPushButton(self.frame)
        self.button_stop.setObjectName(u"button_stop")
        self.button_stop.setGeometry(QRect(260, 250, 200, 40))
        self.button_stop.setMinimumSize(QSize(200, 40))
        self.button_stop.setMaximumSize(QSize(200, 40))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(16)
        self.button_stop.setFont(font2)
        self.button_stop.setStyleSheet(u"QPushButton {\n"
"	color:  rgb(235, 240, 243);\n"
"	border: 0px solid;\n"
"	border-radius: 5px;\n"
"	background-position: center;\n"
"	background-color: rgb(0, 120, 170);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border: 2px solid  rgb(235, 240, 243);\n"
"	background-color: rgb(0, 130,180 );\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	color: rgb(69, 69, 69);\n"
"	background-color: rgb(217, 237, 247);\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u":/button_stop/cil-media-stop.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_stop.setIcon(icon8)
        self.button_stop.setIconSize(QSize(40, 50))
        self.line_edit_input_file = QLineEdit(self.frame)
        self.line_edit_input_file.setObjectName(u"line_edit_input_file")
        self.line_edit_input_file.setGeometry(QRect(10, 190, 221, 31))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(12)
        font3.setBold(True)
        font3.setWeight(75)
        self.line_edit_input_file.setFont(font3)
        self.line_edit_input_file.setStyleSheet(u"QLineEdit {\n"
"	color: rgb(69, 69, 69);\n"
"	border: 0px solid;\n"
"	border-radius: 5px;\n"
"	background-position: center;\n"
"	background-color: rgb(235, 240,243 );\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"	border: 2px solid  rgb(0, 120, 170);\n"
"	background-color: rgb(235, 240,243 );\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	color: rgb(69, 69, 69);\n"
"	background-color: rgb(217, 237, 247);\n"
"}")
        self.line_edit_input_file.setAlignment(Qt.AlignCenter)
        self.line_edit_output_file = QLineEdit(self.frame)
        self.line_edit_output_file.setObjectName(u"line_edit_output_file")
        self.line_edit_output_file.setGeometry(QRect(490, 190, 231, 31))
        self.line_edit_output_file.setFont(font3)
        self.line_edit_output_file.setStyleSheet(u"QLineEdit {\n"
"	color: rgb(69, 69, 69);\n"
"	border: 0px solid;\n"
"	border-radius: 5px;\n"
"	background-position: center;\n"
"	background-color: rgb(235, 240,243 );\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"	border: 2px solid  rgb(0, 120, 170);\n"
"	background-color: rgb(235, 240,243 );\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	color: rgb(69, 69, 69);\n"
"	background-color: rgb(217, 237, 247);\n"
"}")
        self.line_edit_output_file.setAlignment(Qt.AlignCenter)
        self.button_open_folder = QPushButton(self.frame)
        self.button_open_folder.setObjectName(u"button_open_folder")
        self.button_open_folder.setGeometry(QRect(560, 230, 81, 40))
        self.button_open_folder.setMinimumSize(QSize(40, 40))
        self.button_open_folder.setMaximumSize(QSize(100, 100))
        self.button_open_folder.setStyleSheet(u"QPushButton {\n"
"	color:  rgb(235, 240, 243);\n"
"	border: 0px solid;\n"
"	border-radius: 5px;\n"
"	background-position: center;\n"
"	background-color: rgb(0, 120, 170);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border: 2px solid  rgb(235, 240, 243);\n"
"	background-color: rgb(0, 130,180 );\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	color: rgb(69, 69, 69);\n"
"	background-color: rgb(217, 237, 247);\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u":/open_folder/cil-folder.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_open_folder.setIcon(icon9)
        self.button_open_folder.setIconSize(QSize(40, 40))

        self.vboxLayout.addWidget(self.frame)

        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_8 = QVBoxLayout(self.page_2)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_page2 = QFrame(self.page_2)
        self.frame_page2.setObjectName(u"frame_page2")
        self.frame_page2.setMinimumSize(QSize(730, 150))
        self.frame_page2.setStyleSheet(u"background-color: rgb(237, 240, 243);")
        self.frame_page2.setFrameShape(QFrame.StyledPanel)
        self.frame_page2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_page2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_top_page_2 = QFrame(self.frame_page2)
        self.frame_top_page_2.setObjectName(u"frame_top_page_2")
        self.frame_top_page_2.setMinimumSize(QSize(0, 100))
        self.frame_top_page_2.setMaximumSize(QSize(16777215, 150))
        self.frame_top_page_2.setFrameShape(QFrame.StyledPanel)
        self.frame_top_page_2.setFrameShadow(QFrame.Raised)
        self.label_split = QLabel(self.frame_top_page_2)
        self.label_split.setObjectName(u"label_split")
        self.label_split.setGeometry(QRect(10, 10, 331, 41))
        self.label_split.setFont(font)
        self.label_split.setStyleSheet(u"color: rgb(69, 69, 69);")

        self.verticalLayout_2.addWidget(self.frame_top_page_2)

        self.frame_body_page_2 = QFrame(self.frame_page2)
        self.frame_body_page_2.setObjectName(u"frame_body_page_2")
        self.frame_body_page_2.setFrameShape(QFrame.StyledPanel)
        self.frame_body_page_2.setFrameShadow(QFrame.Raised)
        self.button_source_file_split = QPushButton(self.frame_body_page_2)
        self.button_source_file_split.setObjectName(u"button_source_file_split")
        self.button_source_file_split.setGeometry(QRect(90, 70, 100, 100))
        self.button_source_file_split.setMinimumSize(QSize(70, 70))
        self.button_source_file_split.setMaximumSize(QSize(100, 100))
        self.button_source_file_split.setStyleSheet(u"QPushButton {\n"
"	color:  rgb(235, 240, 243);\n"
"	border: 0px solid;\n"
"	border-radius: 5px;\n"
"	background-position: center;\n"
"	background-color: rgb(0, 120, 170);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border: 2px solid  rgb(235, 240, 243);\n"
"	background-color: rgb(0, 130,180 );\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	color: rgb(69, 69, 69);\n"
"	background-color: rgb(217, 237, 247);\n"
"}")
        self.button_source_file_split.setIcon(icon7)
        self.button_source_file_split.setIconSize(QSize(100, 100))
        self.line_edit_input_file_split = QLineEdit(self.frame_body_page_2)
        self.line_edit_input_file_split.setObjectName(u"line_edit_input_file_split")
        self.line_edit_input_file_split.setGeometry(QRect(20, 190, 250, 31))
        self.line_edit_input_file_split.setMinimumSize(QSize(250, 0))
        self.line_edit_input_file_split.setMaximumSize(QSize(16777215, 16777215))
        self.line_edit_input_file_split.setFont(font3)
        self.line_edit_input_file_split.setStyleSheet(u"QLineEdit {\n"
"	color: rgb(69, 69, 69);\n"
"	border: 0px solid;\n"
"	border-radius: 5px;\n"
"	background-position: center;\n"
"	background-color: rgb(235, 240,243 );\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"	border: 2px solid  rgb(0, 120, 170);\n"
"	background-color: rgb(235, 240,243 );\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	color: rgb(69, 69, 69);\n"
"	background-color: rgb(217, 237, 247);\n"
"}")
        self.line_edit_input_file_split.setAlignment(Qt.AlignCenter)
        self.button_start_split = QPushButton(self.frame_body_page_2)
        self.button_start_split.setObjectName(u"button_start_split")
        self.button_start_split.setGeometry(QRect(310, 70, 100, 100))
        self.button_start_split.setMinimumSize(QSize(70, 70))
        self.button_start_split.setMaximumSize(QSize(100, 100))
        self.button_start_split.setStyleSheet(u"QPushButton {\n"
"	color:  rgb(235, 240, 243);\n"
"	border: 0px solid;\n"
"	border-radius: 5px;\n"
"	background-position: center;\n"
"	background-color: rgb(0, 120, 170);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border: 2px solid  rgb(235, 240, 243);\n"
"	background-color: rgb(0, 130,180 );\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	color: rgb(69, 69, 69);\n"
"	background-color: rgb(217, 237, 247);\n"
"}")
        self.button_start_split.setIcon(icon5)
        self.button_start_split.setIconSize(QSize(100, 100))
        self.button_output_file_split = QPushButton(self.frame_body_page_2)
        self.button_output_file_split.setObjectName(u"button_output_file_split")
        self.button_output_file_split.setGeometry(QRect(540, 70, 100, 100))
        self.button_output_file_split.setMinimumSize(QSize(70, 70))
        self.button_output_file_split.setMaximumSize(QSize(100, 100))
        self.button_output_file_split.setStyleSheet(u"QPushButton {\n"
"	color:  rgb(235, 240, 243);\n"
"	border: 0px solid;\n"
"	border-radius: 5px;\n"
"	background-position: center;\n"
"	background-color: rgb(0, 120, 170);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border: 2px solid  rgb(235, 240, 243);\n"
"	background-color: rgb(0, 130,180 );\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	color: rgb(69, 69, 69);\n"
"	background-color: rgb(217, 237, 247);\n"
"}")
        self.button_output_file_split.setIcon(icon6)
        self.button_output_file_split.setIconSize(QSize(100, 100))
        self.line_edit_output_file_split = QLineEdit(self.frame_body_page_2)
        self.line_edit_output_file_split.setObjectName(u"line_edit_output_file_split")
        self.line_edit_output_file_split.setGeometry(QRect(460, 190, 250, 31))
        self.line_edit_output_file_split.setMinimumSize(QSize(250, 0))
        self.line_edit_output_file_split.setFont(font3)
        self.line_edit_output_file_split.setStyleSheet(u"QLineEdit {\n"
"	color: rgb(69, 69, 69);\n"
"	border: 0px solid;\n"
"	border-radius: 5px;\n"
"	background-position: center;\n"
"	background-color: rgb(235, 240,243 );\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"	border: 2px solid  rgb(0, 120, 170);\n"
"	background-color: rgb(235, 240,243 );\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	color: rgb(69, 69, 69);\n"
"	background-color: rgb(217, 237, 247);\n"
"}")
        self.line_edit_output_file_split.setAlignment(Qt.AlignCenter)
        self.button_open_folder_split = QPushButton(self.frame_body_page_2)
        self.button_open_folder_split.setObjectName(u"button_open_folder_split")
        self.button_open_folder_split.setGeometry(QRect(550, 230, 81, 40))
        self.button_open_folder_split.setMinimumSize(QSize(40, 40))
        self.button_open_folder_split.setMaximumSize(QSize(100, 40))
        self.button_open_folder_split.setStyleSheet(u"QPushButton {\n"
"	color:  rgb(235, 240, 243);\n"
"	border: 0px solid;\n"
"	border-radius: 5px;\n"
"	background-position: center;\n"
"	background-color: rgb(0, 120, 170);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border: 2px solid  rgb(235, 240, 243);\n"
"	background-color: rgb(0, 130,180 );\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	color: rgb(69, 69, 69);\n"
"	background-color: rgb(217, 237, 247);\n"
"}")
        self.button_open_folder_split.setIcon(icon9)
        self.button_open_folder_split.setIconSize(QSize(40, 40))

        self.verticalLayout_2.addWidget(self.frame_body_page_2)


        self.verticalLayout_8.addWidget(self.frame_page2)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_4 = QVBoxLayout(self.page_3)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_top_page_3 = QFrame(self.page_3)
        self.frame_top_page_3.setObjectName(u"frame_top_page_3")
        self.frame_top_page_3.setMinimumSize(QSize(0, 100))
        self.frame_top_page_3.setMaximumSize(QSize(16777215, 150))
        self.frame_top_page_3.setFrameShape(QFrame.StyledPanel)
        self.frame_top_page_3.setFrameShadow(QFrame.Raised)
        self.label_ajustes = QLabel(self.frame_top_page_3)
        self.label_ajustes.setObjectName(u"label_ajustes")
        self.label_ajustes.setGeometry(QRect(10, 10, 331, 41))
        self.label_ajustes.setFont(font)
        self.label_ajustes.setStyleSheet(u"color: rgb(69, 69, 69);")

        self.verticalLayout_4.addWidget(self.frame_top_page_3)

        self.frame_body_page_3 = QFrame(self.page_3)
        self.frame_body_page_3.setObjectName(u"frame_body_page_3")
        self.frame_body_page_3.setFrameShape(QFrame.StyledPanel)
        self.frame_body_page_3.setFrameShadow(QFrame.Raised)
        self.textEdit = QTextEdit(self.frame_body_page_3)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(190, 40, 331, 341))
        self.textEdit.setStyleSheet(u"QTextEdit{\n"
"	border: 0px solid;\n"
"}")

        self.verticalLayout_4.addWidget(self.frame_body_page_3)

        self.stackedWidget.addWidget(self.page_3)
        self.frame_botton = QFrame(self.frame_pages)
        self.frame_botton.setObjectName(u"frame_botton")
        self.frame_botton.setGeometry(QRect(0, 570, 730, 30))
        self.frame_botton.setMinimumSize(QSize(550, 30))
        self.frame_botton.setMaximumSize(QSize(16777215, 30))
        self.frame_botton.setStyleSheet(u"background-color: rgb(217, 237, 247);")
        self.frame_botton.setFrameShape(QFrame.NoFrame)
        self.frame_botton.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_botton)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.frame_botton)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: rgb(69, 69, 69);")

        self.horizontalLayout.addWidget(self.label)

        self.label_4 = QLabel(self.frame_botton)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout.addWidget(self.label_4, 0, Qt.AlignRight)


        self.horizontalLayout_2.addWidget(self.frame_pages)


        self.verticalLayout.addWidget(self.content)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Conversor e Divisor", None))
        self.button_toggle.setText("")
        self.button_page_1.setText("")
        self.button_page_2.setText("")
        self.button_settings.setText("")
        self.label_convert_split.setText(QCoreApplication.translate("MainWindow", u"Conversor e Divisor", None))
        self.radio_button_normal.setText(QCoreApplication.translate("MainWindow", u"Normal", None))
        self.radio_button_low.setText(QCoreApplication.translate("MainWindow", u"Baixa", None))
        self.check_box_split.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o Dividir", None))
        self.button_start.setText("")
        self.button_output_file.setText(QCoreApplication.translate("MainWindow", u"Destino", None))
        self.button_source_file.setText(QCoreApplication.translate("MainWindow", u"Origem", None))
        self.button_stop.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
        self.button_open_folder.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
        self.label_split.setText(QCoreApplication.translate("MainWindow", u"Divisor", None))
        self.button_source_file_split.setText(QCoreApplication.translate("MainWindow", u"Origem", None))
        self.button_start_split.setText("")
        self.button_output_file_split.setText(QCoreApplication.translate("MainWindow", u"Destino", None))
        self.button_open_folder_split.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
        self.label_ajustes.setText(QCoreApplication.translate("MainWindow", u"Sobre", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-weight:600;\">Conversor &amp; Divisor</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2'; font-weight:600;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2';\">	Interface Grafica para convis\u00e3o e divis\u00e3o de v\u00ed"
                        "deos para inclus\u00e3o no PJe, utilizando as ferramentas FFMPEG e MP4Box.</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Desenvolvido por Haddly Trindade", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"V 1.0.0", None))
    # retranslateUi

