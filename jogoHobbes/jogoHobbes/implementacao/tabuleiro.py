from jogador import Jogador


class Tabuleiro():
    def __init__(self, nomeJodadorUm:str, nomeJogadorDois:str) -> None:
        self._matrizPosicoes = [[0 for x in range(5)] for y in range(5)] 
        self._jogadorUm = Jogador(id=1, nome=nomeJodadorUm, turno=True, direcaoAtual='baixo')
        self._jogadorDois = Jogador(id=2, nome=nomeJogadorDois, turno=False, direcaoAtual='cima')
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

    def moverPeca(self):
        pass

    def verificarPosicao(self):
        pass

    def verificarDirecaoLivre(self):
        pass

    def atualizarMatrizPosicoes(self):
        pass

    def mudarDirecaoPeca(self):
        pass

    def getDirecaoJogadorDaVez(self):
        pass

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
        pass

    def criarTabuleiro(self):
        pass

    def verificarEncerramentoDaPartida(self):
        pass        