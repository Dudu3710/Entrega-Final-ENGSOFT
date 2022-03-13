from tkinter import *
import tkinter
from controlador import Controlador
import numpy as np
#from jogador import Jogador

from time import sleep

class Interface():
    def __init__(self) -> None:
        self._janela = Tk()
        self._partidaEncerrada = False
        self._controlador = self._controlador = Controlador('', '')
        self._botaoApertado = ''
        self._mainFrame = Frame(self._janela,width=520,height=420, bg="white")
        self._buttonFrame = Frame(self._janela,width=520,height=100,bg='green')
        self._mensagem = Frame(self._janela,width=520,height=70, bg="lightgrey")
        self._vazio = PhotoImage(file = "jogoHobbes/jogoHobbes/implementacao/imagens/vazio.png")
        self._rei_1_d = PhotoImage(file = "jogoHobbes/jogoHobbes/implementacao/imagens/rei_1_direita.png")
        self._rei_1_e = PhotoImage(file = "jogoHobbes/jogoHobbes/implementacao/imagens/rei_1_esquerda.png")
        self._rei_1_b = PhotoImage(file = "jogoHobbes/jogoHobbes/implementacao/imagens/rei_1_baixo.png")
        self._rei_1_c = PhotoImage(file = "jogoHobbes/jogoHobbes/implementacao/imagens/rei_1_cima.png")
        self._rei_2_d = PhotoImage(file = "jogoHobbes/jogoHobbes/implementacao/imagens/rei_2_direita.png")
        self._rei_2_e = PhotoImage(file = "jogoHobbes/jogoHobbes/implementacao/imagens/rei_2_esquerda.png")
        self._rei_2_b = PhotoImage(file = "jogoHobbes/jogoHobbes/implementacao/imagens/rei_2_baixo.png")
        self._rei_2_c = PhotoImage(file = "jogoHobbes/jogoHobbes/implementacao/imagens/rei_2_cima.png")
        self._peao = PhotoImage(file = "jogoHobbes/jogoHobbes/implementacao/imagens/peao.png")
        self.fillMainWindow()

    def fillMainWindow(self):
        self._janela.title("UM PEGA-PEGA ENTRE REIS")
        self._janela.iconbitmap("jogoHobbes/jogoHobbes/implementacao/imagens/coroa_icon.ico")
        self._janela.geometry("770x730")
        self._janela.resizable(False, False)
        self._janela["bg"]="lightgrey"

            
        #MENSAGEM DO DUDU ->
        #estou com problemas em importar as imagens!!! --- amanha eu vou conseguir resolver
        #entendi tambem como funciona as labels e frames vai ser bem tranquilo
        #so fiquei com duvida nesse mainloop() mas vou ver ele amanha tambem !!
        #a interface e o controlador estao se comunicando certinho ta ficando lindo



        #vazio = PhotoImage(file = "jogoHobbes/jogoHobbes/implementacao/imagens/vazio.png")
        #pyimage1
        #rei_1_d = PhotoImage(file = "jogoHobbes/jogoHobbes/implementacao/imagens/rei_1_baixo.png")
        #rei_1_e = PhotoImage(file = "jogoHobbes/jogoHobbes/implementacao/imagens/rei_1_esquerda.png")
        #rei_1_b = PhotoImage(file = "jogoHobbes/jogoHobbes/implementacao/imagens/rei_1_baixo.png")
        #rei_1_c = PhotoImage(file = "jogoHobbes/jogoHobbes/implementacao/imagens/rei_1_cima.png")
        #pyimage2
        #rei_2_d = PhotoImage(file = "jogoHobbes/jogoHobbes/implementacao/imagens/rei_2_direita.png")
        #rei_2_e = PhotoImage(file = "jogoHobbes/jogoHobbes/implementacao/imagens/rei_2_esquerda.png")
        #rei_2_b = PhotoImage(file = "jogoHobbes/jogoHobbes/implementacao/imagens/rei_1_baixo.png")
        #rei_2_c = PhotoImage(file = "jogoHobbes/jogoHobbes/implementacao/imagens/rei_1_cima.png")
        #pyimage3
        #peao = PhotoImage(file = "jogoHobbes/jogoHobbes/implementacao/imagens/peao.png")
        #pyimage4

        #self.atualizaInterface(self.vazio,self.rei_1,self.rei_1,self.peao,self._mainFrame)

        
        #self.atualizaInterface(self.vazio,self.rei_1,self.rei_2,self.peao,self._mainFrame)
        self._mainFrame.place(x=110,y=200)
        self._buttonFrame.place(x=200, y=13)
        self._mensagem.place(x=185,y=120)

        #labelInstrucao = Label(self._mensagem, text='Hobbes: um pega-pega entre reis' , font="Courier 21")
        #labelInstrucao.grid(row=0, column=0)
        

        #apenas um teste !!! mudar depois para iniciar somente quando o botao de iniciar for apertado
        #self._controlador.preencherTabuleiro()
        botao_iniciar = Button(self._buttonFrame,text = "INICIAR",height = 4,width = 15,command=lambda:self.iniciar_jogo(''))
        botao_desistir = Button(self._buttonFrame,text = "DESISTIR",height = 4,width = 15,command='')
        botao_sair_jogo = Button(self._buttonFrame,text = "SAIR DO JOGO",height = 4,width = 15,command='')
        botao_iniciar.grid(row= 0, column=0)
        botao_desistir.grid(row= 0, column=1)
        botao_sair_jogo.grid(row= 0, column=2)

        #realizar jogada
        self._janela.bind('w', lambda event: self.atualizaInterface('w'))
        self._janela.bind('a', lambda event: self.atualizaInterface('a'))
        self._janela.bind('s', lambda event: self.atualizaInterface('s'))
        self._janela.bind('d', lambda event: self.atualizaInterface('d'))
        self._janela.bind('e', lambda event: self.atualizaInterface('e'))
        self._janela.bind('p', lambda event: self.atualizaInterface('p'))

        #teste
        #self._controlador.setPartidaAndamento()
        #self.atualizaInterface(vazio,rei_1,rei_2,peao,self._mainFrame)
        self._janela.mainloop()

    def iniciar_jogo(self,acao):
        if self._controlador.getPartidaAndamento() == False:
            self._controlador.setPartidaAndamento(True)
            self.atualizaInterface(acao)

    def atualiza_imagem_rei(self,direcao,jogador):
        if jogador == 1:
            if direcao == 'cima':
                return self._rei_1_c
            elif direcao == 'baixo':
                return self._rei_1_b
            elif direcao == 'direita':
                return self._rei_1_d
            else:
                return self._rei_1_e

        else:
            if direcao == 'cima':
                return self._rei_2_c
            elif direcao == 'baixo':
                return self._rei_2_b
            elif direcao == 'direita':
                return self._rei_2_d
            else:
                return self._rei_2_e

    def atualizaInterface(self,acao):
        if self._controlador.getPartidaAndamento():
            self._controlador.verificarAcao(acao)
            labelInstrucao = Label(self._mensagem, text='                    ' , font="Courier 21",bg = "lightgrey")
            labelInstrucao.grid(row=0, column=0)

            if (acao == 'e' or acao == 'p') and (self._controlador.getFlagJogada() == False):
                labelInstrucao = Label(self._mensagem, text='Jogada inválida' , font="Courier 21")
                labelInstrucao.grid(row=0, column=0)

            if self._controlador.getPartidaEncerrada():
                if self._controlador._jogadorDaVez == 1:
                    texto = 'Jogador dourado venceu!'
                else:
                    texto = 'Jogador prata venceu!'
                labelInstrucao = Label(self._mensagem, text=texto , font="Courier 21")
                labelInstrucao.grid(row=0, column=0)


            print(self._controlador.getJogadorDaVez())
            print(self._controlador.getDirecaoJogadorDaVez())
            print(np.matrix(self._controlador.getPosicoesTabuleiro()))
            
            for y in range(5):
                for x in range(5):
                    if self._controlador.getPosicoesTabuleiro() [x][y] == 0:
                        labelvazio = Label(self._mainFrame, bd = 2, relief="solid", image = self._vazio)
                        xLabel = labelvazio
                    elif self._controlador.getPosicoesTabuleiro()  [x][y] == 3:
                        labelPeao = Label(self._mainFrame, bd = 2, relief="solid", image = self._peao)
                        xLabel = labelPeao
                    elif self._controlador.getPosicoesTabuleiro()  [x][y] == 1:

                        imagem_r1 = self.atualiza_imagem_rei(self._controlador.getDirecaoJogador1(),1)
                        print(imagem_r1)
                        labelReiUm = Label(self._mainFrame, bd = 2, relief="solid", image = imagem_r1)
                        xLabel = labelReiUm
                    else:
                        imagem_r2 = self.atualiza_imagem_rei(self._controlador.getDirecaoJogador2(),2)
                        print(imagem_r2)
                        labelReiDois = Label(self._mainFrame, bd = 2, relief="solid", image = imagem_r2)
                        xLabel = labelReiDois



                    xLabel.grid(row=x , column=y)


interface = Interface()

