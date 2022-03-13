
from tabuleiro import Tabuleiro
import random

class Controlador():
    def __init__(self, nomeJodadorUm:str, nomeJogadorDois:str) -> None:
        self._tabuleiro = Tabuleiro()
        self._jogadorDaVez = 0 #consistente com o diagrama de estados do controlador
        self._vencedores = []
        self._acao = ''
        self._partidaAndamento = False
        self._partidaEncerrada = False
        self._jogadaObrigatoriaRealizada = False
        self.preencherTabuleiro()   #---> acho que temos que tirar isso
        self.definirJogadorDaVez()    #---> acho que temos que tirar isso

    def preencherTabuleiro(self):
        self._tabuleiro.criarTabuleiro()

    def definirJogadorDaVez(self):
        self._jogadorDaVez = random.randint(1, 2)

    def getPartidaEncerrada(self):
        return self._partidaEncerrada

    def getPosicoesTabuleiro(self):
        return self._tabuleiro.getMatrizPosicoes()

    def getPartidaAndamento(self):
        return self._partidaAndamento

    def determinarVencedor(self):
        if self._jogadorDaVez == 1:
            self._vencedores.append(2)
        else:
            self._vencedores.append(1)

        self._partidaEncerrada = True

    def verificarAcao(self, input):
        if input == 'w':
            print('recebi acao w\n')
            self._acao = 'cima'
        elif input == 'a':
            print('recebi acao a\n')
            self._acao = 'esquerda'
        elif input == 's':
            print('recebi acao s\n')
            self._acao = 'baixo'
        elif input == 'd':
            print('recebi acao d\n')
            self._acao = 'direita'
        elif input == 'p':
            print('recebi acao p\n')
            self._acao = 'puxar'
        elif input == 'e':
            print('recebi acao e\n')
            self._acao = 'empurrar'
        else:
            self._acao = ''

        direcao = self.getDirecaoJogadorDaVez()
        #direcao = self._tabuleiro.getDirecaoJogadorDaVez(self._jogadorDaVez)

        #jogada opcional
        if (self._acao == 'cima') or(self._acao == 'direita') or (self._acao == 'esquerda') or (self._acao == 'baixo'):
            #seta aponta para mesma direcao do movimento
            if self._acao == direcao:
                self.moverRei(self._jogadorDaVez, direcao)
            else:
                direcao = self._acao
                self.mudarDirecaoRei(self._jogadorDaVez, direcao)

        #jogada obrigatoria
        elif (self._acao == 'puxar') or (self._acao == 'empurrar'):
            if self._acao == 'puxar':
                self.puxarPeao(self._jogadorDaVez, direcao)
            else:
                self.empurrarPeao(self._jogadorDaVez, direcao)
            
            self._jogadaObrigatoriaRealizada = True
        
        
            self.verificarVencedores(self._jogadorDaVez)
            vencedores = self._tabuleiro.getVencedores()

            if vencedores:
                self._partidaEncerrada = True
                print("partida encerrada")
            else:
                if self._jogadaObrigatoriaRealizada:
                    self._jogadorDaVez = self.mudarJogadorDaVez(self._jogadorDaVez)
                    self._jogadaObrigatoriaRealizada = False
        else:
            pass
        
    def getDirecaoJogadorDaVez(self):
        return self._tabuleiro.getDirecaoJogadorDaVez(self._jogadorDaVez)

    def moverRei(self, jogador, direcao):
        self._tabuleiro.moverPeca(jogador, direcao)

    def mudarDirecaoRei(self, jogador, direcao):
        self._tabuleiro.mudarDirecaoPeca(jogador, direcao)

    def puxarPeao(self, jogador, direcao):
        self._tabuleiro.puxarPeao(jogador, direcao)

    def empurrarPeao(self, jogador, direcao):
        self._tabuleiro.empurrarPeao(jogador, direcao)

    def verificarVencedores(self, jogador):
        self._tabuleiro.verificarEncerramentoDaPartida(jogador)

    def mudarJogadorDaVez(self, jogador):
        if jogador == 1:
            return 2
        else:
            return 1

    def getVencedores(self):
        return self._vencedores()

    def setPartidaAndamento(self,partida_iniciada):
        self._partidaAndamento = partida_iniciada

    def getJogadorDaVez(self):
        return self._jogadorDaVez

