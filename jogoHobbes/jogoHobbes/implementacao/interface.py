from tkinter import *
from controlador import Controlador
#from jogador import Jogador

from time import sleep

class Interface():
    def __init__(self) -> None:
        self._janela = Tk()
        #self._labelVazio = Label()
        #self._labelReiUm = Label()
        #self._labelReiDois = Label()
        #self._labelPeao = Label()
        self._mainFrame = Frame()
        self._mensagem = Frame()
        self._primeiroNome = ''
        self._segundoNome = ''
        self._partidaEncerrada = False
        self._controlador = Controlador(nomeJodadorUm=self._primeiroNome, nomeJogadorDois=self._segundoNome)
        self._botaoApertado = ''

        
        #self.matriz_inic = [[0,3,2,3,0], #tirar, todas elas vem do controlador
        #                   [0,3,3,3,0],
        #                    [0,0,0,0,0],
        #                    [0,3,3,3,0],
        #                    [0,3,1,3,0]]
                            
        #self.jogador_1 = Jogador(1, True, 'baixo') # tirar
        #self.jogador_2 = Jogador(2, False, 'cima') # tirar

        self._mainFrame = Frame(self._janela, padx=5, pady=5, bg="dark grey")
        self._mensagem = Frame(self._janela, padx=0, pady=0, bg="lightgreen")
        self.fillMainWindow()

    def fillMainWindow(self):
        self._janela.title("UM PEGA-PEGA ENTRE REIS")
        #self._janela.iconbitmap("imagens/coroa_icon.ico")
        self._janela.geometry("750x630")
        self._janela.resizable(False, False)
        self._janela["bg"]="lightgrey"

            
        #MENSAGEM DO DUDU ->
        #estou com problemas em importar as imagens!!! --- amanha eu vou conseguir resolver
        #entendi tambem como funciona as labels e frames vai ser bem tranquilo
        #so fiquei com duvida nesse mainloop() mas vou ver ele amanha tambem !!
        #a interface e o controlador estao se comunicando certinho ta ficando lindo



        #self.vazio = PhotoImage(file = "imagens/vazio.png")
        #pyimage1
        #self.rei_1 = PhotoImage(file = "imagens/rei_1.png")
        #pyimage2
        #self.rei_2 = PhotoImage(file = "imagens/rei_2.png")
        #pyimage3
        #self.peao = PhotoImage(file = "imagens/peao.png")
        #pyimage4


        labelInstrucao = Label(self._mainFrame, bg="lightgrey", text='Hobbes: um pega-pega entre reis' , font="Courier 20").place(x = 250 , y = 30)
        
        #self.atualiza_tabuleiro(self.vazio,self.rei_1,self.rei_2,self.peao,self._mainFrame)

        #labelInstrucao.grid(row=0, column=0)
        self._mainFrame.grid(row=2,column=0,pady=10)
        self._mensagem.grid(row=1,column=0,pady = 20)
        
        self.rei_1Turn = True

        #apenas um teste !!! mudar depois para iniciar somente quando o botao de iniciar for apertado
        self._controlador.preencherTabuleiro()

        #realizar jogada
        self._janela.bind('w', lambda event: self._controlador.verificarAcao('w'))
        self._janela.bind('a', lambda event: self._controlador.verificarAcao('a'))
        self._janela.bind('s', lambda event: self._controlador.verificarAcao('s'))
        self._janela.bind('d', lambda event: self._controlador.verificarAcao('d'))
        self._janela.bind('e', lambda event: self._controlador.verificarAcao('e'))
        self._janela.bind('p', lambda event: self._controlador.verificarAcao('p'))
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
        for y in range(5):
            for x in range(5):
                if self._controlador.getPosicoesTabuleiro() [x][y] == 0:
                    self._labelPeao = Label(mainFrame, bd = 2, relief="solid", image = vazio)
                    xLabel = self._labelPeao
                elif self._controlador.getPosicoesTabuleiro()  [x][y] == 3:
                    self._labelPeao = Label(mainFrame, bd = 2, relief="solid", image = peao)
                    xLabel = self._labelPeao
                elif self._controlador.getPosicoesTabuleiro()  [x][y] == 2:
                    self._labelReiUm = Label(mainFrame, bd = 2, relief="solid", image = rei_1)
                    xLabel = self._labelReiUm
                else:
                    self._labelReiDois = Label(mainFrame, bd = 2, relief="solid", image = rei_2)
                    xLabel = self._labelReiDois



                xLabel.grid(row=x , column=y)


Interface()