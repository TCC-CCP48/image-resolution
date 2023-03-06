# coding: utf-8
#
#   controller.py
#   Objetivo:       Módulo que consiste em concentrar o fluxo da aplicação.
#   Autores:        Caroline, Daniel, Leonardo e Paloma
#   Contato:        tcc.ccp48@gmail.com
#   Data:           15/09/2021


# Imports necessários
import sys
from PyQt5.QtWidgets import QApplication, QFileDialog

from models.model import *
from views.forms import *
from utils.utilsNeuralNetwork import *

from PIL.Image import DecompressionBombError


class Controller:

    def __init__(self) -> None:
        """
        Método construtor da classe Controller.
        :return: None
        """
        self.app = QApplication(sys.argv)
        self.form = FormApp(self)
        self.modelo = constroi_modelo(fatorUpscale=8, canais=1)
        self.fatorRedimensionamento = 8


    def main(self) -> None:
        """
        Método onde se concentra as principais ações do app para manter o loop de processos.
        :return: None
        """
        self.form.show()
        self.app.exit(self.app.exec_())
    

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

            telaLoading = TelaLoading("Carregando imagem...")
            telaLoading.show()
            self.app.processEvents()

            # Verificando se o usuário escolheu uma imagem válida
            extensaoCaminhoImg: str = caminhoImg[caminhoImg.find("."):]
            if caminhoImg == "" or extensaoCaminhoImg not in [".jpg", ".jpeg", ".png"]:
                mostraMensagemErro(
                        "O arquivo passado não é valido. " +
                        "Por favor, adicione um arquivo de extensão válida (.jpg, .jpeg ou .png)."
                )
                return

            # Novo objeto de Imagem sendo instanciado
            self.imgOriginal = Imagem(caminhoImg)

            # Validando se a imagem está dentro dos requisitos
            if self.imgOriginal.totalPx > LIMITE_PX:
                mostraMensagemErro(
                    f"A imagem não pode ser processada pois possui pixels além do permitido.\n" +
                    f"Tamanho da imagem: {self.imgOriginal.largura}px x {self.imgOriginal.altura}px = {self.imgOriginal.totalPx}px\n" +  
                    f"Limite: {LIMITE_PX}px" 
                )
                return

            # Mudando a página para opções de upload e configurando previa
            self.form.configuraPrevia(self.form.btnPreviaImg, self.imgOriginal.caminhoImg)
            self.form.configuraDadosUpload(self.imgOriginal, self.fatorRedimensionamento)
            self.form.stckPrincipal.setCurrentWidget(self.form.pgUpload)

        except Exception as e:
            mostraMensagemErro(f"Um erro inesperado aconteceu {e.__class__}. Por favor, tente novamente.")

    
    def mudouPadraoImpressao(self, template: TipoTemplate) -> None:
        """
        Método que é disparado pelos botões 'Papel' e 'Foto'; para alterar o conteúdo da ComboBox.
        :param template: TipoTemplate que será aplicado no cmbBox.
        :return: None
        """
        # Alterando o template da imagem
        self.imgOriginal.tipoTemplate = template.padrao()
        
        # Configurando as informações na tela
        self.form.configuraDadosUpload(self.imgOriginal, self.fatorRedimensionamento)


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
                self.imgOriginal.tipoTemplate = novoTemplate
                self.imgOriginal.template = novoTemplate.value

                # Configurando novas informações na tela
                self.form.atualizaDadosUpload(self.imgOriginal)

        except Exception as e:
            mostraMensagemErro(f"Um erro inesperado aconteceu {e.__class__}. Por favor, tente novamente.")
        

    def salvaFatorUpscale(self, fator: int) -> None:
        """
        Método para salvar o fator a ser utilizado no possível redimensionamento.
        :param fator: inteiro que representa o fator.
        :return: None
        """
        self.fatorRedimensionamento = fator
        self.form.atualizaResSaida(self.imgOriginal, self.fatorRedimensionamento)
        self.form.configuraOpcaoFator(self.fatorRedimensionamento)


    def processarImagem(self) -> None:
        """
        Método que processa a imagem via rede neural.
        :return: None
        """

        telaLoading = TelaLoading("Processando imagem...")
        telaLoading.show()
        self.app.processEvents()
        
        try:
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

        except Exception as e:
            mostraMensagemErro(f"Um erro inesperado aconteceu {e.__class__}. Por favor, tente novamente.")


    def reprocessar(self) -> None:
        """
        Método para reprocessar a imagem na rede neural, a fim de tentar melhorar a qualidade da imagem passada.
        :return: None
        """
    
        # Mudando a página para opções de upload e configurando previa
        self.form.configuraPrevia(self.form.btnPreviaImg, self.imgOriginal.caminhoImg)
        self.form.configuraDadosUpload(self.imgOriginal, self.fatorRedimensionamento)
        self.form.stckPrincipal.setCurrentWidget(self.form.pgUpload)

    
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
            
            extensaoImgProcessada: str = self.imgOriginal.extensao

            # Abrindo a tela para salvar a imagem
            caminhoSalvarImg, _ = QFileDialog.getSaveFileName(
                    None,
                    "Salvar Imagem",
                    "",
                    "Todos os arquivos(*);;Arquivos de imagem(*.jpg *.png)",
                    options=options
            )

            telaLoading = TelaLoading("Salvando imagem...")
            telaLoading.show()
            self.app.processEvents()
            
            self.imgProcessada.caminhoImg = caminhoSalvarImg + extensaoImgProcessada
            self.imgProcessada.salvar()

            mostraMensagemSucesso("Imagem salva com sucesso!")
            
            # Mudando para a tela de agradecimento
            self.form.stckPrincipal.setCurrentWidget(self.form.pgAgradecimento)

        except Exception as e:
            mostraMensagemErro(f"Um erro inesperado aconteceu {e.__class__}. Por favor, tente novamente.")

    
    def voltarHomepage(self) -> None:
        """
        Método que volta a aplicação para a página final.
        :return: None
        """
        self.form.stckPrincipal.setCurrentWidget(self.form.pgInicial)

