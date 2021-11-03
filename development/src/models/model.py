# coding: utf-8
#
#   model.py
#   Objetivo:       Módulo que agrupa os objetos que são manipulados ao decorrer da aplicação.
#   Autores:        Caroline, Daniel, Leonardo e Paloma
#   Contato:        tcc.ccp48@gmail.com
#   Data:           15/09/2021


# Imports necessários
import os
import PIL.Image
from enum import Enum
from math import ceil


class Imagem:
    """
    Classe que representa uma imagem a ser processada pela rede neural ou que já foi processada.
    """

    def __init__(self, caminhoImg="", img=None) -> None:
        """
        Método construtor da classe Imagem.
        :param caminhoImg: opcional; str que representa o caminho da imagem a ser/já processada.
        :return: None
        """
        # Inicializando atributos
        self.__resolveImagem(caminhoImg, img)

        # Atributos da imagem, provenientes de PIL.Image ou calculados
        self.__largura: int = self.__img.size[0]
        self.__altura: int = self.__img.size[1]
        self.__totalPx: int = self.altura * self.largura

        # Atributos calculados, referentes ao DPI
        self.__tipoTemplate: TipoTemplate = TemplatePapel.A5
        self.__template: float = max(self.__tipoTemplate.value)
        self.__ppi: int = self.__calculaPPI()


    @property
    def caminhoImg(self) -> str:
        """ Getter do atributo caminhoImg. """
        return self.__caminhoImg
    

    @caminhoImg.setter
    def caminhoImg(self, cmImg: str) -> None:
        """ Setter do atributo caminhoImg. """
        self.__caminhoImg = cmImg
    
    
    @property
    def extensao(self) -> str:
        """ Getter do atributo extensao. """
        return self.__extensao


    @property
    def img(self) -> PIL.Image.Image:
        """ Getter do atributo img. """
        return self.__img


    @img.setter
    def img(self, imgParam: PIL.Image.Image) -> None:
        """ Setter do parâmetro img. """
        self.__img = imgParam


    @property
    def largura(self) -> int:
        """ Getter do atributo largura. """
        return self.__largura


    @property
    def altura(self) -> int:
        """ Getter do atributo altura. """
        return self.__altura


    @property
    def totalPx(self) -> int:
        """ Getter do atributo totalPx. """
        return self.__totalPx


    @property
    def tipoTemplate(self):
        """ Getter do atributo tipoTemplate. """
        return self.__tipoTemplate

    
    @tipoTemplate.setter
    def tipoTemplate(self, template) -> None:
        """ Setter do atributo tipoTemplate. """
        self.__tipoTemplate = template
        self.__template = max(template.value)
        self.__ppi = self.__calculaPPI()


    @property
    def template(self) -> float:
        """ Getter do atributo template. """
        return self.__template


    @template.setter
    def template(self, tmp) -> None:
       """ Setter do atributo template. """
       self.__template = max(tmp)
       self.__ppi = self.__calculaPPI()

    
    @property
    def ppi(self) -> int:
        """ Getter do atributo ppi. """
        return self.__ppi

    
    def salvar(self, extensao="") -> None:
        """
        Método para salvar a imagem no computador.
        Se não houver caminho específico, salvar na pasta tmp/ do projeto.
        :param extensao: opcional, str que indica a extensão em qual o usuário deseja salvar a imagem.
        :return: None
        """
        # Se caminhoImg for nulo, então foi proveniente da rede neural. Salvar em tmp
        if self.caminhoImg == "":
            nomeImg: str = f"tempImg{extensao}"
            self.caminhoImg = os.path.join(os.getcwd(), "tmp", nomeImg)

        # Salvando a imagem
        self.img.save(self.caminhoImg)

    
    def __calculaPPI(self) -> int:
        """
        Método que calcula o valor de Pixels Per Inch da imagem, dado um template utilizado (que pode variar)
        :return: pixels por polegada, sempre arrendodados, representando o PPI para aquele template.
        """ 
        # Tamanho padrão de conversão entre polegadas e mm
        polegadaEmMM: float = 25.4
        
        # Independente do template, utilizar sempre o valor máximo dentre largura e altura
        tamanho = max(self.largura, self.altura)

        # Se o template escolhido for de tipo Papel, então não será necessária a conversão (mudando o valor de polegadaEmMM para 1)
        if type(self.tipoTemplate) == TemplateFoto:
            polegadaEmMM = 1

        # Cálculo ppi
        ppi = tamanho * polegadaEmMM / self.__template
        return ceil(ppi)


    def __resolveImagem(self, caminhoImg="", img=None) -> None:
        """
        Método que auxilia a construção do objeto, ou seja, resolve se o objeto deve ser construído via caminho da imagem ou via imagem já pronta.
        :param caminhoImg: str que representa o caminho absoluto da imagem.
        :param img: PIL.Image.Image que pode (ou não) ser a imagem já construída
        :return: None
        """
        # Se passado o caminho, abrir a imagem em formato PIL.Image
        if caminhoImg != "":
            self.__caminhoImg = caminhoImg
            self.__extensao = caminhoImg[caminhoImg.find("."):]
            self.__img = PIL.Image.open(self.__caminhoImg)

        # Se passada a imagem (exemplo: já processada pela rede), apenas salvá-la
        elif isinstance(img, PIL.Image.Image):
            self.__caminhoImg = ""
            self.__extensao = ""
            self.__img = img

        # Se não passado nem caminho nem imagem válida, estourar uma exceção
        else:
            raise AttributeError("O parâmetro passado no construtor da classe Imagem não é válido")




