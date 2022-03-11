
from jogador import Jogador


class Tabuleiro():
    def __init__(self) -> None:
        self._matrizPosicoes = None
        self._jogadorUm = None
        self._jogadorDois = None
        self._vencedores = []
        
    def criarTabuleiro(self):
        self._jogadorUm = Jogador(id=1, posicao = [0, 2], direcaoAtual='baixo')
        self._jogadorDois = Jogador(id=2, posicao = [4, 2], direcaoAtual='cima')
        self._matrizPosicoes =[[0,3,2,3,0],
                               [0,3,3,3,0],
                               [0,0,0,0,0],
                               [0,3,3,3,0],
                               [0,3,1,3,0]]

    def getDirecaoJogadorDaVez(self, jogador):
        if jogador == 1:
            return self._jogadorUm.getDirecaoJogador()
        else:
            return self._jogadorDois.getDirecaoJogador()

    def moverPeca(self, jogador, direcao):
        if jogador == 1:
            posicaoPeca = self._jogadorUm._posicao
        else:
            posicaoPeca = self._jogadorDois._posicao

        direcaoLivre = self.verificarDirecaoLivre(posicaoPeca, direcao)

        if direcaoLivre:
            self.atualizarMatrizPosicoes(posicaoPeca, direcao, jogador)

    def verificarDirecaoLivre(self, posicaoPeca, direcao):
        x, y = posicaoPeca

        if direcao == 'cima':
            if x == 0 or self._matrizPosicoes[x-1][y] != 0:
                return False

        elif direcao == 'direita':
            if x == 4 or self._matrizPosicoes[x][y-1] != 0:
                return False

        elif direcao == 'baixo':
            if x == 4 or self._matrizPosicoes[x+1][y] != 0:
                return False

        elif direcao == 'esquerda':
            if y == 0 or self._matrizPosicoes[x][y+1] != 0:
                return False

        return True

    def atualizarMatrizPosicoes(self, posicaoPeca, direcao, jogador):
        x, y = posicaoPeca

        if jogador == 1:
            if direcao == 'cima':
                self._matrizPosicoes[x+1][y] = jogador
                self._jogadorUm._posicao = [x+1, y]
            elif direcao == 'direita':
                self._matrizPosicoes[x][y+1] = jogador
                self._jogadorUm._posicao = [x][y+1]
            elif direcao == 'baixo':
                self._matrizPosicoes[x+1][y] = jogador
                self._jogadorUm._posicao = [x+1][y]
            elif direcao == 'esquerda':
                self._matrizPosicoes[x][y-1] = jogador
                self._jogadorUm._posicao = [x][y-1]
        else:
            if direcao == 'cima':
                self._matrizPosicoes[x+1][y] = jogador
                self._jogadorDois._posicao = [x+1, y]
            elif direcao == 'direita':
                self._matrizPosicoes[x][y+1] = jogador
                self._jogadorDois._posicao = [x][y+1]
            elif direcao == 'baixo':
                self._matrizPosicoes[x+1][y] = jogador
                self._jogadorDois._posicao = [x+1][y]
            elif direcao == 'esquerda':
                self._matrizPosicoes[x][y-1] = jogador
                self._jogadorDois._posicao = [x][y-1]

        self._matrizPosicoes[x][y] = 0

    def mudarDirecaoPeca(self, jogador, direcao):
        if jogador == 1:
            self._jogadorUm.mudarDirecaoJogador(direcao)
        else:
            self._jogadorDois.mudarDirecaoJogador(direcao)

    def puxarPeao(self, jogador, direcao):
        if jogador == 1:
            posicaoPeca = self._jogadorUm._posicao
        else:
            posicaoPeca = self._jogadorDois._posicao

        haPeao, posicaoPeao = self.verificarPeaoDirecao(posicaoPeca, direcao)

        if haPeao:
            traseiraVazia = self.verificarTraseiraJogador(posicaoPeca, direcao)

            if direcao == 'cima':
                direcaoNova = 'baixo'
            elif direcao == 'direita':
                direcaoNova = 'esquerda'
            elif direcao == 'esquerda':
                direcaoNova = 'direita'
            else:
                direcaoNova = 'cima'

            if traseiraVazia:
                #atualizando a posicao do rei na matriz para recuar
                self.atualizarMatrizPosicoes(posicaoPeca, direcaoNova, jogador)
                #atualizando a posicao do peao para recuar
                self.atualizarMatrizPosicoes(posicaoPeao, direcaoNova, 3)

    def verificarPeaoDirecao(self, posicaoPeca, direcao):
        x, y = posicaoPeca

        if direcao == 'cima':
            if x == 0 or self._matrizPosicoes[x-1][y] != 3:
                posicaoPeao = [x-1, y]
                return False, posicaoPeao

        elif direcao == 'direita':
            if x == 4 or self._matrizPosicoes[x][y-1] != 3:
                posicaoPeao = [x, y-1]
                return False, posicaoPeao

        elif direcao == 'baixo':
            if x == 4 or self._matrizPosicoes[x+1][y] != 3:
                posicaoPeao = [x+1, y]
                return False, posicaoPeao

        elif direcao == 'esquerda':
            if y == 0 or self._matrizPosicoes[x][y+1] != 3:
                posicaoPeao = [x, y+1]
                return False, posicaoPeao

        return True, posicaoPeao

    def verificarTraseiraJogador(self, posicaoPeca, direcao):
        x, y = posicaoPeca

        if direcao == 'cima':
            if x == 0 or self._matrizPosicoes[x+1][y] != 0:
                return False

        elif direcao == 'direita':
            if x == 4 or self._matrizPosicoes[x][y+1] != 0:
                return False

        elif direcao == 'baixo':
            if x == 4 or self._matrizPosicoes[x-1][y] != 0:
                return False

        elif direcao == 'esquerda':
            if y == 0 or self._matrizPosicoes[x][y-1] != 0:
                return False

        return True

    def empurrarPeao(self, jogador, direcao):
        if jogador == 1:
            posicaoPeca = self._jogadorUm._posicao
        else:
            posicaoPeca = self._jogadorDois._posicao

        haPeao, posicaoPeao = self.verificarPeaoDirecao(posicaoPeca, direcao)

        if haPeao:
            dianteiraVazia = self.verificarDirecaoLivre(posicaoPeao, direcao)

            if dianteiraVazia:
                #atualizando a posicao do rei na matriz para recuar
                self.atualizarMatrizPosicoes(posicaoPeao, direcao, 3)
                #atualizando a posicao do peao para recuar
                self.atualizarMatrizPosicoes(posicaoPeca, direcao, jogador)
    
    def verificarEncerramentoDaPartida(self, jogador):
        reiPosicoesAdjacentes = self.verificarPosicoesAdjacentes(jogador)
        
        if reiPosicoesAdjacentes:
            self._vencedores.append(jogador)
        else:
            impedido = self.verificarPosicoesAcima(self._jogadorUm._posicao)

            if impedido:
                impedido = self.verificarPosicoesDireita(self._jogadorUm._posicao)

                if impedido:
                    impedido = self.verificarPosicoesAbaixo(self._jogadorUm._posicao)

                    if impedido:
                        impedido = self.verificarPosicoesEsquerda(self._jogadorDois._posicao)

                        if impedido:
                            self._vencedores.append(2)

            impedido = self.verificarPosicoesAcima(self._jogadorDois._posicao)

            if impedido:
                impedido = self.verificarPosicoesDireita(self._jogadorDois._posicao)

                if impedido:
                    impedido = self.verificarPosicoesAbaixo(self._jogadorDois._posicao)

                    if impedido:
                        impedido = self.verificarPosicoesEsquerda(self._jogadorDois._posicao)

                        if impedido:
                            self._vencedores.append(1)

    def verificarPosicoesAdjacentes(self, jogador):
        if jogador == 1:
            jogadorOposto = 2
            x, y = self._jogadorUm._posicao
        else:
            jogadorOposto = 1
            x, y = self._jogadorDois._posicao

        for x in range(len(self._matrizPosicoes)):
            for y in range(len(self._matrizPosicoes[x])):
                if self._matrizPosicoes[x][y] == jogadorOposto:
                    x_oposto = x
                    y_oposto = y

        if (x_oposto == x-1 and y_oposto == y) or (x_oposto == x+1 and y_oposto == y) or (x_oposto == x and y_oposto == y+1) or (x_oposto == x and y_oposto == y-1):
            return True
        else:
            return False

    def verificarPosicoesAcima(self, posicao):
        x, y = posicao

        if x == 0:
            return True
        elif x == 1:
            if not self._matrizPosicoes[x-1][y] != 0:
                return False
        else:
            if not (self._matrizPosicoes[x-1][y] != 0 and self._matrizPosicoes[x-2][y] != 0):
                return False
        return True

    def verificarPosicoesDireita(self, posicao):
        x, y = posicao

        if y == 4:
            return True
        elif y == 3:
            if not self._matrizPosicoes[x][y+1] != 0:
                return False
        else:
            if not (self._matrizPosicoes[x][y+1] != 0 and self._matrizPosicoes[x][y+2] != 0):
                return False
        return True

    def verificarPosicoesAbaixo(self, posicao):
        x, y = posicao

        if x == 4:
            return True
        elif x == 3:
            if not self._matrizPosicoes[x+1][y] != 0:
                return False
        else:
            if not (self._matrizPosicoes[x+1][y] != 0 and self._matrizPosicoes[x+2][y] != 0):
                return False
        return True

    def verificarPosicoesEsquerda(self, posicao):
        x, y = posicao

        if y == 0:
            return True
        elif y == 1:
            if not self._matrizPosicoes[x][y-1] != 0:
                return False
        else:
            if not (self._matrizPosicoes[x][y-1] != 0 and self._matrizPosicoes[x][y-2] != 0):
                return False
        return True

    def getVencedores(self):
        return self._vencedores
