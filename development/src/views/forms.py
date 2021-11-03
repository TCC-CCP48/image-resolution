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



def mostraMensagemErro(erro: str) -> None:
    """
    Função para mostrar uma determinada mensagem de erro ao usuário.
    """
    caixaMensagem = QtWidgets.QMessageBox()
    caixaMensagem.setIcon(QtWidgets.QMessageBox.Critical)
    caixaMensagem.setWindowTitle("Erro")
    caixaMensagem.setText(erro)
    caixaMensagem.exec_()


def mostraMensagemSucesso(msg: str) -> None:
    """
    Função para mostrar uma determinada mensagem de sucesso ao usuário.
    """
    caixaMensagem = QtWidgets.QMessageBox()
    caixaMensagem.setIcon(QtWidgets.QMessageBox.Information)
    caixaMensagem.setWindowTitle("Sucesso")
    caixaMensagem.setText(msg)
    caixaMensagem.exec_()


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
        self.frmIconeTitulo.setMinimumSize(QtCore.QSize(300, 0))
        self.frmIconeTitulo.setMaximumSize(QtCore.QSize(512, 16777215))
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
        spacerItem1 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem1)
        self.lblSlogan = QtWidgets.QLabel(self.frmIconeTitulo)
        self.lblSlogan.setAlignment(QtCore.Qt.AlignCenter)
        self.lblSlogan.setWordWrap(True)
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
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.frmUpload)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem3)
        self.frmEsqProcessamento = QtWidgets.QFrame(self.frmUpload)
        self.frmEsqProcessamento.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frmEsqProcessamento.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frmEsqProcessamento.setObjectName("frmEsqProcessamento")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frmEsqProcessamento)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.btnPreviaImg = QtWidgets.QPushButton(self.frmEsqProcessamento)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnPreviaImg.sizePolicy().hasHeightForWidth())
        self.btnPreviaImg.setSizePolicy(sizePolicy)
        self.btnPreviaImg.setMinimumSize(QtCore.QSize(300, 0))
        self.btnPreviaImg.setMaximumSize(QtCore.QSize(400, 300))
        self.btnPreviaImg.setText("")
        self.btnPreviaImg.setIconSize(QtCore.QSize(300, 300))
        self.btnPreviaImg.setObjectName("btnPreviaImg")
        self.verticalLayout_5.addWidget(self.btnPreviaImg)
        self.frmConfigTemplate = QtWidgets.QFrame(self.frmEsqProcessamento)
        self.frmConfigTemplate.setStyleSheet(self._estilo_frm_secundario)
        self.frmConfigTemplate.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frmConfigTemplate.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frmConfigTemplate.setObjectName("frmConfigTemplate")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frmConfigTemplate)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, -1)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.frmInfoTemplate = QtWidgets.QFrame(self.frmConfigTemplate)
        self.frmInfoTemplate.setMaximumSize(QtCore.QSize(16777215, 61))
        self.frmInfoTemplate.setStyleSheet("background-color: #4a4a4a;")
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
        self.verticalLayout_5.addWidget(self.frmConfigTemplate)
        self.frmBtnVoltar_PgProcessamento = QtWidgets.QFrame(self.frmEsqProcessamento)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frmBtnVoltar_PgProcessamento.sizePolicy().hasHeightForWidth())
        self.frmBtnVoltar_PgProcessamento.setSizePolicy(sizePolicy)
        self.frmBtnVoltar_PgProcessamento.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frmBtnVoltar_PgProcessamento.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frmBtnVoltar_PgProcessamento.setObjectName("frmBtnVoltar_PgProcessamento")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frmBtnVoltar_PgProcessamento)
        self.horizontalLayout_3.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btnVoltarInicio = QtWidgets.QPushButton(self.frmBtnVoltar_PgProcessamento)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnVoltarInicio.sizePolicy().hasHeightForWidth())
        self.btnVoltarInicio.setSizePolicy(sizePolicy)
        self.btnVoltarInicio.setMinimumSize(QtCore.QSize(0, 50))
        self.btnVoltarInicio.setMaximumSize(QtCore.QSize(1000, 50))
        self.btnVoltarInicio.setStyleSheet(self._estilo_btn_desfoque)
        self.btnVoltarInicio.setObjectName("btnVoltarInicio")
        self.horizontalLayout_3.addWidget(self.btnVoltarInicio)
        self.verticalLayout_5.addWidget(self.frmBtnVoltar_PgProcessamento)
        self.horizontalLayout_18.addWidget(self.frmEsqProcessamento)
        self.frmDirProcessamento = QtWidgets.QFrame(self.frmUpload)
        self.frmDirProcessamento.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frmDirProcessamento.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frmDirProcessamento.setObjectName("frmDirProcessamento")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frmDirProcessamento)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frmConfigImg = QtWidgets.QFrame(self.frmDirProcessamento)
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
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frmInfoNomeResPPI)
        self.verticalLayout_10.setContentsMargins(20, -1, 20, -1)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.lblInfoNomeImg = QtWidgets.QLabel(self.frmInfoNomeResPPI)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblInfoNomeImg.sizePolicy().hasHeightForWidth())
        self.lblInfoNomeImg.setSizePolicy(sizePolicy)
        self.lblInfoNomeImg.setObjectName("lblInfoNomeImg")
        self.verticalLayout_10.addWidget(self.lblInfoNomeImg)
        self.lblInfoResolucaoImg = QtWidgets.QLabel(self.frmInfoNomeResPPI)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblInfoResolucaoImg.sizePolicy().hasHeightForWidth())
        self.lblInfoResolucaoImg.setSizePolicy(sizePolicy)
        self.lblInfoResolucaoImg.setObjectName("lblInfoResolucaoImg")
        self.verticalLayout_10.addWidget(self.lblInfoResolucaoImg)
        self.lblInfoPPIImagem = QtWidgets.QLabel(self.frmInfoNomeResPPI)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblInfoPPIImagem.sizePolicy().hasHeightForWidth())
        self.lblInfoPPIImagem.setSizePolicy(sizePolicy)
        self.lblInfoPPIImagem.setObjectName("lblInfoPPIImagem")
        self.verticalLayout_10.addWidget(self.lblInfoPPIImagem)
        self.lblInfoResolucaoImgSaida = QtWidgets.QLabel(self.frmInfoNomeResPPI)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblInfoResolucaoImgSaida.sizePolicy().hasHeightForWidth())
        self.lblInfoResolucaoImgSaida.setSizePolicy(sizePolicy)
        self.lblInfoResolucaoImgSaida.setObjectName("lblInfoResolucaoImgSaida")
        self.verticalLayout_10.addWidget(self.lblInfoResolucaoImgSaida)
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
        self.frmInfoTituloFator.setStyleSheet("background-color: #4a4a4a;")
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
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.frmBtnFatores)
        self.verticalLayout_11.setContentsMargins(20, -1, 20, -1)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.btn2x = QtWidgets.QPushButton(self.frmBtnFatores)
        self.btn2x.setMaximumSize(QtCore.QSize(16777215, 30))
        self.btn2x.setStyleSheet(self._estilo_btn_desfoque)
        self.btn2x.setObjectName("btn2x")
        self.verticalLayout_11.addWidget(self.btn2x)
        self.btn4x = QtWidgets.QPushButton(self.frmBtnFatores)
        self.btn4x.setMaximumSize(QtCore.QSize(16777215, 30))
        self.btn4x.setStyleSheet(self._estilo_btn_desfoque)
        self.btn4x.setObjectName("btn4x")
        self.verticalLayout_11.addWidget(self.btn4x)
        self.btn8x = QtWidgets.QPushButton(self.frmBtnFatores)
        self.btn8x.setMaximumSize(QtCore.QSize(16777215, 30))
        self.btn8x.setStyleSheet(self._estilo_btn_clicado)
        self.btn8x.setObjectName("btn8x")
        self.verticalLayout_11.addWidget(self.btn8x)
        self.verticalLayout_9.addWidget(self.frmBtnFatores)
        self.verticalLayout_7.addWidget(self.frmConfigImg)
        self.frmBtnProcessar_PgProcessamento = QtWidgets.QFrame(self.frmDirProcessamento)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frmBtnProcessar_PgProcessamento.sizePolicy().hasHeightForWidth())
        self.frmBtnProcessar_PgProcessamento.setSizePolicy(sizePolicy)
        self.frmBtnProcessar_PgProcessamento.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frmBtnProcessar_PgProcessamento.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frmBtnProcessar_PgProcessamento.setObjectName("frmBtnProcessar_PgProcessamento")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frmBtnProcessar_PgProcessamento)
        self.horizontalLayout_9.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.btnProcessaImg = QtWidgets.QPushButton(self.frmBtnProcessar_PgProcessamento)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnProcessaImg.sizePolicy().hasHeightForWidth())
        self.btnProcessaImg.setSizePolicy(sizePolicy)
        self.btnProcessaImg.setMinimumSize(QtCore.QSize(0, 50))
        self.btnProcessaImg.setMaximumSize(QtCore.QSize(1000, 50))
        self.btnProcessaImg.setStyleSheet(self._estilo_btn_destaque)
        self.btnProcessaImg.setObjectName("btnProcessaImg")
        self.horizontalLayout_9.addWidget(self.btnProcessaImg)
        self.verticalLayout_7.addWidget(self.frmBtnProcessar_PgProcessamento)
        self.horizontalLayout_18.addWidget(self.frmDirProcessamento)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem4)
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
        self.horizontalLayout_27 = QtWidgets.QHBoxLayout(self.frmDecisao)
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_27.setSpacing(0)
        self.horizontalLayout_27.setObjectName("horizontalLayout_27")
        spacerItem5 = QtWidgets.QSpacerItem(150, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_27.addItem(spacerItem5)
        self.frmReprocessamento = QtWidgets.QFrame(self.frmDecisao)
        self.frmReprocessamento.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frmReprocessamento.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frmReprocessamento.setObjectName("frmReprocessamento")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout(self.frmReprocessamento)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.frmReprocessamentoGeral = QtWidgets.QFrame(self.frmReprocessamento)
        self.frmReprocessamentoGeral.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frmReprocessamentoGeral.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frmReprocessamentoGeral.setObjectName("frmReprocessamentoGeral")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.frmReprocessamentoGeral)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.frmEsqReprocessamento = QtWidgets.QFrame(self.frmReprocessamentoGeral)
        self.frmEsqReprocessamento.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frmEsqReprocessamento.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frmEsqReprocessamento.setObjectName("frmEsqReprocessamento")
        self.verticalLayout_22 = QtWidgets.QVBoxLayout(self.frmEsqReprocessamento)
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.btnPreviaImgProcessada = QtWidgets.QPushButton(self.frmEsqReprocessamento)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnPreviaImgProcessada.sizePolicy().hasHeightForWidth())
        self.btnPreviaImgProcessada.setSizePolicy(sizePolicy)
        self.btnPreviaImgProcessada.setMinimumSize(QtCore.QSize(300, 300))
        self.btnPreviaImgProcessada.setText("")
        self.btnPreviaImgProcessada.setIconSize(QtCore.QSize(300, 300))
        self.btnPreviaImgProcessada.setObjectName("btnPreviaImgProcessada")
        self.verticalLayout_22.addWidget(self.btnPreviaImgProcessada)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_22.addItem(spacerItem6)
        self.btnPreviaProcessada = QtWidgets.QPushButton(self.frmEsqReprocessamento)
        self.btnPreviaProcessada.setMinimumSize(QtCore.QSize(0, 30))
        self.btnPreviaProcessada.setStyleSheet(self._estilo_btn_desfoque)
        self.btnPreviaProcessada.setObjectName("btnPreviaProcessada")
        self.verticalLayout_22.addWidget(self.btnPreviaProcessada)
        self.horizontalLayout_14.addWidget(self.frmEsqReprocessamento)
        self.frmDirReprocessamento = QtWidgets.QFrame(self.frmReprocessamentoGeral)
        self.frmDirReprocessamento.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frmDirReprocessamento.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frmDirReprocessamento.setObjectName("frmDirReprocessamento")
        self.verticalLayout_23 = QtWidgets.QVBoxLayout(self.frmDirReprocessamento)
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.frmComparacao = QtWidgets.QFrame(self.frmDirReprocessamento)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frmComparacao.sizePolicy().hasHeightForWidth())
        self.frmComparacao.setSizePolicy(sizePolicy)
        self.frmComparacao.setMinimumSize(QtCore.QSize(300, 0))
        self.frmComparacao.setMaximumSize(QtCore.QSize(600, 500))
        self.frmComparacao.setStyleSheet(self._estilo_frm_secundario)
        self.frmComparacao.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frmComparacao.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frmComparacao.setObjectName("frmComparacao")
        self.verticalLayout_24 = QtWidgets.QVBoxLayout(self.frmComparacao)
        self.verticalLayout_24.setContentsMargins(0, 0, 0, -1)
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.frmInfoImgProcessada = QtWidgets.QFrame(self.frmComparacao)
        self.frmInfoImgProcessada.setMaximumSize(QtCore.QSize(16777215, 61))
        self.frmInfoImgProcessada.setStyleSheet("background-color: #4a4a4a;")
        self.frmInfoImgProcessada.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frmInfoImgProcessada.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frmInfoImgProcessada.setObjectName("frmInfoImgProcessada")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.frmInfoImgProcessada)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.lblTituloDetalhesProcessada = QtWidgets.QLabel(self.frmInfoImgProcessada)
        self.lblTituloDetalhesProcessada.setObjectName("lblTituloDetalhesProcessada")
        self.horizontalLayout_19.addWidget(self.lblTituloDetalhesProcessada)
        self.verticalLayout_24.addWidget(self.frmInfoImgProcessada)
        self.frmComparacaoOriginalProcessada = QtWidgets.QFrame(self.frmComparacao)
        self.frmComparacaoOriginalProcessada.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frmComparacaoOriginalProcessada.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frmComparacaoOriginalProcessada.setObjectName("frmComparacaoOriginalProcessada")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout(self.frmComparacaoOriginalProcessada)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
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
        self.verticalLayout_25 = QtWidgets.QVBoxLayout(self.frmNomeResPPIProcessadaInfo)
        self.verticalLayout_25.setContentsMargins(20, -1, 20, -1)
        self.verticalLayout_25.setObjectName("verticalLayout_25")
        self.lblNomeImgProcessadaInfo = QtWidgets.QLabel(self.frmNomeResPPIProcessadaInfo)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblNomeImgProcessadaInfo.sizePolicy().hasHeightForWidth())
        self.lblNomeImgProcessadaInfo.setSizePolicy(sizePolicy)
        self.lblNomeImgProcessadaInfo.setObjectName("lblNomeImgProcessadaInfo")
        self.verticalLayout_25.addWidget(self.lblNomeImgProcessadaInfo)
        self.lblPPIImagemProcessadaInfo = QtWidgets.QLabel(self.frmNomeResPPIProcessadaInfo)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblPPIImagemProcessadaInfo.sizePolicy().hasHeightForWidth())
        self.lblPPIImagemProcessadaInfo.setSizePolicy(sizePolicy)
        self.lblPPIImagemProcessadaInfo.setObjectName("lblPPIImagemProcessadaInfo")
        self.verticalLayout_25.addWidget(self.lblPPIImagemProcessadaInfo)
        self.horizontalLayout_20.addWidget(self.frmNomeResPPIProcessadaInfo)
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
        self.verticalLayout_26 = QtWidgets.QVBoxLayout(self.frmNomeResPPIProcessada)
        self.verticalLayout_26.setContentsMargins(20, -1, 20, -1)
        self.verticalLayout_26.setObjectName("verticalLayout_26")
        self.lblNomeImgProcessada = QtWidgets.QLabel(self.frmNomeResPPIProcessada)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblNomeImgProcessada.sizePolicy().hasHeightForWidth())
        self.lblNomeImgProcessada.setSizePolicy(sizePolicy)
        self.lblNomeImgProcessada.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblNomeImgProcessada.setObjectName("lblNomeImgProcessada")
        self.verticalLayout_26.addWidget(self.lblNomeImgProcessada)
        self.lblTemplateImagemProcessada = QtWidgets.QLabel(self.frmNomeResPPIProcessada)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblTemplateImagemProcessada.sizePolicy().hasHeightForWidth())
        self.lblTemplateImagemProcessada.setSizePolicy(sizePolicy)
        self.lblTemplateImagemProcessada.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblTemplateImagemProcessada.setObjectName("lblTemplateImagemProcessada")
        self.verticalLayout_26.addWidget(self.lblTemplateImagemProcessada)
        self.horizontalLayout_20.addWidget(self.frmNomeResPPIProcessada)
        self.verticalLayout_24.addWidget(self.frmComparacaoOriginalProcessada)
        self.frmInfoComparacao = QtWidgets.QFrame(self.frmComparacao)
        self.frmInfoComparacao.setMaximumSize(QtCore.QSize(16777215, 61))
        self.frmInfoComparacao.setStyleSheet(self._estilo_frm_titulo_quadrado)
        self.frmInfoComparacao.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frmInfoComparacao.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frmInfoComparacao.setObjectName("frmInfoComparacao")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout(self.frmInfoComparacao)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.lblDetalhesImgOriginal = QtWidgets.QLabel(self.frmInfoComparacao)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblDetalhesImgOriginal.sizePolicy().hasHeightForWidth())
        self.lblDetalhesImgOriginal.setSizePolicy(sizePolicy)
        self.lblDetalhesImgOriginal.setObjectName("lblDetalhesImgOriginal")
        self.horizontalLayout_21.addWidget(self.lblDetalhesImgOriginal)
        self.lblDetalhesImgProcessada = QtWidgets.QLabel(self.frmInfoComparacao)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblDetalhesImgProcessada.sizePolicy().hasHeightForWidth())
        self.lblDetalhesImgProcessada.setSizePolicy(sizePolicy)
        self.lblDetalhesImgProcessada.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblDetalhesImgProcessada.setObjectName("lblDetalhesImgProcessada")
        self.horizontalLayout_21.addWidget(self.lblDetalhesImgProcessada)
        self.verticalLayout_24.addWidget(self.frmInfoComparacao)
        self.frmDetalhesComparacao = QtWidgets.QFrame(self.frmComparacao)
        self.frmDetalhesComparacao.setStyleSheet(self._estilo_frm_titulo_quadrado)
        self.frmDetalhesComparacao.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frmDetalhesComparacao.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frmDetalhesComparacao.setObjectName("frmDetalhesComparacao")
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout(self.frmDetalhesComparacao)
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.frmDetalhesImgOriginal = QtWidgets.QFrame(self.frmDetalhesComparacao)
        self.frmDetalhesImgOriginal.setStyleSheet(self._estilo_frm_secundario_quadrado)
        self.frmDetalhesImgOriginal.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frmDetalhesImgOriginal.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frmDetalhesImgOriginal.setObjectName("frmDetalhesImgOriginal")
        self.verticalLayout_27 = QtWidgets.QVBoxLayout(self.frmDetalhesImgOriginal)
        self.verticalLayout_27.setContentsMargins(20, -1, 20, -1)
        self.verticalLayout_27.setObjectName("verticalLayout_27")
        self.lblDetalhesImgOriginalPPI = QtWidgets.QLabel(self.frmDetalhesImgOriginal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblDetalhesImgOriginalPPI.sizePolicy().hasHeightForWidth())
        self.lblDetalhesImgOriginalPPI.setSizePolicy(sizePolicy)
        self.lblDetalhesImgOriginalPPI.setObjectName("lblDetalhesImgOriginalPPI")
        self.verticalLayout_27.addWidget(self.lblDetalhesImgOriginalPPI)
        self.lblDetalhesImgOriginalRes = QtWidgets.QLabel(self.frmDetalhesImgOriginal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblDetalhesImgOriginalRes.sizePolicy().hasHeightForWidth())
        self.lblDetalhesImgOriginalRes.setSizePolicy(sizePolicy)
        self.lblDetalhesImgOriginalRes.setObjectName("lblDetalhesImgOriginalRes")
        self.verticalLayout_27.addWidget(self.lblDetalhesImgOriginalRes)
        self.horizontalLayout_22.addWidget(self.frmDetalhesImgOriginal)
        self.frmDetalhesImgProcessada = QtWidgets.QFrame(self.frmDetalhesComparacao)
        self.frmDetalhesImgProcessada.setStyleSheet(self._estilo_frm_secundario_quadrado)
        self.frmDetalhesImgProcessada.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frmDetalhesImgProcessada.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frmDetalhesImgProcessada.setObjectName("frmDetalhesImgProcessada")
        self.verticalLayout_28 = QtWidgets.QVBoxLayout(self.frmDetalhesImgProcessada)
        self.verticalLayout_28.setContentsMargins(20, -1, 20, -1)
        self.verticalLayout_28.setObjectName("verticalLayout_28")
        self.lblDetalhesImgProcessadaPPI = QtWidgets.QLabel(self.frmDetalhesImgProcessada)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblDetalhesImgProcessadaPPI.sizePolicy().hasHeightForWidth())
        self.lblDetalhesImgProcessadaPPI.setSizePolicy(sizePolicy)
        self.lblDetalhesImgProcessadaPPI.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblDetalhesImgProcessadaPPI.setObjectName("lblDetalhesImgProcessadaPPI")
        self.verticalLayout_28.addWidget(self.lblDetalhesImgProcessadaPPI)
        self.lblDetalhesImgProcessadaRes = QtWidgets.QLabel(self.frmDetalhesImgProcessada)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblDetalhesImgProcessadaRes.sizePolicy().hasHeightForWidth())
        self.lblDetalhesImgProcessadaRes.setSizePolicy(sizePolicy)
        self.lblDetalhesImgProcessadaRes.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblDetalhesImgProcessadaRes.setObjectName("lblDetalhesImgProcessadaRes")
        self.verticalLayout_28.addWidget(self.lblDetalhesImgProcessadaRes)
        self.horizontalLayout_22.addWidget(self.frmDetalhesImgProcessada)
        self.verticalLayout_24.addWidget(self.frmDetalhesComparacao)
        self.verticalLayout_23.addWidget(self.frmComparacao)
        self.horizontalLayout_14.addWidget(self.frmDirReprocessamento)
        self.verticalLayout_21.addWidget(self.frmReprocessamentoGeral)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_21.addItem(spacerItem7)
        self.frmInfoSalvarReprocessar = QtWidgets.QFrame(self.frmReprocessamento)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frmInfoSalvarReprocessar.sizePolicy().hasHeightForWidth())
        self.frmInfoSalvarReprocessar.setSizePolicy(sizePolicy)
        self.frmInfoSalvarReprocessar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frmInfoSalvarReprocessar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frmInfoSalvarReprocessar.setObjectName("frmInfoSalvarReprocessar")
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout(self.frmInfoSalvarReprocessar)
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.lblInfoSalvarReprocessar = QtWidgets.QLabel(self.frmInfoSalvarReprocessar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblInfoSalvarReprocessar.sizePolicy().hasHeightForWidth())
        self.lblInfoSalvarReprocessar.setSizePolicy(sizePolicy)
        self.lblInfoSalvarReprocessar.setAlignment(QtCore.Qt.AlignCenter)
        self.lblInfoSalvarReprocessar.setWordWrap(True)
        self.lblInfoSalvarReprocessar.setObjectName("lblInfoSalvarReprocessar")
        self.horizontalLayout_23.addWidget(self.lblInfoSalvarReprocessar)
        self.verticalLayout_21.addWidget(self.frmInfoSalvarReprocessar)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_21.addItem(spacerItem8)
        self.frmBtnsReprocessamento = QtWidgets.QFrame(self.frmReprocessamento)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frmBtnsReprocessamento.sizePolicy().hasHeightForWidth())
        self.frmBtnsReprocessamento.setSizePolicy(sizePolicy)
        self.frmBtnsReprocessamento.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frmBtnsReprocessamento.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frmBtnsReprocessamento.setObjectName("frmBtnsReprocessamento")
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout(self.frmBtnsReprocessamento)
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.frmBtnReprocessarReprocessamento = QtWidgets.QFrame(self.frmBtnsReprocessamento)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frmBtnReprocessarReprocessamento.sizePolicy().hasHeightForWidth())
        self.frmBtnReprocessarReprocessamento.setSizePolicy(sizePolicy)
        self.frmBtnReprocessarReprocessamento.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frmBtnReprocessarReprocessamento.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frmBtnReprocessarReprocessamento.setObjectName("frmBtnReprocessarReprocessamento")
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout(self.frmBtnReprocessarReprocessamento)
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.btnReprocessar = QtWidgets.QPushButton(self.frmBtnReprocessarReprocessamento)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnReprocessar.sizePolicy().hasHeightForWidth())
        self.btnReprocessar.setSizePolicy(sizePolicy)
        self.btnReprocessar.setMinimumSize(QtCore.QSize(0, 50))
        self.btnReprocessar.setMaximumSize(QtCore.QSize(1000, 50))
        self.btnReprocessar.setStyleSheet(self._estilo_btn_desfoque)
        self.btnReprocessar.setObjectName("btnReprocessar")
        self.horizontalLayout_25.addWidget(self.btnReprocessar)
        self.horizontalLayout_24.addWidget(self.frmBtnReprocessarReprocessamento)
        self.frmBtnSalvarReprocessamento = QtWidgets.QFrame(self.frmBtnsReprocessamento)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frmBtnSalvarReprocessamento.sizePolicy().hasHeightForWidth())
        self.frmBtnSalvarReprocessamento.setSizePolicy(sizePolicy)
        self.frmBtnSalvarReprocessamento.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frmBtnSalvarReprocessamento.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frmBtnSalvarReprocessamento.setObjectName("frmBtnSalvarReprocessamento")
        self.horizontalLayout_26 = QtWidgets.QHBoxLayout(self.frmBtnSalvarReprocessamento)
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        self.btnSalvar = QtWidgets.QPushButton(self.frmBtnSalvarReprocessamento)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnSalvar.sizePolicy().hasHeightForWidth())
        self.btnSalvar.setSizePolicy(sizePolicy)
        self.btnSalvar.setMinimumSize(QtCore.QSize(0, 50))
        self.btnSalvar.setMaximumSize(QtCore.QSize(1000, 50))
        self.btnSalvar.setStyleSheet(self._estilo_btn_destaque)
        self.btnSalvar.setObjectName("btnSalvar")
        self.horizontalLayout_26.addWidget(self.btnSalvar)
        self.horizontalLayout_24.addWidget(self.frmBtnSalvarReprocessamento)
        self.verticalLayout_21.addWidget(self.frmBtnsReprocessamento)
        self.horizontalLayout_27.addWidget(self.frmReprocessamento)
        spacerItem9 = QtWidgets.QSpacerItem(150, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_27.addItem(spacerItem9)
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
        self.frmIconeTituloAg.setMinimumSize(QtCore.QSize(400, 0))
        self.frmIconeTituloAg.setMaximumSize(QtCore.QSize(500, 16777215))
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
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout_19.addItem(spacerItem10)
        self.lblAg1 = QtWidgets.QLabel(self.frmIconeTituloAg)
        self.lblAg1.setAlignment(QtCore.Qt.AlignCenter)
        self.lblAg1.setObjectName("lblAg1")
        self.verticalLayout_19.addWidget(self.lblAg1)
        self.lblAg2 = QtWidgets.QLabel(self.frmIconeTituloAg)
        self.lblAg2.setAlignment(QtCore.Qt.AlignCenter)
        self.lblAg2.setWordWrap(True)
        self.lblAg2.setObjectName("lblAg2")
        self.verticalLayout_19.addWidget(self.lblAg2)
        spacerItem11 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_19.addItem(spacerItem11)
        self.btnVoltarAg = QtWidgets.QPushButton(self.frmIconeTituloAg)
        self.btnVoltarAg.setMinimumSize(QtCore.QSize(0, 71))
        self.btnVoltarAg.setStyleSheet(self._estilo_btn_destaque)
        self.btnVoltarAg.setObjectName("btnVoltarAg")
        self.verticalLayout_19.addWidget(self.btnVoltarAg)
        spacerItem12 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_19.addItem(spacerItem12)
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
        self.lblSlogan.setText(_translate("App_IVision", "Aumente a resolução de suas imagens sem perder a qualidade das mesmas. Usando inteligência artificial, nós executamos a sua visão."))
        self.btnIniciar.setText(_translate("App_IVision", "Iniciar Processo"))
        self.lblTipoTamanhoImpressao.setText(_translate("App_IVision", "Padrão de Tamanho de Impressão"))
        self.btnPadraoPapel.setText(_translate("App_IVision", "Papel"))
        self.btnPadraoFoto.setText(_translate("App_IVision", "Foto"))
        self.cmbTamanhoImpressao.setItemText(0, _translate("App_IVision", "Exemplo"))
        self.btnVoltarInicio.setText(_translate("App_IVision", "Voltar"))
        self.lblTituloDetalhes.setText(_translate("App_IVision", "Detalhes da Imagem"))
        self.lblInfoNomeImg.setText(_translate("App_IVision", "Nome:"))
        self.lblInfoResolucaoImg.setText(_translate("App_IVision", "Resolução:"))
        self.lblInfoPPIImagem.setText(_translate("App_IVision", "PPI:"))
        self.lblInfoResolucaoImgSaida.setText(_translate("App_IVision", "Resolução de Saída:"))
        self.lblNomeImg.setText(_translate("App_IVision", "<Nome IMG>"))
        self.lblResolucaoImg.setText(_translate("App_IVision", "<Resolução (512x512 px)>"))
        self.lblPPIImagem.setText(_translate("App_IVision", "<Numero PPI>"))
        self.lblResolucaoImgSaida.setText(_translate("App_IVision", "<Resolução (512x512 px)>"))
        self.lblTituloFator.setText(_translate("App_IVision", "Escolha o fator de aumento"))
        self.btn2x.setText(_translate("App_IVision", "x2"))
        self.btn4x.setText(_translate("App_IVision", "x4"))
        self.btn8x.setText(_translate("App_IVision", "x8"))
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
        self.lblInfoSalvarReprocessar.setText(_translate("App_IVision", "Obrigado por usar nossa aplicação. Se a resolução estiver de seu agrado, clique em Salvar. Caso o contrário, clique em Reprocessar!"))
        self.btnReprocessar.setText(_translate("App_IVision", "Reprocessar"))
        self.btnSalvar.setText(_translate("App_IVision", "Salvar"))
        self.lblAg1.setText(_translate("App_IVision", "Obrigado por usar nossa aplicação!"))
        self.lblAg2.setText(_translate("App_IVision", "Se quiser aumentar a resolução de mais imagens, clique em Voltar ao Início."))
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





class TelaLoading(QtWidgets.QMainWindow):

    def __init__(self, mensagem: str):
        super(TelaLoading, self).__init__()
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setupUi(self)

        # Configurando lbl com a mensagem disposta
        self.lblMensagemLoading.setText(mensagem)

        # Configurando o gif de loading
        self.movie = QtGui.QMovie(CAMINHO_LOADING)
        self.lblGIFLoading.setMovie(self.movie)
        self.movie.start()


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
        self.frame.setStyleSheet("background-color: #000000; color: #EDEDED;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lblGIFLoading = QtWidgets.QLabel(self.frame)
        self.lblGIFLoading.setText("")
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

