
from tabuleiro import Tabuleiro
import random

class Controlador():
    def __init__(self, nomeJodadorUm:str, nomeJogadorDois:str) -> None:
        self._tabuleiro = Tabuleiro(nomeJodadorUm=nomeJodadorUm, nomeJogadorDois=nomeJogadorDois)
        self._jogadorDaVez = None
        self._partidaAndamento = False
        self._acao = ''
        self._partidaEncerrada = False
        self._vencedores = []
        self._jogadaObrigatoriaRealizada = False
        self.preencherTabuleiro()
        self.definirJogadorDaVez()

    def preencherTabuleiro(self):
        self._tabuleiro.criarTabuleiro()

    def definirJogadorDaVez(self):
        self._jogadorDaVez = random.randint(1, 2)

    def informarPartidaAndamento(self):
        return self._partidaAndamento

    def verificarAcao(self,input):
        self._acao = input
        #direcao = self.getDirecaoJogadorDaVez()
        direcao = "direita"

        #jogada opcional
        if (self._acao == "cima") or(self._acao == "direita") or (self._acao == "esquerda") or (self._acao == "baixo"):
            #seta aponta para mesma direcao do movimento
            if self._acao == direcao:
                self.moverRei(self._jogadorDaVez,direcao)
            else:
                self.mudarDirecaoRei(self._jogadorDaVez,direcao)

        

        #jogada obrigatoria
        else:
            print("entreri aq")


    def getDirecaoJogadorDaVez(self):
        return self._tabuleiro.getDirecaoJogadorDaVez(self.getQualJogador())

    def moverRei(self,jogador,direcao):
        self._tabuleiro.moverPeca()

    def mudarDirecaoRei(self,jogador,direcao):
        self._tabuleiro.mudarDirecaoPeca(jogador,direcao)

    def mudarJogadorDaVez(self):
        pass

    def puxarPeao(self):
        pass

    def empurrarPeao(self):
        pass

    def verificarVencedores(self):
        pass

    def getVencedores(self):
        pass

    def getQualJogador(self):
        return self._jogadorDaVez

cont = Controlador("a","b")
cont.verificarAcao("direita")
