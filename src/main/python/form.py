# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Github\health-weather_correlation\src\main\python\ui\form.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainBaseForm(object):
    def setupUi(self, MainBaseForm):
        MainBaseForm.setObjectName("MainBaseForm")
        MainBaseForm.resize(1003, 491)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainBaseForm.sizePolicy().hasHeightForWidth())
        MainBaseForm.setSizePolicy(sizePolicy)
        MainBaseForm.setMaximumSize(QtCore.QSize(16777215, 16777215))

        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ref_layout = QtWidgets.QGridLayout()
        self.ref_layout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.ref_layout.setHorizontalSpacing(6)
        self.ref_layout.setObjectName("ref_layout")
        self.std_list = QtWidgets.QListWidget(MainBaseForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.std_list.sizePolicy().hasHeightForWidth())
        self.std_list.setSizePolicy(sizePolicy)
        self.std_list.setMinimumSize(QtCore.QSize(150, 0))
        self.std_list.setMaximumSize(QtCore.QSize(150, 16777215))
        self.std_list.setBatchSize(150)
        self.std_list.setObjectName("std_list")
        self.ref_layout.addWidget(self.std_list, 1, 0, 1, 1)
        self.add_std_btn = QtWidgets.QPushButton(MainBaseForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_std_btn.sizePolicy().hasHeightForWidth())
        self.add_std_btn.setSizePolicy(sizePolicy)
        self.add_std_btn.setMaximumSize(QtCore.QSize(150, 16777215))
        self.add_std_btn.setObjectName("add_std_btn")
        self.ref_layout.addWidget(self.add_std_btn, 2, 0, 1, 1)
        self.del_std_btn = QtWidgets.QPushButton(MainBaseForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.del_std_btn.sizePolicy().hasHeightForWidth())
        self.del_std_btn.setSizePolicy(sizePolicy)
        self.del_std_btn.setMaximumSize(QtCore.QSize(150, 16777215))
        self.del_std_btn.setObjectName("del_std_btn")
        self.ref_layout.addWidget(self.del_std_btn, 3, 0, 1, 1)
        self.std_label = QtWidgets.QLabel(MainBaseForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.std_label.sizePolicy().hasHeightForWidth())
        self.std_label.setSizePolicy(sizePolicy)
        self.std_label.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.std_label.setFont(font)
        self.std_label.setAlignment(QtCore.Qt.AlignCenter)
        self.std_label.setObjectName("std_label")
        self.ref_layout.addWidget(self.std_label, 0, 0, 1, 1)
        self.horizontalLayout.addLayout(self.ref_layout)
        self.sample_layout = QtWidgets.QGridLayout()
        self.sample_layout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.sample_layout.setObjectName("sample_layout")
        self.del_sample_btn = QtWidgets.QPushButton(MainBaseForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.del_sample_btn.sizePolicy().hasHeightForWidth())
        self.del_sample_btn.setSizePolicy(sizePolicy)
        self.del_sample_btn.setMaximumSize(QtCore.QSize(150, 16777215))
        self.del_sample_btn.setObjectName("del_sample_btn")
        self.sample_layout.addWidget(self.del_sample_btn, 4, 0, 1, 1)
        self.sample_label = QtWidgets.QLabel(MainBaseForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sample_label.sizePolicy().hasHeightForWidth())
        self.sample_label.setSizePolicy(sizePolicy)
        self.sample_label.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.sample_label.setFont(font)
        self.sample_label.setAlignment(QtCore.Qt.AlignCenter)
        self.sample_label.setObjectName("sample_label")
        self.sample_layout.addWidget(self.sample_label, 1, 0, 1, 1)
        self.sample_list = QtWidgets.QListWidget(MainBaseForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sample_list.sizePolicy().hasHeightForWidth())
        self.sample_list.setSizePolicy(sizePolicy)
        self.sample_list.setMinimumSize(QtCore.QSize(150, 0))
        self.sample_list.setMaximumSize(QtCore.QSize(150, 16777215))
        self.sample_list.setBatchSize(150)
        self.sample_list.setObjectName("sample_list")
        self.sample_layout.addWidget(self.sample_list, 2, 0, 1, 1)
        self.add_sample_btn = QtWidgets.QPushButton(MainBaseForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_sample_btn.sizePolicy().hasHeightForWidth())
        self.add_sample_btn.setSizePolicy(sizePolicy)
        self.add_sample_btn.setMaximumSize(QtCore.QSize(150, 16777215))
        self.add_sample_btn.setObjectName("add_sample_btn")
        self.sample_layout.addWidget(self.add_sample_btn, 3, 0, 1, 1)
        self.horizontalLayout.addLayout(self.sample_layout)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.common_layout = QtWidgets.QHBoxLayout()
        self.common_layout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.common_layout.setObjectName("common_layout")
        self.lead_label = QtWidgets.QLabel(MainBaseForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lead_label.sizePolicy().hasHeightForWidth())
        self.lead_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lead_label.setFont(font)
        self.lead_label.setAlignment(QtCore.Qt.AlignCenter)
        self.lead_label.setObjectName("lead_label")
        self.common_layout.addWidget(self.lead_label)
        self.lead_box = QtWidgets.QComboBox(MainBaseForm)
        self.lead_box.setObjectName("lead_box")
        self.common_layout.addWidget(self.lead_box)
        self.slave_label = QtWidgets.QLabel(MainBaseForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.slave_label.sizePolicy().hasHeightForWidth())
        self.slave_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.slave_label.setFont(font)
        self.slave_label.setAlignment(QtCore.Qt.AlignCenter)
        self.slave_label.setObjectName("slave_label")
        self.common_layout.addWidget(self.slave_label)
        self.slave_box = QtWidgets.QComboBox(MainBaseForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.slave_box.sizePolicy().hasHeightForWidth())
        self.slave_box.setSizePolicy(sizePolicy)
        self.slave_box.setObjectName("slave_box")
        self.common_layout.addWidget(self.slave_box)
        self.factor_label = QtWidgets.QLabel(MainBaseForm)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.factor_label.setFont(font)
        self.factor_label.setAlignment(QtCore.Qt.AlignCenter)
        self.factor_label.setObjectName("factor_label")
        self.common_layout.addWidget(self.factor_label)
        self.factor_box = QtWidgets.QComboBox(MainBaseForm)
        self.factor_box.setObjectName("factor_box")
        self.common_layout.addWidget(self.factor_box)
        self.verticalLayout.addLayout(self.common_layout)
        self.data_layout = QtWidgets.QVBoxLayout()
        self.data_layout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.data_layout.setContentsMargins(0, -1, -1, -1)
        self.data_layout.setObjectName("data_layout")
        self.report_btn = QtWidgets.QPushButton(MainBaseForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.report_btn.sizePolicy().hasHeightForWidth())
        self.report_btn.setSizePolicy(sizePolicy)
        self.report_btn.setObjectName("report_btn")
        self.data_layout.addWidget(self.report_btn)
        self.verticalLayout.addLayout(self.data_layout)
        self.verticalLayout.setStretch(1, 1)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.horizontalLayout.setStretch(2, 1)

        self.retranslateUi(MainBaseForm)
        QtCore.QMetaObject.connectSlotsByName(MainBaseForm)

    def retranslateUi(self, MainBaseForm):
        _translate = QtCore.QCoreApplication.translate
        MainBaseForm.setWindowTitle(_translate("MainBaseForm", "Form"))
        self.add_std_btn.setText(_translate("MainBaseForm", "Добавить"))
        self.del_std_btn.setText(_translate("MainBaseForm", "Удалить"))
        self.std_label.setText(_translate("MainBaseForm", "Эталоны"))
        self.del_sample_btn.setText(_translate("MainBaseForm", "Удалить"))
        self.sample_label.setText(_translate("MainBaseForm", "Пациенты"))
        self.add_sample_btn.setText(_translate("MainBaseForm", "Добавить"))
        self.lead_label.setText(_translate("MainBaseForm", "Ведущий ряд"))
        self.slave_label.setText(_translate("MainBaseForm", "Ведомый ряд"))
        self.factor_label.setText(_translate("MainBaseForm", "Фактор"))
        self.report_btn.setText(_translate("MainBaseForm", "Сформировать отчёт"))

