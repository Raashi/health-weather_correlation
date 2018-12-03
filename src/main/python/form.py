# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src\main\python\ui\health_weather.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget

class Ui_MainBaseForm(object):
    def setupUi(self, MainBaseForm):
        MainBaseForm.setObjectName("MainBaseForm")
        MainBaseForm.resize(811, 578)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainBaseForm.sizePolicy().hasHeightForWidth())
        MainBaseForm.setSizePolicy(sizePolicy)
        MainBaseForm.setMinimumSize(QtCore.QSize(0, 0))
        MainBaseForm.setMaximumSize(QtCore.QSize(16777215, 16777215))

        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.tabWidget = QtWidgets.QTabWidget(MainBaseForm)
        self.tabWidget.setMinimumSize(QtCore.QSize(500, 500))
        self.tabWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.kde_tab = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.kde_tab.sizePolicy().hasHeightForWidth())
        self.kde_tab.setSizePolicy(sizePolicy)
        self.kde_tab.setMinimumSize(QtCore.QSize(300, 300))
        self.kde_tab.setObjectName("kde_tab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.kde_tab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.kde_layout = QtWidgets.QHBoxLayout()
        self.kde_layout.setObjectName("kde_layout")
        self.verticalLayout_2.addLayout(self.kde_layout)
        self.tabWidget.addTab(self.kde_tab, "")
        self.tests_tab = QtWidgets.QWidget()
        self.tests_tab.setObjectName("tests_tab")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tests_tab)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tests_layout = QtWidgets.QHBoxLayout()
        self.tests_layout.setObjectName("tests_layout")
        self.verticalLayout_3.addLayout(self.tests_layout)
        self.tabWidget.addTab(self.tests_tab, "")
        self.table_tab = QtWidgets.QWidget()
        self.table_tab.setObjectName("table_tab")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.table_tab)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.table_layout = QtWidgets.QHBoxLayout()
        self.table_layout.setObjectName("table_layout")
        self.verticalLayout_4.addLayout(self.table_layout)
        self.tabWidget.addTab(self.table_tab, "")
        self.verticalLayout_5.addWidget(self.tabWidget)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.gridLayout.setObjectName("gridLayout")
        self.standard_line = QtWidgets.QLineEdit(MainBaseForm)
        self.standard_line.setObjectName("standard_line")
        self.gridLayout.addWidget(self.standard_line, 0, 1, 1, 1)
        self.sample_line = QtWidgets.QLineEdit(MainBaseForm)
        self.sample_line.setObjectName("sample_line")
        self.gridLayout.addWidget(self.sample_line, 1, 1, 1, 1)
        self.sample_btn = QtWidgets.QPushButton(MainBaseForm)
        self.sample_btn.setObjectName("sample_btn")
        self.gridLayout.addWidget(self.sample_btn, 1, 0, 1, 1)
        self.standard_btn = QtWidgets.QPushButton(MainBaseForm)
        self.standard_btn.setObjectName("standard_btn")
        self.gridLayout.addWidget(self.standard_btn, 0, 0, 1, 1)
        self.start_btn = QtWidgets.QPushButton(MainBaseForm)
        self.start_btn.setObjectName("start_btn")
        self.gridLayout.addWidget(self.start_btn, 0, 2, 1, 1)
        self.exit_btn = QtWidgets.QPushButton(MainBaseForm)
        self.exit_btn.setObjectName("exit_btn")
        self.gridLayout.addWidget(self.exit_btn, 1, 2, 1, 1)
        self.verticalLayout_5.addLayout(self.gridLayout)
        self.verticalLayout.addLayout(self.verticalLayout_5)

        self.retranslateUi(MainBaseForm)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainBaseForm)

    def retranslateUi(self, MainBaseForm):
        _translate = QtCore.QCoreApplication.translate
        MainBaseForm.setWindowTitle(_translate("MainBaseForm", "Программа"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.kde_tab), _translate("MainBaseForm", "Совместный KDE"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tests_tab), _translate("MainBaseForm", "Тесты статистической нормальности"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.table_tab), _translate("MainBaseForm", "Сводная таблица результатов"))
        self.sample_btn.setText(_translate("MainBaseForm", "Выбрать образец"))
        self.standard_btn.setText(_translate("MainBaseForm", "Выбрать эталон"))
        self.start_btn.setText(_translate("MainBaseForm", "Запуск"))
        self.exit_btn.setText(_translate("MainBaseForm", "Выход"))
