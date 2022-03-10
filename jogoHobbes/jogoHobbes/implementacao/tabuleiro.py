
from jogador import Jogador


class Tabuleiro():
    def __init__(self, nomeJodadorUm:str, nomeJogadorDois:str) -> None:
        #self._matrizPosicoes = [[0 for x in range(5)] for y in range(5)] 
        self._matrizPosicoes = None
        self._jogadorUm = None
        self._jogadorDois = None
        self._vencedores = []
        self._posicaoPeca = []
        self._haPeao = False
        self._traseiraVazia = False
        self._dianteiraVazia = False
        self._posicaoJogadorUm = False
        self._posicaoJogadorDois = False
        self._reiPosicoesAdjacentes = []
        self._jogadorOposto = 2
        self._x_oposto = 0
        self._y_oposto = 0

    def moverPeca(self,jogador,direcao):
        self._posicaoPeca = self.verificarPosicao(jogador)
        direcao_livre = self.verificarDirecaoLivre(self._posicaoPeca,direcao)

        if direcao_livre:
            pass

    def verificarPosicao(self,jogador):
        pass #implementado no vpp mas terei q sair

    def verificarDirecaoLivre(self):
        pass

    def atualizarMatrizPosicoes(self):
        pass

    def mudarDirecaoPeca(self,jogador,direcao):
        if jogador == 1:
            self._jogadorUm.mudarDirecaoJogador(direcao)
        else:
            self._jogadorDois.mudarDirecaoJogador(direcao)



    def getDirecaoJogadorDaVez(self,jogador_da_vez):

        if jogador_da_vez == 1:
            return self._jogadorUm.getDirecaoAtual()
        else:
            return self._jogadorDois.getDirecaoAtual()
            
        

    def verificarPeaoDirecao(self):
        pass

    def verificarTraseiraJogador(self):
        pass

    def verificarDianteiraPeao(self):
        pass

    def armazenarPosicoesJogadores(self):
        pass

    def verificarPosicoesAdjacentes(self):
        pass

    def verificarPosicoesAcima(self):
        pass

    def verificarPosicoesDireita(self):
        pass

    def verificarPosicoesAbaixo(self):
        pass

    def verificarPosicoesEsquerda(self):
        pass

    def definirMatrizPosicoes(self):
        self._matrizPosicoes =[[0,3,2,3,0],
                               [0,3,3,3,0],
                               [0,0,0,0,0],
                               [0,3,3,3,0],
                               [0,3,1,3,0]]

    def criarTabuleiro(self):
        self._jogadorUm = Jogador(id=1, nome='nomeJodadorUm', turno=True, direcaoAtual='baixo')
        self._jogadorDois = Jogador(id=2, nome='nomeJogadorDois', turno=False, direcaoAtual='cima') #arrumar nome jogadores 
        self.definirMatrizPosicoes()

    def verificarEncerramentoDaPartida(self):
        pass 

    def getMatrizPosicoes(self):
        return self._matrizPosicoes   

