# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Loading.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TelaLoading(object):
    def setupUi(self, TelaLoading):
        TelaLoading.setObjectName("TelaLoading")
        TelaLoading.resize(296, 165)
        TelaLoading.setMaximumSize(QtCore.QSize(296, 165))
        self.centralwidget = QtWidgets.QWidget(TelaLoading)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background-color: #000000;\n"
"color: #EDEDED;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lblGIFLoading = QtWidgets.QLabel(self.frame)
        self.lblGIFLoading.setText("")
        self.lblGIFLoading.setPixmap(QtGui.QPixmap("loading_100px.gif"))
        self.lblGIFLoading.setAlignment(QtCore.Qt.AlignCenter)
        self.lblGIFLoading.setObjectName("lblGIFLoading")
        self.verticalLayout.addWidget(self.lblGIFLoading)
        self.lblMensagemLoading = QtWidgets.QLabel(self.frame)
        self.lblMensagemLoading.setAlignment(QtCore.Qt.AlignCenter)
        self.lblMensagemLoading.setObjectName("lblMensagemLoading")
        self.verticalLayout.addWidget(self.lblMensagemLoading)
        self.verticalLayout_2.addWidget(self.frame)
        TelaLoading.setCentralWidget(self.centralwidget)

        self.retranslateUi(TelaLoading)
        QtCore.QMetaObject.connectSlotsByName(TelaLoading)

    def retranslateUi(self, TelaLoading):
        _translate = QtCore.QCoreApplication.translate
        TelaLoading.setWindowTitle(_translate("TelaLoading", "Loading"))
        self.lblMensagemLoading.setText(_translate("TelaLoading", "<mensagem>"))
