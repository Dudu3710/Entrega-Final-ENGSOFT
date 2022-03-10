from tkinter import *
from controlador import Controlador
from jogador import Jogador

from time import sleep

class Interface():
    def __init__(self) -> None:
        self._janela = Tk()
        self._labelVazio = Label()
        self._labelReiUm = Label()
        self._labelReiDois = Label()
        self._labelPeao = Label()
        self._mainFrame = Frame()
        self._mensagem = Frame()
        self._primeiroNome = ''
        self._segundoNome = ''
        self._partidaEncerrada = False
        self._controlador = Controlador(nomeJodadorUm=self._primeiroNome, nomeJogadorDois=self._segundoNome)
        self._botaoApertado = ''

        
        self.matriz_inic = [[0,3,2,3,0], #tirar, todas elas vem do controlador
                            [0,3,3,3,0],
                            [0,0,0,0,0],
                            [0,3,3,3,0],
                            [0,3,1,3,0]]
                            
        self.jogador_1 = Jogador(1, True, 'baixo') # tirar
        self.jogador_2 = Jogador(2, False, 'cima') # tirar

        self._mainFrame = Frame(self._janela, padx=5, pady=5, bg="dark grey")
        self._mensagem = Frame(self._janela, padx=0, pady=0, bg="lightgreen")
        self.fillMainWindow()

    def fillMainWindow(self):
        self._janela.title("UM PEGA-PEGA ENTRE REIS")
        self._janela.iconbitmap("imagens/coroa_icon.ico")
        self._janela.geometry("750x630")
        self._janela.resizable(False, False)
        self._janela["bg"]="lightgrey"

        self.vazio = PhotoImage(file = "imagens/vazio.png")
         #pyimage1
        self.rei_1 = PhotoImage(file = "imagens/rei_1.png")
        #pyimage2
        self.rei_2 = PhotoImage(file = "imagens/rei_2.png")
        #pyimage3
        self.peao = PhotoImage(file = "imagens/peao.png")
        #pyimage4


        self._labelInstrucao = Label(self._mensagem, bg="lightgrey", text='Hobbes: um pega-pega entre reis' , font="Courier 20",padx = 130,pady=0)

        self.atualiza_tabuleiro(self.vazio,self.rei_1,self.rei_2,self.peao,self._mainFrame)

        self._labelInstrucao.grid(row=0, column=0)
        self._mainFrame.grid(row=500,column=0,pady=10)
        self._mensagem.grid(row=1,column=0,pady = 20)
        
        self.rei_1Turn = True
        self._janela.bind('w', lambda event: self.input_teclado(event,self.vazio,self.rei_1,self.rei_2,self.peao))
        self._janela.bind('a', lambda event: self.input_teclado(event,self.vazio,self.rei_1,self.rei_2,self.peao))
        self._janela.bind('s', lambda event: self.input_teclado(event,self.vazio,self.rei_1,self.rei_2,self.peao))
        self._janela.bind('d', lambda event: self.input_teclado(event,self.vazio,self.rei_1,self.rei_2,self.peao))
        self._janela.mainloop()


    def input_teclado(self,event,vazio,rei_1,rei_2,peao):
        if self.jogador_1.turno == True:
            jogador_da_vez = self.jogador_1

        elif self.jogador_2.turno == True:
            jogador_da_vez = self.jogador_2

        pos = jogador_da_vez.getposicao()

        try:
            if event.char == 's' and pos[0]+1 <=5:
                self.matriz_inic[pos[0]+1][pos[1]] = jogador_da_vez.id
                self.matriz_inic[pos[0]][pos[1]] = 0
                self.atualiza_tabuleiro(vazio,rei_1,rei_2,peao,self._mainFrame)
                jogador_da_vez.setposicao((pos[0]+1,pos[1]))


            elif event.char == 'd' and pos[1]+1 <=5:
                self.matriz_inic[pos[0]][pos[1]+1] = jogador_da_vez.id
                self.matriz_inic[pos[0]][pos[1]] = 0
                self.atualiza_tabuleiro(vazio,rei_1,rei_2,peao,self._mainFrame)
                jogador_da_vez.setposicao((pos[0],pos[1]+1))


            elif event.char == 'a' and pos[1]-1 >=0:
                self.matriz_inic[pos[0]][pos[1]-1] = jogador_da_vez.id
                self.matriz_inic[pos[0]][pos[1]] = 0
                self.atualiza_tabuleiro(vazio,rei_1,rei_2,peao,self._mainFrame)
                jogador_da_vez.setposicao((pos[0],pos[1]-1))



            elif event.char == 'w' and pos[0]-1 >=0:
                self.matriz_inic[pos[0]-1][pos[1]] = jogador_da_vez.id
                self.matriz_inic[pos[0]][pos[1]] = 0
                self.atualiza_tabuleiro(vazio,rei_1,rei_2,peao,self._mainFrame)
                jogador_da_vez.setposicao((pos[0]-1,pos[1]))

            self.jogador_1._turno = not self.jogador_1._turno
            self.jogador_2._turno = not self.jogador_2._turno
        except:
            pass
            #print("nao da")

        #print(jogador_da_vez.getposicao())


    def atualiza_tabuleiro(self,vazio,rei_1,rei_2,peao,mainFrame):
        tabuleiro = []
        for y in range(5):
            coluna = []
            for x in range(5):
                if self.matriz_inic [x][y] == 0:
                    self._labelPeao = Label(mainFrame, bd = 2, relief="solid", image = vazio)
                    xLabel = self._labelPeao
                elif self.matriz_inic [x][y] == 3:
                    self._labelPeao = Label(mainFrame, bd = 2, relief="solid", image = peao)
                    xLabel = self._labelPeao
                elif self.matriz_inic [x][y] == 2:
                    self._labelReiUm = Label(mainFrame, bd = 2, relief="solid", image = rei_1)
                    xLabel = self._labelReiUm
                else:
                    self._labelReiDois = Label(mainFrame, bd = 2, relief="solid", image = rei_2)
                    xLabel = self._labelReiDois



                xLabel.grid(row=x , column=y)
                coluna.append(xLabel)
            tabuleiro.append(coluna)


Interface()