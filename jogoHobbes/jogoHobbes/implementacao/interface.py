from tkinter import *
import tkinter
from controlador import Controlador
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
        self._mensagem = Frame(self._janela,width=520,height=70, bg="red")
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



        vazio = PhotoImage(file = "jogoHobbes/jogoHobbes/implementacao/imagens/vazio.png")
        #pyimage1
        rei_1 = PhotoImage(file = "jogoHobbes/jogoHobbes/implementacao/imagens/rei_1.png")
        #pyimage2
        rei_2 = PhotoImage(file = "jogoHobbes/jogoHobbes/implementacao/imagens/rei_2.png")
        #pyimage3
        peao = PhotoImage(file = "jogoHobbes/jogoHobbes/implementacao/imagens/peao.png")
        #pyimage4

        #self.atualiza_tabuleiro(self.vazio,self.rei_1,self.rei_1,self.peao,self._mainFrame)

        
        #self.atualiza_tabuleiro(self.vazio,self.rei_1,self.rei_2,self.peao,self._mainFrame)
        self._mainFrame.place(x=110,y=200)
        self._buttonFrame.place(x=200, y=13)
        self._mensagem.place(x=110,y=120)

        labelInstrucao = Label(self._mensagem, text='Hobbes: um pega-pega entre reis' , font="Courier 21")
        labelInstrucao.grid(row=0, column=0)
        

        #apenas um teste !!! mudar depois para iniciar somente quando o botao de iniciar for apertado
        #self._controlador.preencherTabuleiro()
        botao_iniciar = Button(self._buttonFrame,text = "INICIAR",height = 4,width = 15,command=self.iniciar_jogo())
        botao_desistir = Button(self._buttonFrame,text = "DESISTIR",height = 4,width = 15,command='')
        botao_sair_jogo = Button(self._buttonFrame,text = "SAIR DO JOGO",height = 4,width = 15,command='')
        botao_iniciar.grid(row= 0, column=0)
        botao_desistir.grid(row= 0, column=1)
        botao_sair_jogo.grid(row= 0, column=2)

        #realizar jogada
        self._janela.bind('w', lambda event: self.atualiza_tabuleiro(vazio,rei_1,rei_2,peao,'w'))
        print(self._controlador.getPartidaAndamento())
        self._janela.bind('a', lambda event: self.atualiza_tabuleiro(vazio,rei_1,rei_2,peao,'a'))
        self._janela.bind('s', lambda event: self.atualiza_tabuleiro(vazio,rei_1,rei_2,peao,'s'))
        self._janela.bind('d', lambda event: self.atualiza_tabuleiro(vazio,rei_1,rei_2,peao,'d'))
        self._janela.bind('e', lambda event: self.atualiza_tabuleiro(vazio,rei_1,rei_2,peao,'e'))
        self._janela.bind('p', lambda event: self.atualiza_tabuleiro(vazio,rei_1,rei_2,peao,'p'))

        #teste
        #self._controlador.setPartidaAndamento()
        #self.atualiza_tabuleiro(vazio,rei_1,rei_2,peao,self._mainFrame)
        self._janela.mainloop()

    def iniciar_jogo(self):
        print("pq ta entrando aqui ?")
        self._controlador.setPartidaAndamento(True)

    def atualiza_tabuleiro(self,vazio,rei_1,rei_2,peao,acao):
        if self._controlador.getPartidaAndamento():

            self._controlador.verificarAcao(acao)
            print(self._controlador.getPosicoesTabuleiro())
            for y in range(5):
                for x in range(5):
                    if self._controlador.getPosicoesTabuleiro() [x][y] == 0:
                        labelvazio = Label(self._mainFrame, bd = 2, relief="solid", image = vazio)
                        xLabel = labelvazio
                    elif self._controlador.getPosicoesTabuleiro()  [x][y] == 3:
                        labelPeao = Label(self._mainFrame, bd = 2, relief="solid", image = peao)
                        xLabel = labelPeao
                    elif self._controlador.getPosicoesTabuleiro()  [x][y] == 2:
                        labelReiUm = Label(self._mainFrame, bd = 2, relief="solid", image = rei_1)
                        xLabel = labelReiUm
                    else:
                        labelReiDois = Label(self._mainFrame, bd = 2, relief="solid", image = rei_2)
                        xLabel = labelReiDois



                    xLabel.grid(row=x , column=y)


interface = Interface()