class TipoTemplate(Enum):
    """ Classe de tipo enum base para diferenciar tamanhos de impressão entre foto e papel."""

    def toString(self) -> str:
        """
        Método que será implementado pelas classes concretas de papel e foto.
        Ao ter os membros definidos (para tamanhos de papel ou polegada), este método transforma o enum em uma str, que será adicionada ao ComboBox de tamanhos de impressão.
        """
        return ""
    

    @classmethod
    def fromString(cls, strMembro: str):
        """
        Método que, a partir de uma string, retorna o membro correspondente àquela str.
        :param strMembro: str que representa aquele tipo de template passado (proveniente da ComboBox da tela de upload).
        :return: um dos membros da classe concreta implementada.
        """
        # Iteração sobre cada membro da classe
        for membro in cls:

            # Se o membro (em str, a partir do método toString) for igual à str passada, então o membro requerido foi encontrado.
            if strMembro == membro.toString():
                return membro

        raise NameError(f"String passada para {cls}.fromString não é válida!")


    @classmethod
    def listaMembros(cls) -> list:
        """
        Método de classe onde o retorno será uma lista de strings devidamente formatadas através do método toString.
        :return: lista de str, como ["A0 - 841x1189 mm", "A1 - 594x841 mm", ...] ou ["2R - 2.5x3.5", ...]
        """
        listaResultado: list = []

        for membro in cls:
            strMembro: str = membro.toString()
            listaResultado.append(strMembro)
    
        return listaResultado


    @classmethod
    def padrao(cls):
        """
        Método que sempre retornará o padrão utilizado para cada uma das classes que herdarão de TipoTemplate.
        """
        pass
    



class TemplatePapel(TipoTemplate):
    """
    Classe que herda de TipoTemplate e que tem como seus membros os tamanhos de impressão para Papel (A0, A1, ..., A10), sempre dado em mm.
    Padrão para esta classe: A5
    """

    A0 = (841, 1189)
    A1 = (594, 841)
    A2 = (420, 594)
    A3 = (297, 420)
    A4 = (210, 297)
    A5 = (148, 210)
    A6 = (105, 148)
    A7 = (74, 105)
    A8 = (52, 74)
    A9 = (37, 52)
    A10 = (26, 37)


    def toString(self) -> str:
        """
        Função herdada de TipoTemplate que, ao receber uma das enums de Papel listadas, converte a mesma para uma str. 
        A finalidade da função é facilitar a escrita dos membros na ComboBox, onde o usuário poderá escolher o tamanho que deseja.
        :param self: um dos membros da classe
        :return: str do membro. Ex: "A0 - 841x1189 mm"
        """
        # Coletando nome e tamanhos
        nome: str = self.name
        tam1, tam2 = self.value
        unidade: str = "mm"

        # Construção da str final
        strMembro: str = f"{nome} - {tam1}x{tam2} {unidade}"
        return strMembro


    @classmethod
    def padrao(cls):
        """ Simples método que retorna o padrão para esta classe, que é o padrão A5. """
        return cls.A5




class TemplateFoto(TipoTemplate):
    """
    Classe que herda de TipoTemplate e que tem como seus membros os tamanhos de impressão para foto (2R, 3R, ..., 10R), sempre dado em mm.
    Padrão para esta classe: A5
    """

    IN_2R = (2.5, 3.5)
    IN_3R = (3.5, 5)
    IN_4R = (4, 6)
    IN_5R = (5, 7)
    IN_6R = (6, 8)
    IN_8R = (8, 10)
    IN_S8R = (8, 12)
    IN_10R = (10, 12)


    def toString(self) -> str:
        """
        Função herdada de TipoTemplate que, ao receber uma das enums de Foto listadas, converte a mesma para uma str. 
        A finalidade da função é facilitar a escrita dos membros na ComboBox, onde o usuário poderá escolher o tamanho que deseja.
        :param self: um dos membros da classe
        :return: str do membro. Ex: "2R - 2.5x3.5 in"
        """
        # Coletando nome e tamanhos
        nome: str = self.name.replace("IN_", "")
        tam1, tam2 = self.value
        unidade: str = "in"

        # Construção da str final
        strMembro: str = f"{nome} - {tam1}x{tam2} {unidade}"
        return strMembro


    @classmethod
    def padrao(cls):
        """ Simples método que retorna o padrão para esta classe, que é o padrão 5R. """
        return cls.IN_5R

