# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_cd.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
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
        icon.addFile(u":/MainIcon/main_icone", QSize(), QIcon.Normal, QIcon.Off)
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
        self.frame_left_menu.setFrameShape(QFrame.NoFrame)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_top_menus = QFrame(self.frame_left_menu)
        self.frame_top_menus.setObjectName(u"frame_top_menus")
        self.frame_top_menus.setFrameShape(QFrame.NoFrame)
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
"}\n"
"QPushButton QToolTip {\n"
"	color: #454545;\n"
"	background-color: #d9edf7;\n"
"	border: 0px solid;\n"
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
"}\n"
"\n"
"QPushButton QToolTip {\n"
"	color: #454545;\n"
"	background-color: #d9edf7;\n"
"	border: 0px solid;\n"
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
"}\n"
"\n"
"QPushButton QToolTip {\n"
"	color: #454545;\n"
"	background-color: #d9edf7;\n"
"	border: 0px solid;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/menu_C/cil-view-module.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_page_2.setIcon(icon3)
        self.button_page_2.setIconSize(QSize(50, 40))

        self.layout_menu_top.addWidget(self.button_page_2, 0, Qt.AlignLeft)


        self.verticalLayout_3.addWidget(self.frame_top_menus, 0, Qt.AlignLeft|Qt.AlignTop)

        self.frame_botton_menus = QFrame(self.frame_left_menu)
        self.frame_botton_menus.setObjectName(u"frame_botton_menus")
        self.frame_botton_menus.setFrameShape(QFrame.NoFrame)
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
"}\n"
"\n"
"QPushButton QToolTip {\n"
"	color: #454545;\n"
"	background-color: #d9edf7;\n"
"	border: 0px solid;\n"
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
        self.frame_top_page.setFrameShape(QFrame.NoFrame)
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
        self.radio_button_normal.setGeometry(QRect(180, 110, 101, 21))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(14)
        self.radio_button_normal.setFont(font1)
        self.radio_button_normal.setStyleSheet(u"QRadioButton::indicator{\n"
"	color: rgb(69, 69, 69);\n"
"\n"
"}\n"
"\n"
"QRadioButton QToolTip {\n"
"	color: #454545;\n"
"	background-color: #d9edf7;\n"
"	border: 0px solid;\n"
"}")
        self.radio_button_normal.setChecked(False)
        self.radio_button_low = QRadioButton(self.frame_top_page)
        self.radio_button_low.setObjectName(u"radio_button_low")
        self.radio_button_low.setGeometry(QRect(30, 110, 131, 21))
        self.radio_button_low.setFont(font1)
        self.radio_button_low.setStyleSheet(u"QRadioButton::indicator{\n"
"	color: rgb(69, 69, 69);\n"
"}\n"
"\n"
"QRadioButton QToolTip {\n"
"	color: #454545;\n"
"	background-color: #d9edf7;\n"
"	border: 0px solid;\n"
"}")
        self.radio_button_low.setChecked(True)
        self.check_box_split = QCheckBox(self.frame_top_page)
        self.check_box_split.setObjectName(u"check_box_split")
        self.check_box_split.setGeometry(QRect(30, 76, 141, 21))
        self.check_box_split.setFont(font1)
        self.check_box_split.setStyleSheet(u"QCheckBox::indicator{\n"
"	color: rgb(69, 69, 69);\n"
"	\n"
"}\n"
"\n"
"QCheckBox QToolTip {\n"
"	color: #454545;\n"
"	background-color: #d9edf7;\n"
"	border: 0px solid;\n"
"}")
        self.check_box_split.setChecked(False)

        self.vboxLayout.addWidget(self.frame_top_page)

        self.frame = QFrame(self.page_1)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.button_output_file = QPushButton(self.frame)
        self.button_output_file.setObjectName(u"button_output_file")
        self.button_output_file.setGeometry(QRect(550, 70, 100, 100))
        self.button_output_file.setMinimumSize(QSize(70, 70))
        self.button_output_file.setMaximumSize(QSize(100, 100))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setWeight(75)
        self.button_output_file.setFont(font2)
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
"}\n"
"\n"
"QPushButton QToolTip {\n"
"	color: #454545;\n"
"	background-color: #d9edf7;\n"
"	border: 0px solid;\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/button_output_file/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_output_file.setIcon(icon5)
        self.button_output_file.setIconSize(QSize(100, 100))
        self.button_source_file = QPushButton(self.frame)
        self.button_source_file.setObjectName(u"button_source_file")
        self.button_source_file.setGeometry(QRect(70, 70, 100, 100))
        self.button_source_file.setMinimumSize(QSize(70, 70))
        self.button_source_file.setMaximumSize(QSize(100, 100))
        self.button_source_file.setFont(font2)
        self.button_source_file.setToolTipDuration(-1)
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
"}\n"
"\n"
"QPushButton QToolTip {\n"
"	color: #454545;\n"
"	background-color: #d9edf7;\n"
"	border: 0px solid;\n"
"}\n"
"\n"
"QPushButton QToolTip {\n"
"	color: #454545;\n"
"	background-color: #d9edf7;\n"
"	border: 0px solid;\n"
"}\n"
"\n"
"")
        icon6 = QIcon()
        icon6.addFile(u":/button_search_file/cil-movie.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_source_file.setIcon(icon6)
        self.button_source_file.setIconSize(QSize(100, 100))
        self.button_stop = QPushButton(self.frame)
        self.button_stop.setObjectName(u"button_stop")
        self.button_stop.setGeometry(QRect(270, 250, 200, 40))
        self.button_stop.setMinimumSize(QSize(200, 40))
        self.button_stop.setMaximumSize(QSize(200, 40))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(12)
        font3.setBold(True)
        font3.setWeight(75)
        self.button_stop.setFont(font3)
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
"}\n"
"\n"
"QPushButton QToolTip {\n"
"	color: #454545;\n"
"	background-color: #d9edf7;\n"
"	border: 0px solid;\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/button_stop/cil-media-stop.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_stop.setIcon(icon7)
        self.button_stop.setIconSize(QSize(40, 50))
        self.button_open_folder = QPushButton(self.frame)
        self.button_open_folder.setObjectName(u"button_open_folder")
        self.button_open_folder.setGeometry(QRect(560, 250, 81, 40))
        self.button_open_folder.setMinimumSize(QSize(40, 40))
        self.button_open_folder.setMaximumSize(QSize(100, 100))
        self.button_open_folder.setFont(font2)
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
"}\n"
"\n"
"QPushButton QToolTip {\n"
"	color: #454545;\n"
"	background-color: #d9edf7;\n"
"	border: 0px solid;\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u":/open_folder/cil-folder.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_open_folder.setIcon(icon8)
        self.button_open_folder.setIconSize(QSize(40, 40))
        self.button_start = QPushButton(self.frame)
        self.button_start.setObjectName(u"button_start")
        self.button_start.setGeometry(QRect(310, 70, 100, 100))
        self.button_start.setMinimumSize(QSize(70, 70))
        self.button_start.setMaximumSize(QSize(100, 100))
        self.button_start.setFont(font2)
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
"}\n"
"\n"
"QPushButton QToolTip {\n"
"	color: #454545;\n"
"	background-color: #d9edf7;\n"
"	border: 0px solid;\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u":/button_start/cil-media-play.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_start.setIcon(icon9)
        self.button_start.setIconSize(QSize(200, 200))
        self.line_edit_output_file = QLineEdit(self.frame)
        self.line_edit_output_file.setObjectName(u"line_edit_output_file")
        self.line_edit_output_file.setGeometry(QRect(494, 190, 231, 35))
        self.line_edit_output_file.setMaximumSize(QSize(240, 35))
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
        self.progress_bar = QProgressBar(self.frame)
        self.progress_bar.setObjectName(u"progress_bar")
        self.progress_bar.setGeometry(QRect(250, 190, 240, 35))
        self.progress_bar.setMaximumSize(QSize(240, 35))
        self.progress_bar.setStyleSheet(u"QProgressBar {\n"
"	color:  rgb(69, 69,69);\n"
"	border: 0px solid;\n"
"	border-radius: 5px;\n"
"	border-style: none;\n"
"	background-position: center;\n"
"	text-align: center;\n"
"	background-color: rgb(217, 237,247);\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"	background-color: rgb(0, 120, 170);\n"
"	border-radius: 5px;\n"
"}\n"
"")
        self.progress_bar.setValue(0)
        self.line_edit_input_file = QLineEdit(self.frame)
        self.line_edit_input_file.setObjectName(u"line_edit_input_file")
        self.line_edit_input_file.setGeometry(QRect(5, 190, 240, 35))
        self.line_edit_input_file.setMaximumSize(QSize(240, 35))
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
        self.frame_page2.setFrameShape(QFrame.NoFrame)
        self.frame_page2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_page2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_top_page_2 = QFrame(self.frame_page2)
        self.frame_top_page_2.setObjectName(u"frame_top_page_2")
        self.frame_top_page_2.setMinimumSize(QSize(0, 100))
        self.frame_top_page_2.setMaximumSize(QSize(16777215, 150))
        self.frame_top_page_2.setFrameShape(QFrame.NoFrame)
        self.frame_top_page_2.setFrameShadow(QFrame.Raised)
        self.label_split = QLabel(self.frame_top_page_2)
        self.label_split.setObjectName(u"label_split")
        self.label_split.setGeometry(QRect(10, 10, 331, 41))
        self.label_split.setFont(font)
        self.label_split.setStyleSheet(u"color: rgb(69, 69, 69);")
        self.label_2 = QLabel(self.frame_top_page_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 110, 711, 20))
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        font4.setPointSize(8)
        font4.setBold(True)
        font4.setWeight(75)
        self.label_2.setFont(font4)
        self.label_2.setStyleSheet(u"color: rgb(69, 69, 69);")

        self.verticalLayout_2.addWidget(self.frame_top_page_2)

        self.frame_body_page_2 = QFrame(self.frame_page2)
        self.frame_body_page_2.setObjectName(u"frame_body_page_2")
        self.frame_body_page_2.setFrameShape(QFrame.NoFrame)
        self.frame_body_page_2.setFrameShadow(QFrame.Raised)
        self.button_source_file_split = QPushButton(self.frame_body_page_2)
        self.button_source_file_split.setObjectName(u"button_source_file_split")
        self.button_source_file_split.setGeometry(QRect(70, 70, 100, 100))
        self.button_source_file_split.setMinimumSize(QSize(70, 70))
        self.button_source_file_split.setMaximumSize(QSize(100, 100))
        self.button_source_file_split.setFont(font2)
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
"}\n"
"\n"
"QPushButton QToolTip {\n"
"	color: #454545;\n"
"	background-color: #d9edf7;\n"
"	border: 0px solid;\n"
"}")
        self.button_source_file_split.setIcon(icon6)
        self.button_source_file_split.setIconSize(QSize(100, 100))
        self.line_edit_input_file_split = QLineEdit(self.frame_body_page_2)
        self.line_edit_input_file_split.setObjectName(u"line_edit_input_file_split")
        self.line_edit_input_file_split.setGeometry(QRect(2, 190, 240, 35))
        self.line_edit_input_file_split.setMinimumSize(QSize(240, 35))
        self.line_edit_input_file_split.setMaximumSize(QSize(240, 35))
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
        self.button_start_split.setFont(font2)
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
"}\n"
"\n"
"QPushButton QToolTip {\n"
"	color: #454545;\n"
"	background-color: #d9edf7;\n"
"	border: 0px solid;\n"
"}")
        self.button_start_split.setIcon(icon9)
        self.button_start_split.setIconSize(QSize(100, 100))
        self.button_output_file_split = QPushButton(self.frame_body_page_2)
        self.button_output_file_split.setObjectName(u"button_output_file_split")
        self.button_output_file_split.setGeometry(QRect(550, 70, 100, 100))
        self.button_output_file_split.setMinimumSize(QSize(70, 70))
        self.button_output_file_split.setMaximumSize(QSize(100, 100))
        self.button_output_file_split.setFont(font2)
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
"}\n"
"\n"
"QPushButton QToolTip {\n"
"	color: #454545;\n"
"	background-color: #d9edf7;\n"
"	border: 0px solid;\n"
"}")
        self.button_output_file_split.setIcon(icon5)
        self.button_output_file_split.setIconSize(QSize(100, 100))
        self.line_edit_output_file_split = QLineEdit(self.frame_body_page_2)
        self.line_edit_output_file_split.setObjectName(u"line_edit_output_file_split")
        self.line_edit_output_file_split.setGeometry(QRect(486, 190, 240, 35))
        self.line_edit_output_file_split.setMinimumSize(QSize(240, 35))
        self.line_edit_output_file_split.setMaximumSize(QSize(240, 35))
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
        self.button_open_folder_split.setGeometry(QRect(560, 250, 81, 40))
        self.button_open_folder_split.setMinimumSize(QSize(40, 40))
        self.button_open_folder_split.setMaximumSize(QSize(100, 40))
        self.button_open_folder_split.setFont(font2)
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
"}\n"
"\n"
"QPushButton QToolTip {\n"
"	color: #454545;\n"
"	background-color: #d9edf7;\n"
"	border: 0px solid;\n"
"}")
        self.button_open_folder_split.setIcon(icon8)
        self.button_open_folder_split.setIconSize(QSize(40, 40))
        self.progress_bar_split = QProgressBar(self.frame_body_page_2)
        self.progress_bar_split.setObjectName(u"progress_bar_split")
        self.progress_bar_split.setGeometry(QRect(244, 190, 240, 35))
        self.progress_bar_split.setMaximumSize(QSize(240, 35))
        self.progress_bar_split.setStyleSheet(u"QProgressBar {\n"
"	color:  rgb(65, 65,65);\n"
"	border: 0px solid;\n"
"	border-radius: 5px;\n"
"	border-style: none;\n"
"	background-position: center;\n"
"	text-align: center;\n"
"	background-color: rgb(217, 237,247);\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"	background-color: rgb(0, 120, 170);\n"
"	border-radius: 5px;\n"
"}\n"
"")
        self.progress_bar_split.setValue(0)
        self.button_stop_split = QPushButton(self.frame_body_page_2)
        self.button_stop_split.setObjectName(u"button_stop_split")
        self.button_stop_split.setGeometry(QRect(265, 250, 200, 40))
        self.button_stop_split.setMinimumSize(QSize(200, 40))
        self.button_stop_split.setMaximumSize(QSize(200, 40))
        self.button_stop_split.setFont(font3)
        self.button_stop_split.setStyleSheet(u"QPushButton {\n"
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
"}\n"
"\n"
"QPushButton QToolTip {\n"
"	color: #454545;\n"
"	background-color: #d9edf7;\n"
"	border: 0px solid;\n"
"}")
        self.button_stop_split.setIcon(icon7)
        self.button_stop_split.setIconSize(QSize(40, 50))

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
        self.frame_top_page_3.setFrameShape(QFrame.NoFrame)
        self.frame_top_page_3.setFrameShadow(QFrame.Raised)
        self.label_about = QLabel(self.frame_top_page_3)
        self.label_about.setObjectName(u"label_about")
        self.label_about.setGeometry(QRect(10, 10, 101, 41))
        self.label_about.setFont(font)
        self.label_about.setStyleSheet(u"color: rgb(69, 69, 69);")
        self.textEdit = QTextEdit(self.frame_top_page_3)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(180, 20, 331, 121))
        self.textEdit.setStyleSheet(u"QTextEdit{\n"
"	border: 0px solid;\n"
"}")
        self.textEdit.setFrameShape(QFrame.NoFrame)

        self.verticalLayout_4.addWidget(self.frame_top_page_3)

        self.frame_body_page_3 = QFrame(self.page_3)
        self.frame_body_page_3.setObjectName(u"frame_body_page_3")
        self.frame_body_page_3.setFrameShape(QFrame.NoFrame)
        self.frame_body_page_3.setFrameShadow(QFrame.Raised)
        self.label_config = QLabel(self.frame_body_page_3)
        self.label_config.setObjectName(u"label_config")
        self.label_config.setGeometry(QRect(20, 20, 231, 41))
        self.label_config.setFont(font)
        self.label_config.setStyleSheet(u"color: rgb(69, 69, 69);")
        self.label_split_size = QLabel(self.frame_body_page_3)
        self.label_split_size.setObjectName(u"label_split_size")
        self.label_split_size.setGeometry(QRect(40, 150, 131, 31))
        self.label_split_size.setFont(font2)
        self.label_split_size.setStyleSheet(u"color: rgb(69, 69, 69);")
        self.spinBox_split_size = QSpinBox(self.frame_body_page_3)
        self.spinBox_split_size.setObjectName(u"spinBox_split_size")
        self.spinBox_split_size.setGeometry(QRect(180, 145, 71, 41))
        self.spinBox_split_size.setFont(font2)
        self.spinBox_split_size.setStyleSheet(u"QSpinBox {\n"
"	color: rgb(69, 69, 69);\n"
"	border: 0px solid;\n"
"	border-radius: 5px;\n"
"	background-position: center;\n"
"	background-color: rgb(255, 255,255 );\n"
"}\n"
"\n"
"QSpinBox:hover {\n"
"	border: 2px solid  rgb(0, 120, 170);\n"
"	background-color: rgb(255, 255,255 );\n"
"}\n"
"\n"
"QSpinBox:focus {\n"
"	color: rgb(69, 69, 69);\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.spinBox_split_size.setMaximum(1000)
        self.spinBox_split_size.setValue(30)
        self.label_confi_split = QLabel(self.frame_body_page_3)
        self.label_confi_split.setObjectName(u"label_confi_split")
        self.label_confi_split.setGeometry(QRect(40, 90, 101, 31))
        self.label_confi_split.setFont(font2)
        self.label_confi_split.setStyleSheet(u"color: rgb(69, 69, 69);")
        self.label_confi_convert = QLabel(self.frame_body_page_3)
        self.label_confi_convert.setObjectName(u"label_confi_convert")
        self.label_confi_convert.setGeometry(QRect(410, 90, 101, 31))
        self.label_confi_convert.setFont(font2)
        self.label_confi_convert.setStyleSheet(u"color: rgb(69, 69, 69);")
        self.pushButton_apply_settings = QPushButton(self.frame_body_page_3)
        self.pushButton_apply_settings.setObjectName(u"pushButton_apply_settings")
        self.pushButton_apply_settings.setGeometry(QRect(324, 370, 81, 41))
        self.pushButton_apply_settings.setFont(font2)
        self.pushButton_apply_settings.setStyleSheet(u"QPushButton {\n"
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
"}\n"
"\n"
"QPushButton QToolTip {\n"
"	color: #454545;\n"
"	background-color: #d9edf7;\n"
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
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_author = QLabel(self.frame_botton)
        self.label_author.setObjectName(u"label_author")
        font5 = QFont()
        font5.setFamily(u"Segoe UI")
        font5.setPointSize(10)
        self.label_author.setFont(font5)
        self.label_author.setStyleSheet(u"color: rgb(69, 69, 69);")

        self.horizontalLayout.addWidget(self.label_author)

        self.label_version = QLabel(self.frame_botton)
        self.label_version.setObjectName(u"label_version")
        font6 = QFont()
        font6.setFamily(u"Segoe UI")
        font6.setPointSize(10)
        font6.setBold(False)
        font6.setWeight(50)
        self.label_version.setFont(font6)

        self.horizontalLayout.addWidget(self.label_version, 0, Qt.AlignRight)


        self.horizontalLayout_2.addWidget(self.frame_pages)


        self.verticalLayout.addWidget(self.content)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Conversor e Divisor", None))
#if QT_CONFIG(tooltip)
        self.button_toggle.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Menu</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.button_toggle.setText("")
#if QT_CONFIG(tooltip)
        self.button_page_1.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Converter e Dividir Arquivos de V\u00eddeo</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.button_page_1.setText("")
#if QT_CONFIG(tooltip)
        self.button_page_2.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Dividir Arquivos de V\u00eddeo</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.button_page_2.setText("")
#if QT_CONFIG(tooltip)
        self.button_settings.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Sobre o Aplicativo</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.button_settings.setText("")
        self.label_convert_split.setText(QCoreApplication.translate("MainWindow", u"Conversor e Divisor", None))
#if QT_CONFIG(tooltip)
        self.radio_button_normal.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Qualidade Normal: o v\u00eddeo mant\u00e9m todas suas caracteristicas originais.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.radio_button_normal.setText(QCoreApplication.translate("MainWindow", u"Normal", None))
#if QT_CONFIG(tooltip)
        self.radio_button_low.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Qualidade Baixa: o v\u00eddeo perde qualidade, mas a convers\u00e3o e/ou divis\u00e3o \u00e9 mais r\u00e1pida.</span></p><p><span style=\" font-size:10pt; font-weight:600;\">Resolu\u00e7\u00e3o: 320x240</span></p><p><span style=\" font-size:10pt; font-weight:600;\">Codec: mpeg4</span></p><p><span style=\" font-size:10pt; font-weight:600;\">FPS: 30</span></p><p><span style=\" font-size:10pt; font-weight:600;\">Bitrate: 100 kbps </span></p><p><span style=\" font-size:10pt; font-weight:600;\">\u00c1udio mono de 48 kbps / 44 KHz</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.radio_button_low.setText(QCoreApplication.translate("MainWindow", u"Compactar", None))
#if QT_CONFIG(tooltip)
        self.check_box_split.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">N\u00e3o dividir, somente converte o v\u00eddeo.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.check_box_split.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o Dividir", None))
