# coding: utf-8
#
#   forms.py
#   Objetivo:       Agrupar classes que representam a visualização do aplicativo.
#   Autores:        Caroline, Daniel, Leonardo e Paloma
#   Contato:        tcc.ccp48@gmail.com
#   Data:           15/09/2021


# Imports necessários
from models.model import *
from utils.utils import *
from functools import partial
from PyQt5 import QtCore, QtGui, QtWidgets


class FormApp(QtWidgets.QMainWindow):

    def __init__(self, controller) -> None:
        """
        Método construtor da classe FormApp.
        """
        super(FormApp, self).__init__()
        self.controller = controller

        # Adicionando a fonte na aplicação
        QtGui.QFontDatabase.addApplicationFont(
            CAMINHO_OFFSIDE
        )

        # Inicializando atributos da classe
        self._declaraEstilos()
        self.setStyleSheet("font-family: Offside;")
        self.setupUi(self)
        self._delegaAcoes()


    def setupUi(self, App_IVision):
        App_IVision.setObjectName("App_IVision")
        App_IVision.resize(823, 600)
        self.centralwidget = QtWidgets.QWidget(App_IVision)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.stckPrincipal = QtWidgets.QStackedWidget(self.centralwidget)
        self.stckPrincipal.setStyleSheet(self._estilo_frm_principal)
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
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frmPgInicial)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frmAuxPgInicialEsq = QtWidgets.QFrame(self.frmPgInicial)
        self.frmAuxPgInicialEsq.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frmAuxPgInicialEsq.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frmAuxPgInicialEsq.setObjectName("frmAuxPgInicialEsq")
        self.horizontalLayout_2.addWidget(self.frmAuxPgInicialEsq)
        self.frmIconeTitulo = QtWidgets.QFrame(self.frmPgInicial)
        self.frmIconeTitulo.setMaximumSize(QtCore.QSize(256, 16777215))
        self.frmIconeTitulo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frmIconeTitulo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frmIconeTitulo.setObjectName("frmIconeTitulo")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frmIconeTitulo)
        self.verticalLayout_6.setContentsMargins(-1, 50, -1, 50)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.btnIcone = QtWidgets.QPushButton(self.frmIconeTitulo)
        self.btnIcone.setStyleSheet("border: none;")
        self.btnIcone.setText("")
        icon = QtGui.QIcon()

        icon.addPixmap(
                QtGui.QPixmap(CAMINHO_LOGO), 
                QtGui.QIcon.Normal, 
                QtGui.QIcon.Off
        )
        
        self.btnIcone.setIcon(icon)
        self.btnIcone.setIconSize(QtCore.QSize(150, 150))
        self.btnIcone.setObjectName("btnIcone")
        self.verticalLayout_6.addWidget(self.btnIcone)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem)
        self.lblBemVindo = QtWidgets.QLabel(self.frmIconeTitulo)
        self.lblBemVindo.setAlignment(QtCore.Qt.AlignCenter)
        self.lblBemVindo.setObjectName("lblBemVindo")
        self.verticalLayout_6.addWidget(self.lblBemVindo)
        spacerItem1 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_6.addItem(spacerItem1)
        self.lblSlogan = QtWidgets.QLabel(self.frmIconeTitulo)
        self.lblSlogan.setAlignment(QtCore.Qt.AlignCenter)
        self.lblSlogan.setObjectName("lblSlogan")
        self.verticalLayout_6.addWidget(self.lblSlogan)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem2)
        self.btnIniciar = QtWidgets.QPushButton(self.frmIconeTitulo)
        self.btnIniciar.setMinimumSize(QtCore.QSize(0, 71))
        self.btnIniciar.setStyleSheet(self._estilo_btn_destaque)
        self.btnIniciar.setObjectName("btnIniciar")
        self.verticalLayout_6.addWidget(self.btnIniciar)
        self.horizontalLayout_2.addWidget(self.frmIconeTitulo)
        self.frmAuxPgInicialDir = QtWidgets.QFrame(self.frmPgInicial)
        self.frmAuxPgInicialDir.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frmAuxPgInicialDir.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frmAuxPgInicialDir.setObjectName("frmAuxPgInicialDir")
        self.horizontalLayout_2.addWidget(self.frmAuxPgInicialDir)
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
        self.gridLayout = QtWidgets.QGridLayout(self.frmUpload)
        self.gridLayout.setContentsMargins(30, -1, 30, -1)
        self.gridLayout.setObjectName("gridLayout")
        self.frmImgEDetalhes = QtWidgets.QFrame(self.frmUpload)
        self.frmImgEDetalhes.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frmImgEDetalhes.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frmImgEDetalhes.setObjectName("frmImgEDetalhes")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frmImgEDetalhes)
        self.horizontalLayout_9.setSpacing(50)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.frmPreviaTemplate = QtWidgets.QFrame(self.frmImgEDetalhes)
        self.frmPreviaTemplate.setMaximumSize(QtCore.QSize(400, 16777215))
        self.frmPreviaTemplate.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frmPreviaTemplate.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frmPreviaTemplate.setObjectName("frmPreviaTemplate")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.frmPreviaTemplate)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.btnPreviaImg = QtWidgets.QPushButton(self.frmPreviaTemplate)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnPreviaImg.sizePolicy().hasHeightForWidth())
        self.btnPreviaImg.setSizePolicy(sizePolicy)
        self.btnPreviaImg.setMaximumSize(QtCore.QSize(400, 300))
        self.btnPreviaImg.setText("")
        self.btnPreviaImg.setIconSize(QtCore.QSize(300, 300))
        self.btnPreviaImg.setObjectName("btnPreviaImg")
        self.verticalLayout_11.addWidget(self.btnPreviaImg)
        self.frmConfigTemplate = QtWidgets.QFrame(self.frmPreviaTemplate)
        self.frmConfigTemplate.setStyleSheet(self._estilo_frm_secundario)
        self.frmConfigTemplate.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frmConfigTemplate.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frmConfigTemplate.setObjectName("frmConfigTemplate")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frmConfigTemplate)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, -1)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.frmInfoTemplate = QtWidgets.QFrame(self.frmConfigTemplate)
        self.frmInfoTemplate.setMaximumSize(QtCore.QSize(16777215, 61))
        self.frmInfoTemplate.setStyleSheet(self._estilo_frm_titulo)
        self.frmInfoTemplate.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frmInfoTemplate.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frmInfoTemplate.setObjectName("frmInfoTemplate")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frmInfoTemplate)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.lblTipoTamanhoImpressao = QtWidgets.QLabel(self.frmInfoTemplate)
        self.lblTipoTamanhoImpressao.setObjectName("lblTipoTamanhoImpressao")
        self.horizontalLayout_6.addWidget(self.lblTipoTamanhoImpressao)
        self.verticalLayout_8.addWidget(self.frmInfoTemplate)
        self.frmBtnPapelFoto = QtWidgets.QFrame(self.frmConfigTemplate)
        self.frmBtnPapelFoto.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frmBtnPapelFoto.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frmBtnPapelFoto.setObjectName("frmBtnPapelFoto")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frmBtnPapelFoto)
        self.horizontalLayout_7.setContentsMargins(20, -1, 20, -1)
        self.horizontalLayout_7.setSpacing(20)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.btnPadraoPapel = QtWidgets.QPushButton(self.frmBtnPapelFoto)
        self.btnPadraoPapel.setMinimumSize(QtCore.QSize(0, 30))
        self.btnPadraoPapel.setStyleSheet(self._estilo_btn_clicado)
        self.btnPadraoPapel.setObjectName("btnPadraoPapel")
        self.horizontalLayout_7.addWidget(self.btnPadraoPapel)
        self.btnPadraoFoto = QtWidgets.QPushButton(self.frmBtnPapelFoto)
        self.btnPadraoFoto.setMinimumSize(QtCore.QSize(0, 30))
        self.btnPadraoFoto.setStyleSheet(self._estilo_btn_desfoque)
        self.btnPadraoFoto.setObjectName("btnPadraoFoto")
        self.horizontalLayout_7.addWidget(self.btnPadraoFoto)
        self.verticalLayout_8.addWidget(self.frmBtnPapelFoto)
        self.frmCmbBox = QtWidgets.QFrame(self.frmConfigTemplate)
        self.frmCmbBox.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frmCmbBox.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frmCmbBox.setObjectName("frmCmbBox")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frmCmbBox)
        self.horizontalLayout_8.setContentsMargins(30, -1, 30, -1)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.cmbTamanhoImpressao = QtWidgets.QComboBox(self.frmCmbBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmbTamanhoImpressao.sizePolicy().hasHeightForWidth())
        self.cmbTamanhoImpressao.setSizePolicy(sizePolicy)
        self.cmbTamanhoImpressao.setMaximumSize(QtCore.QSize(16777215, 50))
        self.cmbTamanhoImpressao.setStyleSheet(self._estilo_cmbBox)
        self.cmbTamanhoImpressao.setObjectName("cmbTamanhoImpressao")
        self.cmbTamanhoImpressao.addItem("")
        self.horizontalLayout_8.addWidget(self.cmbTamanhoImpressao)
        self.verticalLayout_8.addWidget(self.frmCmbBox)
        self.verticalLayout_11.addWidget(self.frmConfigTemplate)
        self.horizontalLayout_9.addWidget(self.frmPreviaTemplate)
        self.frmConfigImg = QtWidgets.QFrame(self.frmImgEDetalhes)
        self.frmConfigImg.setMaximumSize(QtCore.QSize(400, 16777215))
        self.frmConfigImg.setStyleSheet(self._estilo_frm_secundario)
        self.frmConfigImg.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frmConfigImg.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frmConfigImg.setObjectName("frmConfigImg")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frmConfigImg)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, -1)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.frmInfoImg = QtWidgets.QFrame(self.frmConfigImg)
        self.frmInfoImg.setMaximumSize(QtCore.QSize(16777215, 61))
        self.frmInfoImg.setStyleSheet(self._estilo_frm_titulo)
        self.frmInfoImg.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frmInfoImg.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frmInfoImg.setObjectName("frmInfoImg")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frmInfoImg)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lblTituloDetalhes = QtWidgets.QLabel(self.frmInfoImg)
        self.lblTituloDetalhes.setObjectName("lblTituloDetalhes")
        self.horizontalLayout_5.addWidget(self.lblTituloDetalhes)
        self.verticalLayout_9.addWidget(self.frmInfoImg)
        self.frmConfigInfos = QtWidgets.QFrame(self.frmConfigImg)
        self.frmConfigInfos.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frmConfigInfos.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frmConfigInfos.setObjectName("frmConfigInfos")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.frmConfigInfos)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.frmInfoNomeResPPI = QtWidgets.QFrame(self.frmConfigInfos)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frmInfoNomeResPPI.sizePolicy().hasHeightForWidth())
        self.frmInfoNomeResPPI.setSizePolicy(sizePolicy)
        self.frmInfoNomeResPPI.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frmInfoNomeResPPI.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frmInfoNomeResPPI.setObjectName("frmInfoNomeResPPI")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frmInfoNomeResPPI)
        self.verticalLayout_7.setContentsMargins(20, -1, 20, -1)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.lblInfoNomeImg = QtWidgets.QLabel(self.frmInfoNomeResPPI)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblInfoNomeImg.sizePolicy().hasHeightForWidth())
        self.lblInfoNomeImg.setSizePolicy(sizePolicy)
        self.lblInfoNomeImg.setObjectName("lblInfoNomeImg")
        self.verticalLayout_7.addWidget(self.lblInfoNomeImg)
        self.lblInfoResolucaoImg = QtWidgets.QLabel(self.frmInfoNomeResPPI)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblInfoResolucaoImg.sizePolicy().hasHeightForWidth())
        self.lblInfoResolucaoImg.setSizePolicy(sizePolicy)
        self.lblInfoResolucaoImg.setObjectName("lblInfoResolucaoImg")
        self.verticalLayout_7.addWidget(self.lblInfoResolucaoImg)
        self.lblInfoPPIImagem = QtWidgets.QLabel(self.frmInfoNomeResPPI)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblInfoPPIImagem.sizePolicy().hasHeightForWidth())
        self.lblInfoPPIImagem.setSizePolicy(sizePolicy)
        self.lblInfoPPIImagem.setObjectName("lblInfoPPIImagem")
        self.verticalLayout_7.addWidget(self.lblInfoPPIImagem)
        self.lblInfoResolucaoImgSaida = QtWidgets.QLabel(self.frmInfoNomeResPPI)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblInfoResolucaoImgSaida.sizePolicy().hasHeightForWidth())
        self.lblInfoResolucaoImgSaida.setSizePolicy(sizePolicy)
        self.lblInfoResolucaoImgSaida.setObjectName("lblInfoResolucaoImgSaida")
        self.verticalLayout_7.addWidget(self.lblInfoResolucaoImgSaida)
        self.horizontalLayout_15.addWidget(self.frmInfoNomeResPPI)
        self.frmDetalhesNomeResPPI = QtWidgets.QFrame(self.frmConfigInfos)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frmDetalhesNomeResPPI.sizePolicy().hasHeightForWidth())
        self.frmDetalhesNomeResPPI.setSizePolicy(sizePolicy)
        self.frmDetalhesNomeResPPI.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frmDetalhesNomeResPPI.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frmDetalhesNomeResPPI.setObjectName("frmDetalhesNomeResPPI")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.frmDetalhesNomeResPPI)
        self.verticalLayout_17.setContentsMargins(20, -1, 20, -1)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.lblNomeImg = QtWidgets.QLabel(self.frmDetalhesNomeResPPI)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblNomeImg.sizePolicy().hasHeightForWidth())
        self.lblNomeImg.setSizePolicy(sizePolicy)
        self.lblNomeImg.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblNomeImg.setObjectName("lblNomeImg")
        self.verticalLayout_17.addWidget(self.lblNomeImg)
        self.lblResolucaoImg = QtWidgets.QLabel(self.frmDetalhesNomeResPPI)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblResolucaoImg.sizePolicy().hasHeightForWidth())
        self.lblResolucaoImg.setSizePolicy(sizePolicy)
        self.lblResolucaoImg.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblResolucaoImg.setObjectName("lblResolucaoImg")
        self.verticalLayout_17.addWidget(self.lblResolucaoImg)
        self.lblPPIImagem = QtWidgets.QLabel(self.frmDetalhesNomeResPPI)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblPPIImagem.sizePolicy().hasHeightForWidth())
        self.lblPPIImagem.setSizePolicy(sizePolicy)
        self.lblPPIImagem.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblPPIImagem.setObjectName("lblPPIImagem")
        self.verticalLayout_17.addWidget(self.lblPPIImagem)
        self.lblResolucaoImgSaida = QtWidgets.QLabel(self.frmDetalhesNomeResPPI)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblResolucaoImgSaida.sizePolicy().hasHeightForWidth())
        self.lblResolucaoImgSaida.setSizePolicy(sizePolicy)
        self.lblResolucaoImgSaida.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblResolucaoImgSaida.setObjectName("lblResolucaoImgSaida")
        self.verticalLayout_17.addWidget(self.lblResolucaoImgSaida)
        self.horizontalLayout_15.addWidget(self.frmDetalhesNomeResPPI)
        self.verticalLayout_9.addWidget(self.frmConfigInfos)
        self.frmInfoTituloFator = QtWidgets.QFrame(self.frmConfigImg)
        self.frmInfoTituloFator.setMaximumSize(QtCore.QSize(16777215, 61))
        self.frmInfoTituloFator.setStyleSheet(self._estilo_frm_titulo)
        self.frmInfoTituloFator.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frmInfoTituloFator.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frmInfoTituloFator.setObjectName("frmInfoTituloFator")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frmInfoTituloFator)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lblTituloFator = QtWidgets.QLabel(self.frmInfoTituloFator)
        self.lblTituloFator.setObjectName("lblTituloFator")
        self.horizontalLayout_4.addWidget(self.lblTituloFator)
        self.verticalLayout_9.addWidget(self.frmInfoTituloFator)
        self.frmBtnFatores = QtWidgets.QFrame(self.frmConfigImg)
        self.frmBtnFatores.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frmBtnFatores.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frmBtnFatores.setObjectName("frmBtnFatores")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frmBtnFatores)
        self.verticalLayout_10.setContentsMargins(20, -1, 20, -1)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.btn2x = QtWidgets.QPushButton(self.frmBtnFatores)
        self.btn2x.setMaximumSize(QtCore.QSize(16777215, 30))
        self.btn2x.setStyleSheet(self._estilo_btn_desfoque)
        self.btn2x.setObjectName("btn2x")
        self.verticalLayout_10.addWidget(self.btn2x)
        self.btn4x = QtWidgets.QPushButton(self.frmBtnFatores)
        self.btn4x.setMaximumSize(QtCore.QSize(16777215, 30))
        self.btn4x.setStyleSheet(self._estilo_btn_desfoque)
        self.btn4x.setObjectName("btn4x")
        self.verticalLayout_10.addWidget(self.btn4x)
        self.btn8x = QtWidgets.QPushButton(self.frmBtnFatores)
        self.btn8x.setMaximumSize(QtCore.QSize(16777215, 30))
        self.btn8x.setStyleSheet(self._estilo_btn_clicado)
        self.btn8x.setObjectName("btn8x")
        self.verticalLayout_10.addWidget(self.btn8x)
        self.verticalLayout_9.addWidget(self.frmBtnFatores)
        self.horizontalLayout_9.addWidget(self.frmConfigImg)
        self.gridLayout.addWidget(self.frmImgEDetalhes, 0, 1, 1, 1)
        self.frmBtnProcessarVoltar = QtWidgets.QFrame(self.frmUpload)
        self.frmBtnProcessarVoltar.setMaximumSize(QtCore.QSize(16777215, 65))
        self.frmBtnProcessarVoltar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frmBtnProcessarVoltar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frmBtnProcessarVoltar.setObjectName("frmBtnProcessarVoltar")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frmBtnProcessarVoltar)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.btnVoltarInicio = QtWidgets.QPushButton(self.frmBtnProcessarVoltar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnVoltarInicio.sizePolicy().hasHeightForWidth())
        self.btnVoltarInicio.setSizePolicy(sizePolicy)
        self.btnVoltarInicio.setMinimumSize(QtCore.QSize(0, 0))
        self.btnVoltarInicio.setMaximumSize(QtCore.QSize(150, 50))
        self.btnVoltarInicio.setStyleSheet(self._estilo_btn_desfoque)
        self.btnVoltarInicio.setObjectName("btnVoltarInicio")
        self.horizontalLayout_3.addWidget(self.btnVoltarInicio)
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.btnProcessaImg = QtWidgets.QPushButton(self.frmBtnProcessarVoltar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnProcessaImg.sizePolicy().hasHeightForWidth())
        self.btnProcessaImg.setSizePolicy(sizePolicy)
        self.btnProcessaImg.setMinimumSize(QtCore.QSize(0, 0))
        self.btnProcessaImg.setMaximumSize(QtCore.QSize(150, 50))
        self.btnProcessaImg.setStyleSheet(self._estilo_btn_destaque)
        self.btnProcessaImg.setObjectName("btnProcessaImg")
        self.horizontalLayout_3.addWidget(self.btnProcessaImg)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.gridLayout.addWidget(self.frmBtnProcessarVoltar, 1, 1, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 0, 0, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem7, 0, 2, 1, 1)
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
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frmDecisao)
        self.gridLayout_2.setContentsMargins(30, -1, 30, -1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frmImgProcessadaDetalhes = QtWidgets.QFrame(self.frmDecisao)
        self.frmImgProcessadaDetalhes.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frmImgProcessadaDetalhes.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frmImgProcessadaDetalhes.setObjectName("frmImgProcessadaDetalhes")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frmImgProcessadaDetalhes)
        self.horizontalLayout_10.setSpacing(50)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.frmPreviaTemplateProcessada = QtWidgets.QFrame(self.frmImgProcessadaDetalhes)
        self.frmPreviaTemplateProcessada.setMaximumSize(QtCore.QSize(400, 16777215))
        self.frmPreviaTemplateProcessada.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frmPreviaTemplateProcessada.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frmPreviaTemplateProcessada.setObjectName("frmPreviaTemplateProcessada")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.frmPreviaTemplateProcessada)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.btnPreviaImgProcessada = QtWidgets.QPushButton(self.frmPreviaTemplateProcessada)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnPreviaImgProcessada.sizePolicy().hasHeightForWidth())
        self.btnPreviaImgProcessada.setSizePolicy(sizePolicy)
        self.btnPreviaImgProcessada.setMaximumSize(QtCore.QSize(400, 300))
        self.btnPreviaImgProcessada.setText("")
        self.btnPreviaImgProcessada.setIconSize(QtCore.QSize(300, 300))
        self.btnPreviaImgProcessada.setObjectName("btnPreviaImgProcessada")
        self.verticalLayout_12.addWidget(self.btnPreviaImgProcessada)
        self.btnPreviaProcessada = QtWidgets.QPushButton(self.frmPreviaTemplateProcessada)
        self.btnPreviaProcessada.setMinimumSize(QtCore.QSize(0, 30))
        self.btnPreviaProcessada.setStyleSheet(self._estilo_btn_desfoque)
        self.btnPreviaProcessada.setObjectName("btnPreviaProcessada")
        self.verticalLayout_12.addWidget(self.btnPreviaProcessada)
        self.horizontalLayout_10.addWidget(self.frmPreviaTemplateProcessada)
        self.frmComparacao = QtWidgets.QFrame(self.frmImgProcessadaDetalhes)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frmComparacao.sizePolicy().hasHeightForWidth())
        self.frmComparacao.setSizePolicy(sizePolicy)
        self.frmComparacao.setMaximumSize(QtCore.QSize(400, 500))
        self.frmComparacao.setStyleSheet(self._estilo_frm_secundario)
        self.frmComparacao.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frmComparacao.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frmComparacao.setObjectName("frmComparacao")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.frmComparacao)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, -1)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.frmInfoImgProcessada = QtWidgets.QFrame(self.frmComparacao)
        self.frmInfoImgProcessada.setMaximumSize(QtCore.QSize(16777215, 61))
        self.frmInfoImgProcessada.setStyleSheet(self._estilo_frm_titulo)
        self.frmInfoImgProcessada.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frmInfoImgProcessada.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frmInfoImgProcessada.setObjectName("frmInfoImgProcessada")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frmInfoImgProcessada)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.lblTituloDetalhesProcessada = QtWidgets.QLabel(self.frmInfoImgProcessada)
        self.lblTituloDetalhesProcessada.setObjectName("lblTituloDetalhesProcessada")
        self.horizontalLayout_11.addWidget(self.lblTituloDetalhesProcessada)
        self.verticalLayout_13.addWidget(self.frmInfoImgProcessada)
        self.frmComparacaoOriginalProcessada = QtWidgets.QFrame(self.frmComparacao)
        self.frmComparacaoOriginalProcessada.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frmComparacaoOriginalProcessada.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frmComparacaoOriginalProcessada.setObjectName("frmComparacaoOriginalProcessada")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.frmComparacaoOriginalProcessada)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.frmNomeResPPIProcessadaInfo = QtWidgets.QFrame(self.frmComparacaoOriginalProcessada)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frmNomeResPPIProcessadaInfo.sizePolicy().hasHeightForWidth())
        self.frmNomeResPPIProcessadaInfo.setSizePolicy(sizePolicy)
        self.frmNomeResPPIProcessadaInfo.setMinimumSize(QtCore.QSize(0, 100))
        self.frmNomeResPPIProcessadaInfo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frmNomeResPPIProcessadaInfo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frmNomeResPPIProcessadaInfo.setObjectName("frmNomeResPPIProcessadaInfo")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.frmNomeResPPIProcessadaInfo)
        self.verticalLayout_18.setContentsMargins(20, -1, 20, -1)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.lblNomeImgProcessadaInfo = QtWidgets.QLabel(self.frmNomeResPPIProcessadaInfo)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblNomeImgProcessadaInfo.sizePolicy().hasHeightForWidth())
        self.lblNomeImgProcessadaInfo.setSizePolicy(sizePolicy)
        self.lblNomeImgProcessadaInfo.setObjectName("lblNomeImgProcessadaInfo")
        self.verticalLayout_18.addWidget(self.lblNomeImgProcessadaInfo)
        self.lblPPIImagemProcessadaInfo = QtWidgets.QLabel(self.frmNomeResPPIProcessadaInfo)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblPPIImagemProcessadaInfo.sizePolicy().hasHeightForWidth())
        self.lblPPIImagemProcessadaInfo.setSizePolicy(sizePolicy)
        self.lblPPIImagemProcessadaInfo.setObjectName("lblPPIImagemProcessadaInfo")
        self.verticalLayout_18.addWidget(self.lblPPIImagemProcessadaInfo)
        self.horizontalLayout_16.addWidget(self.frmNomeResPPIProcessadaInfo)
        self.frmNomeResPPIProcessada = QtWidgets.QFrame(self.frmComparacaoOriginalProcessada)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frmNomeResPPIProcessada.sizePolicy().hasHeightForWidth())
        self.frmNomeResPPIProcessada.setSizePolicy(sizePolicy)
        self.frmNomeResPPIProcessada.setMinimumSize(QtCore.QSize(0, 100))
        self.frmNomeResPPIProcessada.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frmNomeResPPIProcessada.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frmNomeResPPIProcessada.setObjectName("frmNomeResPPIProcessada")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.frmNomeResPPIProcessada)
        self.verticalLayout_14.setContentsMargins(20, -1, 20, -1)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.lblNomeImgProcessada = QtWidgets.QLabel(self.frmNomeResPPIProcessada)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblNomeImgProcessada.sizePolicy().hasHeightForWidth())
        self.lblNomeImgProcessada.setSizePolicy(sizePolicy)
        self.lblNomeImgProcessada.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblNomeImgProcessada.setObjectName("lblNomeImgProcessada")
        self.verticalLayout_14.addWidget(self.lblNomeImgProcessada)
        self.lblTemplateImagemProcessada = QtWidgets.QLabel(self.frmNomeResPPIProcessada)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblTemplateImagemProcessada.sizePolicy().hasHeightForWidth())
        self.lblTemplateImagemProcessada.setSizePolicy(sizePolicy)
        self.lblTemplateImagemProcessada.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblTemplateImagemProcessada.setObjectName("lblPPIImagemProcessada")
        self.verticalLayout_14.addWidget(self.lblTemplateImagemProcessada)
        self.horizontalLayout_16.addWidget(self.frmNomeResPPIProcessada)
        self.verticalLayout_13.addWidget(self.frmComparacaoOriginalProcessada)
        self.frmInfoComparacao = QtWidgets.QFrame(self.frmComparacao)
        self.frmInfoComparacao.setMaximumSize(QtCore.QSize(16777215, 61))
        self.frmInfoComparacao.setStyleSheet(self._estilo_frm_titulo_quadrado)
        self.frmInfoComparacao.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frmInfoComparacao.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frmInfoComparacao.setObjectName("frmInfoComparacao")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.frmInfoComparacao)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.lblDetalhesImgOriginal = QtWidgets.QLabel(self.frmInfoComparacao)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblDetalhesImgOriginal.sizePolicy().hasHeightForWidth())
        self.lblDetalhesImgOriginal.setSizePolicy(sizePolicy)
        self.lblDetalhesImgOriginal.setObjectName("lblDetalhesImgOriginal")
        self.horizontalLayout_12.addWidget(self.lblDetalhesImgOriginal)
        self.lblDetalhesImgProcessada = QtWidgets.QLabel(self.frmInfoComparacao)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblDetalhesImgProcessada.sizePolicy().hasHeightForWidth())
        self.lblDetalhesImgProcessada.setSizePolicy(sizePolicy)
        self.lblDetalhesImgProcessada.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblDetalhesImgProcessada.setObjectName("lblDetalhesImgProcessada")
        self.horizontalLayout_12.addWidget(self.lblDetalhesImgProcessada)
        self.verticalLayout_13.addWidget(self.frmInfoComparacao)
        self.frmDetalhesComparacao = QtWidgets.QFrame(self.frmComparacao)
        self.frmDetalhesComparacao.setStyleSheet(self._estilo_frm_titulo_quadrado)
        self.frmDetalhesComparacao.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frmDetalhesComparacao.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frmDetalhesComparacao.setObjectName("frmDetalhesComparacao")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.frmDetalhesComparacao)
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.frmDetalhesImgOriginal = QtWidgets.QFrame(self.frmDetalhesComparacao)
        self.frmDetalhesImgOriginal.setStyleSheet(self._estilo_frm_secundario_quadrado)
        self.frmDetalhesImgOriginal.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frmDetalhesImgOriginal.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frmDetalhesImgOriginal.setObjectName("frmDetalhesImgOriginal")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.frmDetalhesImgOriginal)
        self.verticalLayout_15.setContentsMargins(20, -1, 20, -1)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.lblDetalhesImgOriginalPPI = QtWidgets.QLabel(self.frmDetalhesImgOriginal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblDetalhesImgOriginalPPI.sizePolicy().hasHeightForWidth())
        self.lblDetalhesImgOriginalPPI.setSizePolicy(sizePolicy)
        self.lblDetalhesImgOriginalPPI.setObjectName("lblDetalhesImgOriginalPPI")
        self.verticalLayout_15.addWidget(self.lblDetalhesImgOriginalPPI)
        self.lblDetalhesImgOriginalRes = QtWidgets.QLabel(self.frmDetalhesImgOriginal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblDetalhesImgOriginalRes.sizePolicy().hasHeightForWidth())
        self.lblDetalhesImgOriginalRes.setSizePolicy(sizePolicy)
        self.lblDetalhesImgOriginalRes.setObjectName("lblDetalhesImgOriginalRes")
        self.verticalLayout_15.addWidget(self.lblDetalhesImgOriginalRes)
        self.horizontalLayout_13.addWidget(self.frmDetalhesImgOriginal)
        self.frmDetalhesImgProcessada = QtWidgets.QFrame(self.frmDetalhesComparacao)
        self.frmDetalhesImgProcessada.setStyleSheet(self._estilo_frm_secundario_quadrado)
        self.frmDetalhesImgProcessada.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frmDetalhesImgProcessada.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frmDetalhesImgProcessada.setObjectName("frmDetalhesImgProcessada")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.frmDetalhesImgProcessada)
        self.verticalLayout_16.setContentsMargins(20, -1, 20, -1)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.lblDetalhesImgProcessadaPPI = QtWidgets.QLabel(self.frmDetalhesImgProcessada)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblDetalhesImgProcessadaPPI.sizePolicy().hasHeightForWidth())
        self.lblDetalhesImgProcessadaPPI.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblDetalhesImgProcessadaPPI.setSizePolicy(sizePolicy)
        self.lblDetalhesImgProcessadaPPI.setObjectName("lblDetalhesImgProcessadaPPI")
        self.verticalLayout_16.addWidget(self.lblDetalhesImgProcessadaPPI)
        self.lblDetalhesImgProcessadaRes = QtWidgets.QLabel(self.frmDetalhesImgProcessada)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblDetalhesImgProcessadaRes.sizePolicy().hasHeightForWidth())
        self.lblDetalhesImgProcessadaRes.setSizePolicy(sizePolicy)
        self.lblDetalhesImgProcessadaRes.setObjectName("lblDetalhesImgProcessadaRes")
        self.lblDetalhesImgProcessadaRes.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.verticalLayout_16.addWidget(self.lblDetalhesImgProcessadaRes)
        self.horizontalLayout_13.addWidget(self.frmDetalhesImgProcessada)
        self.verticalLayout_13.addWidget(self.frmDetalhesComparacao)
        self.horizontalLayout_10.addWidget(self.frmComparacao)
        self.gridLayout_2.addWidget(self.frmImgProcessadaDetalhes, 0, 1, 1, 1)
        self.frmBtnReprocessarSalvar = QtWidgets.QFrame(self.frmDecisao)
        self.frmBtnReprocessarSalvar.setMaximumSize(QtCore.QSize(16777215, 65))
        self.frmBtnReprocessarSalvar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frmBtnReprocessarSalvar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frmBtnReprocessarSalvar.setObjectName("frmBtnReprocessarSalvar")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.frmBtnReprocessarSalvar)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem8)
        self.btnReprocessar = QtWidgets.QPushButton(self.frmBtnReprocessarSalvar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnReprocessar.sizePolicy().hasHeightForWidth())
        self.btnReprocessar.setSizePolicy(sizePolicy)
        self.btnReprocessar.setMinimumSize(QtCore.QSize(0, 0))
        self.btnReprocessar.setMaximumSize(QtCore.QSize(150, 50))
        self.btnReprocessar.setStyleSheet(self._estilo_btn_desfoque)
        self.btnReprocessar.setObjectName("btnReprocessar")
        self.horizontalLayout_14.addWidget(self.btnReprocessar)
        spacerItem9 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem9)
        self.btnSalvar = QtWidgets.QPushButton(self.frmBtnReprocessarSalvar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnSalvar.sizePolicy().hasHeightForWidth())
        self.btnSalvar.setSizePolicy(sizePolicy)
        self.btnSalvar.setMinimumSize(QtCore.QSize(0, 0))
        self.btnSalvar.setMaximumSize(QtCore.QSize(150, 50))
        self.btnSalvar.setStyleSheet(self._estilo_btn_destaque)
        self.btnSalvar.setObjectName("btnSalvar")
        self.horizontalLayout_14.addWidget(self.btnSalvar)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem10)
        self.gridLayout_2.addWidget(self.frmBtnReprocessarSalvar, 1, 1, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem11, 0, 0, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem12, 0, 2, 1, 1)
        self.verticalLayout_4.addWidget(self.frmDecisao)
        self.stckPrincipal.addWidget(self.pgDecisao)
        self.pgAgradecimento = QtWidgets.QWidget()
        self.pgAgradecimento.setObjectName("pgAgradecimento")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.pgAgradecimento)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frmPgAg = QtWidgets.QFrame(self.pgAgradecimento)
        self.frmPgAg.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frmPgAg.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frmPgAg.setObjectName("frmPgAg")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.frmPgAg)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.frmAuxPgAgEsq = QtWidgets.QFrame(self.frmPgAg)
        self.frmAuxPgAgEsq.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frmAuxPgAgEsq.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frmAuxPgAgEsq.setObjectName("frmAuxPgAgEsq")
        self.horizontalLayout_17.addWidget(self.frmAuxPgAgEsq)
        self.frmIconeTituloAg = QtWidgets.QFrame(self.frmPgAg)
        self.frmIconeTituloAg.setMaximumSize(QtCore.QSize(256, 16777215))
        self.frmIconeTituloAg.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frmIconeTituloAg.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frmIconeTituloAg.setObjectName("frmIconeTituloAg")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.frmIconeTituloAg)
        self.verticalLayout_19.setContentsMargins(-1, 50, -1, 50)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.btnIconeAg = QtWidgets.QPushButton(self.frmIconeTituloAg)
        self.btnIconeAg.setStyleSheet("border: none;")
        self.btnIconeAg.setText("")
        self.btnIconeAg.setIcon(icon)
        self.btnIconeAg.setIconSize(QtCore.QSize(150, 150))
        self.btnIconeAg.setObjectName("btnIconeAg")
        self.verticalLayout_19.addWidget(self.btnIconeAg)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout_19.addItem(spacerItem13)
        self.lblAg = QtWidgets.QLabel(self.frmIconeTituloAg)
        self.lblAg.setAlignment(QtCore.Qt.AlignCenter)
        self.lblAg.setObjectName("lblAg")
        self.verticalLayout_19.addWidget(self.lblAg)
        spacerItem14 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_19.addItem(spacerItem14)
        self.btnVoltarAg = QtWidgets.QPushButton(self.frmIconeTituloAg)
        self.btnVoltarAg.setMinimumSize(QtCore.QSize(0, 71))
        self.btnVoltarAg.setStyleSheet(self._estilo_btn_destaque)
        self.btnVoltarAg.setObjectName("btnVoltarAg")
        self.verticalLayout_19.addWidget(self.btnVoltarAg)
        spacerItem15 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_19.addItem(spacerItem15)
        self.horizontalLayout_17.addWidget(self.frmIconeTituloAg)
        self.frmAuxPgAgDir = QtWidgets.QFrame(self.frmPgAg)
        self.frmAuxPgAgDir.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frmAuxPgAgDir.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frmAuxPgAgDir.setObjectName("frmAuxPgAgDir")
        self.horizontalLayout_17.addWidget(self.frmAuxPgAgDir)
        self.verticalLayout_3.addWidget(self.frmPgAg)
        self.stckPrincipal.addWidget(self.pgAgradecimento)
        self.horizontalLayout.addWidget(self.stckPrincipal)
        App_IVision.setCentralWidget(self.centralwidget)

        self.retranslateUi(App_IVision)
        self.stckPrincipal.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(App_IVision)


    def retranslateUi(self, App_IVision):
        _translate = QtCore.QCoreApplication.translate
        App_IVision.setWindowTitle(_translate("App_IVision", "IVision"))
        self.lblBemVindo.setText(_translate("App_IVision", "Bem-vindo ao IVision"))
        self.lblSlogan.setText(_translate("App_IVision", "<slogan>"))
        self.btnIniciar.setText(_translate("App_IVision", "Iniciar Processo"))
        self.lblTipoTamanhoImpressao.setText(_translate("App_IVision", "Padrão de Tamanho de Impressão"))
        self.btnPadraoPapel.setText(_translate("App_IVision", "Papel"))
        self.btnPadraoFoto.setText(_translate("App_IVision", "Foto"))
        self.cmbTamanhoImpressao.setItemText(0, _translate("App_IVision", "Exemplo"))
        self.lblTituloDetalhes.setText(_translate("App_IVision", "Detalhes da Imagem"))
        self.lblInfoNomeImg.setText(_translate("App_IVision", "Nome:"))
        self.lblInfoResolucaoImg.setText(_translate("App_IVision", "Resolução:"))
        self.lblInfoPPIImagem.setText(_translate("App_IVision", "PPI:"))
        self.lblNomeImg.setText(_translate("App_IVision", "<Nome IMG>"))
        self.lblResolucaoImg.setText(_translate("App_IVision", "<Resolução (512x512 px)>"))
        self.lblInfoResolucaoImgSaida.setText(_translate("App_IVision", "Resolução de Saída:"))
        self.lblPPIImagem.setText(_translate("App_IVision", "<Numero PPI>"))
        self.lblResolucaoImgSaida.setText(_translate("App_IVision", "<Resolução (512x512 px)>"))
        self.lblTituloFator.setText(_translate("App_IVision", "Escolha o fator de aumento"))
        self.btn2x.setText(_translate("App_IVision", "x2"))
        self.btn4x.setText(_translate("App_IVision", "x4"))
        self.btn8x.setText(_translate("App_IVision", "x8"))
        self.btnVoltarInicio.setText(_translate("App_IVision", "Voltar"))
        self.btnProcessaImg.setText(_translate("App_IVision", "Processar"))
        self.btnPreviaProcessada.setText(_translate("App_IVision", "Abrir Prévia"))
        self.lblTituloDetalhesProcessada.setText(_translate("App_IVision", "Detalhes da Imagem"))
        self.lblNomeImgProcessadaInfo.setText(_translate("App_IVision", "Nome:"))
        self.lblPPIImagemProcessadaInfo.setText(_translate("App_IVision", "Template:"))
        self.lblNomeImgProcessada.setText(_translate("App_IVision", "<Nome IMG>"))
        self.lblTemplateImagemProcessada.setText(_translate("App_IVision", "<Numero PPI>"))
        self.lblDetalhesImgOriginal.setText(_translate("App_IVision", "Original"))
        self.lblDetalhesImgProcessada.setText(_translate("App_IVision", "Aumentado"))
        self.lblDetalhesImgOriginalPPI.setText(_translate("App_IVision", "<ppi_original>"))
        self.lblDetalhesImgOriginalRes.setText(_translate("App_IVision", "<res_original>"))
        self.lblDetalhesImgProcessadaPPI.setText(_translate("App_IVision", "<ppi_processada>"))
        self.lblDetalhesImgProcessadaRes.setText(_translate("App_IVision", "<res_processada>"))
        self.btnReprocessar.setText(_translate("App_IVision", "Reprocessar"))
        self.btnSalvar.setText(_translate("App_IVision", "Salvar"))
        self.lblAg.setText(_translate("App_IVision", "Obrigado por usar nossa aplicação!"))
        self.btnVoltarAg.setText(_translate("App_IVision", "Voltar ao Início"))


    def atualizaDadosUpload(self, imagem: Imagem) -> None:
        """
        Método para que atualiza informações de PPI na tela de upload.
        :param imagem: objeto de tipo Imagem que será configurado na tela de upload.
        :return: None
        """
        textoPPI = f"{imagem.ppi} PPI"
        self.lblPPIImagem.setText(textoPPI)
    

    def atualizaResSaida(self, imagem: Imagem, fator: int) -> None:
        """
        Método que atualiza a resolução calculada de saída. Método disparado quando o usuário altera a escolha do fator de saída.
        """
        # Calculando resolução de saída
        textoResolucaoSaida = f"{imagem.largura * fator} x {imagem.altura * fator} px"
        self.lblResolucaoImgSaida.setText(textoResolucaoSaida)


    def configuraDadosUpload(self, imagem: Imagem, fator: int) -> None:
        """
        Método que ao receber um objeto de tipo Imagem, configura na tela os dados do mesmo, para informar ao usuário qual imagem será processada.
        :param imagem: objeto do tipo Imagem a ser configurada.
        :param fator: int que representa em quantas vezes a imagem será aumentada.
        :return: None
        """
        # Coletando as informações
        textoNome = nomeDoArquivo(imagem.caminhoImg)
        textoResolucao = f"{imagem.largura} x {imagem.altura} px"

        # Coletando o padrão do template da imagem fornecido
        templateImagem = imagem.tipoTemplate
        templateInicial = templateImagem.padrao().toString()
        listaTemplate = templateImagem.listaMembros()

        # Atribuindo cada info à seus respectivos campos
        self.lblNomeImg.setText(textoNome)
        self.lblResolucaoImg.setText(textoResolucao)
        self.atualizaDadosUpload(imagem)
        self.atualizaResSaida(imagem, fator)
        
        self.configuraOpcaoTemplate(templateImagem)
        self.cmbTamanhoImpressao.clear()
        self.cmbTamanhoImpressao.addItems(listaTemplate)
        self.cmbTamanhoImpressao.setCurrentText(templateInicial)


    def configuraImgPrevia(self, imgOriginal: Imagem, imgProcessada: Imagem) -> None:
        """
        Método para configurar a tela de prévia de imagem processada.
        :param imgOriginal: objeto Imagem escolhido pelo usuário.
        :param imgProcessada: objeto Imagem processada.
        :return: None
        """
        # Configurando prévia no botão
        self.btnPreviaImgProcessada = botaoComIcone(
            btn=self.btnPreviaImgProcessada,
            caminho=imgProcessada.caminhoImg,
            tamanho=(300, 300)
        )
        
        # Capturando as informações de ambas imagens
        nomeImg: str = nomeDoArquivo(imgOriginal.caminhoImg)
        templateImgOriginal: str = f"{imgOriginal.tipoTemplate.toString()}"
        resImgOriginal: str = f"{imgOriginal.largura} x {imgOriginal.altura} px"
        resImgProcessada: str = f"{imgProcessada.largura} x {imgProcessada.altura} px"
        ppiImgOriginal: str = f"{imgOriginal.ppi} PPI"
        ppiImgProcessada: str = f"{imgProcessada.ppi} PPI"

        # Setando os labels com as informações obtidas
        self.lblNomeImgProcessada.setText(nomeImg)
        self.lblTemplateImagemProcessada.setText(templateImgOriginal)
        self.lblDetalhesImgOriginalPPI.setText(ppiImgOriginal)
        self.lblDetalhesImgOriginalRes.setText(resImgOriginal)
        self.lblDetalhesImgProcessadaPPI.setText(ppiImgProcessada)
        self.lblDetalhesImgProcessadaRes.setText(resImgProcessada)

        self.stckPrincipal.setCurrentWidget(self.pgDecisao)


    def configuraOpcaoFator(self, fator: int) -> None:
        """
        Método que configura o design dos botões de fator de escolha, dando destaque ao btn clicado.
        :param fator: int que representa qual o botão clicado pelo usuário.
        :return: None
        """
        # Desfocando todos os botões
        self.btn2x.setStyleSheet(self._estilo_btn_desfoque)
        self.btn4x.setStyleSheet(self._estilo_btn_desfoque)
        self.btn8x.setStyleSheet(self._estilo_btn_desfoque)
        
        # Dando destaque ao botão clicado
        dictEscolha: dict = {
                2: self.btn2x,
                4: self.btn4x,
                8: self.btn8x
        }
        btnClicado = dictEscolha.get(fator, self.btn8x)
        btnClicado.setStyleSheet(self._estilo_btn_clicado)


    def configuraOpcaoTemplate(self, template: TipoTemplate) -> None:
        """
        Método que configura os botões de padrão de template, para destaque/desfoque do botão selecionado.
        :param template: TipoTemplate que determina se o botão "Papel" e "Foto" receberá destaque.
        :return: None
        """
        if isinstance(template, TemplateFoto):
            self.btnPadraoFoto.setStyleSheet(self._estilo_btn_clicado)
            self.btnPadraoPapel.setStyleSheet(self._estilo_btn_desfoque)
        else:
            self.btnPadraoFoto.setStyleSheet(self._estilo_btn_desfoque)
            self.btnPadraoPapel.setStyleSheet(self._estilo_btn_clicado)


    def configuraPrevia(self, btn: QtWidgets.QPushButton, caminho: str) -> None:
        """
        Método para adicionar a imagem de upload/processada para um botão, configurando a prévia da mesma ao usuário.
        :param btn: QPushButton a receber o ícone.
        :param caminho: str que representa o caminho da imagem a ser mostrada.
        :return: None
        """
        largura, altura = 400, 300
        btn = botaoComIcone(btn, caminho, (largura, altura))


    def _declaraEstilos(self) -> None:
        """
        Método para declarar todos os estilos utilizados pelos botões do aplicativo.
        :return: None
        """
        self._estilo_btn_clicado: str = """
        QPushButton{
            background-color: #ff8913; 
            border: 2px;
            border-radius: 5px;
        }
        """

        self._estilo_btn_destaque: str = """
        QPushButton{	
            background-color: #ff7a22;
            border: 2px;
            border-radius: 5px;
        }

        QPushButton::hover{
            background-color: #ffbd4b;
        }
        """
        
        self._estilo_btn_desfoque: str = """
        QPushButton{	
            background-color: rgba(255, 122, 34, 150);
            border: 2px;
            border-radius: 5px;
        }

        QPushButton::hover{
            background-color: #ffbd4b;
        }
        """

        self._estilo_cmbBox: str = """
        QComboBox{
            color: #171717;
            background-color: #EDEDED;
        }

        QComboBox::drop-down {
            border: 0px;
        }

        QComboBox::down-arrow { 
            image: url(""" + CAMINHO_SETA_BAIXO + """);
            width: 15px;
            height: 15px;
            border-radius: 10px;
        }
        """

        self._estilo_frm_principal: str = """
        background-color: #171717;
        color: #EDEDED;
        """

        self._estilo_frm_secundario: str = """
        background-color: #262626;
        border-radius: 10;
        """

        self._estilo_frm_secundario_quadrado: str = """
        background-color: #262626;
        border-radius: 0;
        """

        self._estilo_frm_titulo: str = """
        background-color: #4a4a4a;
        """

        self._estilo_frm_titulo_quadrado: str = """
        background-color: #4a4a4a;
        border-radius: 0px;
        """


    def _delegaAcoes(self) -> None:
        """
        Método para delegar todas as ações dos botões da janela FormApp.
        """
        self.btnIniciar.clicked.connect(self.controller.iniciaUpload)
        self.cmbTamanhoImpressao.activated.connect(self.controller.mudouTamanhoImpressao)
        self.btnPadraoPapel.clicked.connect(partial(self.controller.mudouPadraoImpressao, TemplatePapel))
        self.btnPadraoFoto.clicked.connect(partial(self.controller.mudouPadraoImpressao, TemplateFoto))
        self.btn2x.clicked.connect(partial(self.controller.salvaFatorUpscale, 2))
        self.btn4x.clicked.connect(partial(self.controller.salvaFatorUpscale, 4))
        self.btn8x.clicked.connect(partial(self.controller.salvaFatorUpscale, 8))
        self.btnVoltarInicio.clicked.connect(self.controller.voltarHomepage)
        self.btnProcessaImg.clicked.connect(self.controller.processarImagem)
        self.btnPreviaProcessada.clicked.connect(self.controller.abrirPrevia)
        self.btnReprocessar.clicked.connect(self.controller.reprocessar)
        self.btnSalvar.clicked.connect(self.controller.salvarImagem)
        self.btnVoltarAg.clicked.connect(self.controller.voltarHomepage)
