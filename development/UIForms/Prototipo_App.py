# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Prototipo_App.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NomeApp(object):
    def setupUi(self, NomeApp):
        NomeApp.setObjectName("NomeApp")
        NomeApp.resize(773, 600)
        self.centralwidget = QtWidgets.QWidget(NomeApp)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.stckPrincipal = QtWidgets.QStackedWidget(self.centralwidget)
        self.stckPrincipal.setStyleSheet("background-color: white;\n"
"color: black;")
        self.stckPrincipal.setObjectName("stckPrincipal")
        self.pgInicial = QtWidgets.QWidget()
        self.pgInicial.setObjectName("pgInicial")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.pgInicial)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frmPgInicial = QtWidgets.QFrame(self.pgInicial)
        self.frmPgInicial.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frmPgInicial.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frmPgInicial.setObjectName("frmPgInicial")
        self.lblNomeApp = QtWidgets.QLabel(self.frmPgInicial)
        self.lblNomeApp.setGeometry(QtCore.QRect(360, 90, 81, 31))
        self.lblNomeApp.setObjectName("lblNomeApp")
        self.btnIniciar = QtWidgets.QPushButton(self.frmPgInicial)
        self.btnIniciar.setGeometry(QtCore.QRect(350, 320, 90, 28))
        self.btnIniciar.setObjectName("btnIniciar")
        self.verticalLayout_2.addWidget(self.frmPgInicial)
        self.stckPrincipal.addWidget(self.pgInicial)
        self.pgUpload = QtWidgets.QWidget()
        self.pgUpload.setObjectName("pgUpload")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.pgUpload)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frmUpload = QtWidgets.QFrame(self.pgUpload)
        self.frmUpload.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frmUpload.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frmUpload.setObjectName("frmUpload")
        self.frmImg = QtWidgets.QFrame(self.frmUpload)
        self.frmImg.setGeometry(QtCore.QRect(30, 30, 351, 271))
        self.frmImg.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frmImg.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frmImg.setObjectName("frmImg")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frmImg)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.btnPreviaImg = QtWidgets.QPushButton(self.frmImg)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnPreviaImg.sizePolicy().hasHeightForWidth())
        self.btnPreviaImg.setSizePolicy(sizePolicy)
        self.btnPreviaImg.setText("")
        self.btnPreviaImg.setObjectName("btnPreviaImg")
        self.verticalLayout_3.addWidget(self.btnPreviaImg)
        self.btn2x = QtWidgets.QPushButton(self.frmUpload)
        self.btn2x.setGeometry(QtCore.QRect(250, 370, 61, 51))
        self.btn2x.setObjectName("btn2x")
        self.btn4x = QtWidgets.QPushButton(self.frmUpload)
        self.btn4x.setGeometry(QtCore.QRect(350, 370, 61, 51))
        self.btn4x.setObjectName("btn4x")
        self.btn8x = QtWidgets.QPushButton(self.frmUpload)
        self.btn8x.setGeometry(QtCore.QRect(450, 370, 61, 51))
        self.btn8x.setObjectName("btn8x")
        self.lblNomeImg = QtWidgets.QLabel(self.frmUpload)
        self.lblNomeImg.setGeometry(QtCore.QRect(470, 40, 201, 31))
        self.lblNomeImg.setObjectName("lblNomeImg")
        self.lblResolucaoImg = QtWidgets.QLabel(self.frmUpload)
        self.lblResolucaoImg.setGeometry(QtCore.QRect(470, 70, 201, 41))
        self.lblResolucaoImg.setObjectName("lblResolucaoImg")
        self.lblPPIImagem = QtWidgets.QLabel(self.frmUpload)
        self.lblPPIImagem.setGeometry(QtCore.QRect(470, 100, 201, 51))
        self.lblPPIImagem.setObjectName("lblPPIImagem")
        self.btnProcessaImg = QtWidgets.QPushButton(self.frmUpload)
        self.btnProcessaImg.setGeometry(QtCore.QRect(280, 480, 191, 51))
        self.btnProcessaImg.setObjectName("btnProcessaImg")
        self.cmbTamanhoImpressao = QtWidgets.QComboBox(self.frmUpload)
        self.cmbTamanhoImpressao.setGeometry(QtCore.QRect(470, 260, 201, 41))
        self.cmbTamanhoImpressao.setObjectName("cmbTamanhoImpressao")
        self.btnPadraoPapel = QtWidgets.QPushButton(self.frmUpload)
        self.btnPadraoPapel.setGeometry(QtCore.QRect(470, 210, 91, 41))
        self.btnPadraoPapel.setObjectName("btnPadraoPapel")
        self.btnPadraoFoto = QtWidgets.QPushButton(self.frmUpload)
        self.btnPadraoFoto.setGeometry(QtCore.QRect(580, 210, 91, 41))
        self.btnPadraoFoto.setObjectName("btnPadraoFoto")
        self.lblTIpoTamanhoImpressao = QtWidgets.QLabel(self.frmUpload)
        self.lblTIpoTamanhoImpressao.setGeometry(QtCore.QRect(470, 170, 201, 41))
        self.lblTIpoTamanhoImpressao.setObjectName("lblTIpoTamanhoImpressao")
        self.verticalLayout.addWidget(self.frmUpload)
        self.stckPrincipal.addWidget(self.pgUpload)
        self.pgDecisao = QtWidgets.QWidget()
        self.pgDecisao.setObjectName("pgDecisao")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.pgDecisao)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frmDecisao = QtWidgets.QFrame(self.pgDecisao)
        self.frmDecisao.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frmDecisao.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frmDecisao.setObjectName("frmDecisao")
        self.frmImgProcessada = QtWidgets.QFrame(self.frmDecisao)
        self.frmImgProcessada.setGeometry(QtCore.QRect(30, 30, 341, 241))
        self.frmImgProcessada.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frmImgProcessada.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frmImgProcessada.setObjectName("frmImgProcessada")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frmImgProcessada)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.btnPreviaImgProcessada = QtWidgets.QPushButton(self.frmImgProcessada)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnPreviaImgProcessada.sizePolicy().hasHeightForWidth())
        self.btnPreviaImgProcessada.setSizePolicy(sizePolicy)
        self.btnPreviaImgProcessada.setText("")
        self.btnPreviaImgProcessada.setObjectName("btnPreviaImgProcessada")
        self.verticalLayout_5.addWidget(self.btnPreviaImgProcessada)
        self.tblEspecificacoes = QtWidgets.QTableView(self.frmDecisao)
        self.tblEspecificacoes.setGeometry(QtCore.QRect(435, 30, 281, 241))
        self.tblEspecificacoes.setObjectName("tblEspecificacoes")
        self.btnReprocessar = QtWidgets.QPushButton(self.frmDecisao)
        self.btnReprocessar.setGeometry(QtCore.QRect(230, 480, 101, 31))
        self.btnReprocessar.setObjectName("btnReprocessar")
        self.btnSalvar = QtWidgets.QPushButton(self.frmDecisao)
        self.btnSalvar.setGeometry(QtCore.QRect(430, 480, 90, 28))
        self.btnSalvar.setObjectName("btnSalvar")
        self.btnPreviaProcessada = QtWidgets.QPushButton(self.frmDecisao)
        self.btnPreviaProcessada.setGeometry(QtCore.QRect(150, 290, 90, 28))
        self.btnPreviaProcessada.setObjectName("btnPreviaProcessada")
        self.verticalLayout_4.addWidget(self.frmDecisao)
        self.stckPrincipal.addWidget(self.pgDecisao)
        self.horizontalLayout.addWidget(self.stckPrincipal)
        NomeApp.setCentralWidget(self.centralwidget)

        self.retranslateUi(NomeApp)
        self.stckPrincipal.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(NomeApp)

    def retranslateUi(self, NomeApp):
        _translate = QtCore.QCoreApplication.translate
        NomeApp.setWindowTitle(_translate("NomeApp", "NomeApp"))
        self.lblNomeApp.setText(_translate("NomeApp", "<Nome APP>"))
        self.btnIniciar.setText(_translate("NomeApp", "INICIAR"))
        self.btn2x.setText(_translate("NomeApp", "x2"))
        self.btn4x.setText(_translate("NomeApp", "x4"))
        self.btn8x.setText(_translate("NomeApp", "x8"))
        self.lblNomeImg.setText(_translate("NomeApp", "<Nome IMG>"))
        self.lblResolucaoImg.setText(_translate("NomeApp", "<Resolução (512x512 px)>"))
        self.lblPPIImagem.setText(_translate("NomeApp", "<Numero PPI>"))
        self.btnProcessaImg.setText(_translate("NomeApp", "PROCESSAR"))
        self.btnPadraoPapel.setText(_translate("NomeApp", "Papel"))
        self.btnPadraoFoto.setText(_translate("NomeApp", "Foto"))
        self.lblTIpoTamanhoImpressao.setText(_translate("NomeApp", "Padrão de Tamanho de Impressão"))
        self.btnReprocessar.setText(_translate("NomeApp", "Reprocessar"))
        self.btnSalvar.setText(_translate("NomeApp", "Salvar"))
        self.btnPreviaProcessada.setText(_translate("NomeApp", "Abrir Prévia"))