#if QT_CONFIG(tooltip)
        self.button_output_file.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Local de destino do V\u00eddeo convertido e/ou dividido.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.button_output_file.setText(QCoreApplication.translate("MainWindow", u"Destino", None))
#if QT_CONFIG(tooltip)
        self.button_source_file.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#454545;\">Procurar 1(um) ou v\u00e1rios v\u00eddeos.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.button_source_file.setText(QCoreApplication.translate("MainWindow", u"Origem", None))
#if QT_CONFIG(tooltip)
        self.button_stop.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Cancelar Processo.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.button_stop.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
#if QT_CONFIG(tooltip)
        self.button_open_folder.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Abrir Local do v\u00eddeo convertido e/ou dividido.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.button_open_folder.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
#if QT_CONFIG(tooltip)
        self.button_start.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Iniciar Processo.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.button_start.setText(QCoreApplication.translate("MainWindow", u"Iniciar", None))
        self.label_split.setText(QCoreApplication.translate("MainWindow", u"Divisor", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Divis\u00e3o dispon\u00edvel somente para v\u00eddeos .MP4, para outros formatos/extens\u00f5es use o menu Conversor e Divisor", None))
#if QT_CONFIG(tooltip)
        self.button_source_file_split.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Procurar v\u00eddeo para dividir</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.button_source_file_split.setText(QCoreApplication.translate("MainWindow", u"Origem", None))
#if QT_CONFIG(tooltip)
        self.button_start_split.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Iniciar Processo.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.button_start_split.setText(QCoreApplication.translate("MainWindow", u"Iniciar", None))
#if QT_CONFIG(tooltip)
        self.button_output_file_split.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Local de Destino do V\u00eddeo</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.button_output_file_split.setText(QCoreApplication.translate("MainWindow", u"Destino", None))
#if QT_CONFIG(tooltip)
        self.button_open_folder_split.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Abrir local do v\u00eddeo dividido.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.button_open_folder_split.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
#if QT_CONFIG(tooltip)
        self.button_stop_split.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Cancelar Divis\u00e3o.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.button_stop_split.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
        self.label_about.setText(QCoreApplication.translate("MainWindow", u"Sobre", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-weight:600;\">Conversor &amp; Divisor</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2'; font-weight:600;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2';\">	Interface Grafica para convers\u00e3o e divis\u00e3o de v\u00ed"
                        "deos para inclus\u00e3o no PJe, utilizando as ferramentas FFMPEG e MP4Box.</span></p></body></html>", None))
        self.label_config.setText(QCoreApplication.translate("MainWindow", u"Configura\u00e7\u00f5es", None))
        self.label_split_size.setText(QCoreApplication.translate("MainWindow", u"Dividir em (MB)", None))
        self.label_confi_split.setText(QCoreApplication.translate("MainWindow", u"Divisor", None))
        self.label_confi_convert.setText(QCoreApplication.translate("MainWindow", u"Conversor", None))
        self.pushButton_apply_settings.setText(QCoreApplication.translate("MainWindow", u"Aplicar", None))
        self.label_author.setText(QCoreApplication.translate("MainWindow", u"  Desenvolvido por Ivo H. Trindade", None))
        self.label_version.setText(QCoreApplication.translate("MainWindow", u"v1.2.0  ", None))
    # retranslateUi

