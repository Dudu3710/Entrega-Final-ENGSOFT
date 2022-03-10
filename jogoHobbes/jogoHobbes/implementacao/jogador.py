class Jogador():
    def __init__(self, id:int, nome:str, turno:bool, direcaoAtual:str) -> None:
        self._id = id
        self._turno = turno
        self._direcaoAtual = direcaoAtual

    def mudarDirecaoJogador(self, direcao):
        self._direcaoAtual = direcao

    def getposicao(self):
        return self.posicao

    def setposicao(self,pos):
        self.posicao = pos

    def getDirecaoAtual(self):
        return self._direcaoAtual
