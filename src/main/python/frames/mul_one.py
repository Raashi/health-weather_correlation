# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/main/python/ui/mul_one.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

# TODO: убрать этот модуль к чертям
class Ui_FrameMulOne(object):
    def setupUi(self, FrameMulOne):
        FrameMulOne.setObjectName("FrameMulOne")
        FrameMulOne.resize(725, 498)
        self.horizontalLayout = QtWidgets.QHBoxLayout(FrameMulOne)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.layout_vertical = QtWidgets.QVBoxLayout()
        self.layout_vertical.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.layout_vertical.setObjectName("layout_vertical")
        self.horizontalLayout.addLayout(self.layout_vertical)

        self.retranslateUi(FrameMulOne)
        QtCore.QMetaObject.connectSlotsByName(FrameMulOne)

    def retranslateUi(self, FrameMulOne):
        _translate = QtCore.QCoreApplication.translate
        FrameMulOne.setWindowTitle(_translate("FrameMulOne", "Frame"))

