from tabuleiro import Tabuleiro
import random

class Controlador():
    def __init__(self, nomeJodadorUm:str, nomeJogadorDois:str) -> None:
        self._tabuleiro = Tabuleiro(nomeJodadorUm=nomeJodadorUm, nomeJogadorDois=nomeJogadorDois)
        self._jogadorDaVez = random.randint(1, 2)
        self._partidaAndamento = False
        self._acao = ''
        self._partidaEncerrada = False
        self._vencedores = []
        self._jogadaObrigatoriaRealizada = False

    def preencherTabuleiro(self):
        pass

    def definirJogadorDaVez(self):
        pass

    def informarPartidaAndamento(self):
        pass

    def verificarAcao(self):
        pass

    def getDirecaoJogadorDaVez(self):
        pass

    def moverRei(self):
        pass

    def mudarDirecaoRei(self):
        pass

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
        pass
