# coding: utf-8
#
#   controller.py
#   Objetivo:       Módulo que consiste em concentrar o fluxo da aplicação.
#   Autores:        Caroline, Daniel, Leonardo e Paloma
#   Contato:        tcc.ccp48@gmail.com
#   Data:           15/09/2021


# Imports necessários
import os
import sys
import PIL
from PyQt5.QtWidgets import QApplication, QFileDialog

from models.model import *
from views.forms import FormApp
from utils.utilsNeuralNetwork import *


class Controller:

    def __init__(self) -> None:
        """
        Método construtor da classe Controller.
        :return: None
        """
        self.app = QApplication(sys.argv)
        self.form = FormApp(self)
        self.modelo = constroi_modelo(fatorUpscale=8, canais=1)
        self.fatorRedimensionamento = 1


    def main(self) -> None:
        """
        Método onde se concentra as principais ações do app para manter o loop de processos.
        :return: None
        """
        self.form.show()
        sys.exit(self.app.exec_())
    

    def iniciaUpload(self) -> None:
        """
        Método que disponibiliza ao usuário realizar o upload da imagem a ser trabalhada.
        :return: None
        """
        
        try:
            # Parametrizando o QFileDialog
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog

            # Abrindo a tela de upload e recuperando o caminho da imagem
            caminhoImg, _ = QFileDialog.getOpenFileName(
                    None,
                    "Carregar Imagem",
                    "",
                    "Todos os arquivos(*);;Arquivos de imagem(*.jpg *.png)",
                    options=options
            )

            # Verificando se o usuário escolheu uma imagem válida
            extensaoCaminhoImg: str = caminhoImg[caminhoImg.find("."):]
            if caminhoImg == "" or extensaoCaminhoImg not in [".jpg", ".jpeg", ".png"]:
                return

            # Novo objeto de Imagem sendo instanciado
            self.imgOriginal = Imagem(caminhoImg)

            # Mudando a página para opções de upload e configurando previa
            self.form.configuraPrevia(self.form.btnPreviaImg, self.imgOriginal.caminhoImg)
            self.form.configuraDadosUpload(self.imgOriginal)
            self.form.stckPrincipal.setCurrentWidget(self.form.pgUpload)


        except Exception as e:
            print(e)

    
    def mudouPadraoImpressao(self, template: TipoTemplate) -> None:
        """
        Método que é disparado pelos botões 'Papel' e 'Foto'; para alterar o conteúdo da ComboBox.
        :param template: TipoTemplate que será aplicado no cmbBox.
        :return: None
        """
        # Alterando o template da imagem
        self.imgOriginal.tipoTemplate = template.padrao()
        
        # Configurando as informações na tela
        self.form.configuraDadosUpload(self.imgOriginal)
        


    def mudouTamanhoImpressao(self) -> None:
        """
        Método que é disparado pela mudança de index do combo box de templates, isto é, o usuário escolheu outro template (ex: mudou de A0 para A5).
        :return: None
        """
        tamanhoAtual = self.form.cmbTamanhoImpressao.currentText()

        try:
            if tamanhoAtual != "":
                # Coletando o template que está sendo usado atualmente pelo usuário
                templateUtilizado = self.imgOriginal.tipoTemplate

                # Coletando o template que o usuário quis alterar
                novoTemplate = templateUtilizado.fromString(tamanhoAtual)

                # Alterando o tamanho do template da imagem
                self.imgOriginal.template = novoTemplate.value

                # Configurando novas informações na tela
                self.form.atualizaDadosUpload(self.imgOriginal)

        except Exception as e:
            print(e)
        

    def salvaFatorUpscale(self, fator: int) -> None:
        """
        Método para salvar o fator a ser utilizado no possível redimensionamento.
        :param fator: inteiro que representa o fator.
        :return: None
        """
        self.fatorRedimensionamento = fator


    def processarImagem(self) -> None:
        """
        Método que processa a imagem via rede neural.
        :return: None
        """
        # Processando a imagem via rede neural
        imgProcessada = conversor_alta_resolucao(
                self.modelo, 
                self.imgOriginal.img,
                self.fatorRedimensionamento
        )

        # Criando objeto de tipo Imagem
        self.imgProcessada = Imagem(img=imgProcessada)
        
        templateOriginal: TipoTemplate = self.imgOriginal.tipoTemplate
        self.imgProcessada.tipoTemplate = templateOriginal

        extensaoImgOriginal: str = self.imgOriginal.extensao
        self.imgProcessada.salvar(extensao=extensaoImgOriginal)

        # Mostrando tela de reprocessamento
        self.form.configuraImgPrevia(self.imgOriginal, self.imgProcessada)

    
    def abrirPrevia(self) -> None:
        """
        Método que abre a prévia da imagem processada, via aplicativo definido pelo SO.
        OBS: Não funciona no Unix.
        :return: None
        """
        # os.startfile(self.imgProcessada.caminhoImg)
        pass


    def salvarImagem(self) -> None:
        """
        Método para salvar a imagem de acordo com o caminho passado pelo usuário.
        :return: None
        """
        try:
            # Parametrizando o QFileDialog
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog

            # Abrindo a tela para salvar a imagem
            caminhoSalvarImg, _ = QFileDialog.getSaveFileName(
                    None,
                    "Salvar Imagem",
                    "",
                    "Todos os arquivos(*);;Arquivos de imagem(*.jpg *.png)",
                    options=options
            )
            
            self.imgProcessada.caminhoImg = caminhoSalvarImg
            self.imgProcessada.salvar()
            print("Salvou imagem!")

            # Configurando extensão
            # extensaoImgOriginal: str = self.imgOriginal.extensao


        except Exception as e:
            print(e)
