from random import choice, randrange
from time import sleep
from functools import partial
from tkinter import *
from tkinter import messagebox
from Grafo import *

CORES = ['cornflower blue', 'dark slate blue', 'light sea green', 'lawn green', 'lime green', 'dark khaki', 'goldenrod',  'rosy brown', 'saddle brown', 'dark orange', 'red', 'hot pink', 'pale violet red', 'snow4', 'SlateBlue1', 'DeepSkyBlue2', 'turquoise1', 'SeaGreen1', 'OliveDrab1']

class Grafo:
    def __init__(self):
        self.janela = Tk()
        self.janela.title("CONFIGURAÇÃO")
        self.janela.geometry("+800+400")

        self.direcionado = BooleanVar(False)
        self.ponderado = BooleanVar(False)

        direcionado = Checkbutton(self.janela, text = 'Direcionado', variable = self.direcionado, offvalue = False, onvalue = True)
        ponderado = Checkbutton(self.janela, text = 'Ponderado', variable = self.ponderado, offvalue = False, onvalue = True)
        inicio = Button(self.janela, text = "Iniciar", command = self.main)

        direcionado.pack()
        ponderado.pack()
        inicio.pack()
        self.janela.mainloop()

    def main(self):
        self.janela.destroy()
        self.contador = 0
        self.select = False
        self.janela = Tk()
        self.janela.title("Grafo")
        
        self.top = Frame(self.janela)
        self.foot = Frame(self.janela)

        self.tela = Canvas(self.top, width=1280, height=700, bd=0, highlightthickness=0)
        self.tela.bind('<ButtonPress-1>', self.selecionar)
        self.grafo = Vertices(self.janela, self.tela, self.ponderado.get(), self.direcionado.get()) # Escolher se o grafo é direcionado/ponderado

        self.entrada = Entry(self.foot)
        self.butCreate = Button(self.foot, text = "Adicionar Vértice", command = self.criar, width = 17)
        self.butUpdate = Button(self.foot, text = "Adicionar Aresta", command = self.add, width = 17)
        self.butBfs = Button(self.foot, text = "BFS - Busca em Larg", command = self.bfs, width = 17)
        self.butDfs = Button(self.foot, text = "DFS - Busca em Prof", command = self.dfs, width = 17)
        self.butDijk = Button(self.foot, text = "Path Min - Dijkstra", command = self.dijkstra, width = 17)
        self.butBell = Button(self.foot, text = 'Path Min - Bellman F.', command = self.bellmanFord, width = 17)
        self.butPrim = Button(self.foot, text = 'Arv Ger Min - Prim', command = self.prim, width = 17)
        self.butKrus = Button(self.foot, text = "Arv Ger Min - Kruskal", command = self.kruskal, width = 17)
        self.butDel = Button(self.foot, text = "RESET", command = self.delete, width = 7)
        self.help = Button(self.foot, text = "HELP", command = self.ajuda, width = 7)

        self.top.pack(fill = BOTH, expand = YES)
        self.foot.pack()
        self.tela.pack(fill = BOTH, expand = YES)
        self.entrada.pack(side = 'left')
        self.butCreate.pack(side = 'left')
        self.butUpdate.pack(side = 'left')
        self.butBfs.pack(side = 'left')
        self.butDfs.pack(side = 'left')
        self.butDijk.pack(side = 'left')
        self.butBell.pack(side = 'left')
        self.butPrim.pack(side = 'left')
        self.butKrus.pack(side = 'left')
        self.butDel.pack(side = 'left')
        self.help.pack(side = 'left')

        self.janela.mainloop()

    def selecionar(self, event):
        ver = False
        for x in self.grafo.locals.keys():
            if self.estaEm((event.x, event.y), x):
                if not self.select:
                    self.select = self.grafo.locals[x]
                    self.grafo.select(self.select)
                else:
                    self.add(self.select, self.grafo.locals[x])
                    self.grafo.unselect(self.select)
                    self.select = False
                ver = True
        if not ver:
            if self.select:
                self.grafo.unselect(self.select)
                self.select = False
            if event.x <=self.tela.winfo_width() - 20 and event.y <= self.tela.winfo_height() - 20:
                self.criar(str(self.contador), (event.x, event.y))
                self.contador += 1
            

    def estaEm(self, tupla, seq):
        if tupla[0] >= seq[0] and tupla[0] <= seq[0] + 21:
            if tupla[1] >= seq[1] and tupla[1] <= seq[1] + 21:
                return True
        return False

    def criar(self, vertice = None, local = None):
        if vertice == None: self.grafo.addVertice(self.entrada.get())
        else: self.grafo.addVertice(vertice, local)
    def add(self, vertice = None, aresta = None):
        peso = None
        if vertice == None:
            if self.ponderado.get():
                try:
                    vertice, aresta, peso = self.entrada.get().split()
                except:
                    vertice, aresta = self.entrada.get().split()
                    peso = '0'
            else:
                vertice, aresta = self.entrada.get().split()
        if not self.ponderado.get():
            self.grafo.addAresta(vertice, aresta)
        else:
            if peso == None:
                if self.entrada.get().lstrip('-').isnumeric():
                    self.grafo.addAresta(vertice, aresta, int(self.entrada.get()))
                else:
                    messagebox.showwarning("PROBLEM", "Coloque o peso corretamente!")
            else:
                if peso.lstrip('-').isnumeric():
                    self.grafo.addAresta(vertice, aresta, int(peso))
                else:
                    messagebox.showwarning("PROBLEM", "Coloque o peso corretamente!")

    def bfs(self): 
        entrada = self.entrada.get()
        if self.grafo.tem(entrada):
            self.grafo.bfs(entrada)
        else:
            messagebox.showwarning("PROBLEM", "Coloque um vértice válido!")
    def dfs(self): 
        entrada = self.entrada.get()
        if self.grafo.tem(entrada):
            self.grafo.dfs(self.entrada.get())
        else:
            messagebox.showwarning("PROBLEM", "Coloque um vértice válido!")
    def dijkstra(self): 
        if self.ponderado.get(): 
            entrada = self.entrada.get()
            if self.grafo.tem(entrada):
                self.grafo.menorCaminho("dijkstra", self.entrada.get())
            else:
                messagebox.showwarning("PROBLEM", "Coloque um vértice válido!")
        else:
            messagebox.showerror("ERROR", "O grafo deve ser ponderado!")
    def bellmanFord(self): 
        if self.ponderado.get(): 
            entrada = self.entrada.get()
            if self.grafo.tem(entrada):
                self.grafo.menorCaminho("bellmanFord", self.entrada.get())
            else:
                messagebox.showwarning("PROBLEM", "Coloque um vértice válido!")
        else:
            messagebox.showerror("ERROR", "O grafo deve ser ponderado!")
    def prim(self):
        if not self.direcionado.get() and self.ponderado.get():
            entrada = self.entrada.get()
            if self.grafo.tem(entrada):
                self.grafo.prim(entrada)
            else:
                messagebox.showwarning("PROBLEM", "Coloque um vértice válido!")
        else:
            messagebox.showerror("ERROR", "O grafo não pode ser direcionado e deve ser ponderado!")
    def kruskal(self):
        if not self.direcionado.get() and self.ponderado.get():
            entrada = self.entrada.get()
            if self.grafo.tem(entrada):
                self.grafo.kruskal(entrada)
            else: self.grafo.kruskal()
        else:
            messagebox.showerror("ERROR", "O grafo não pode ser direcionado e deve ser ponderado!")
    
    def delete(self):
        self.contador = 0
        self.grafo.delete()

    def ajuda(self):
        messagebox.showinfo("AJUDA", 
        """
        Para adicionar vértices basta clicar na tela (ela pode ser redimensionada, para ficar maior!)
        Ou basta digitar o ID do vértice no Entry.
        
        Para adicionar arestas basta clicar em um vértice e depois clicar no outro (caso for ponderado, será necessário colocar o peso no Entry).
        Ou simplesmente digite no Entry 'VERTICE01 VERTICE02' se ele não for ponderado, caso contrário 'VERTICE01 VERTICE02 PESO'
        """)

class Vertices:
    def __init__(self, janela, canvas, ponderado = False, direcionado = False):
        self.lista = {}
        self.locals = {}

        self.janela = janela
        self.tela = canvas
        self.ponderado = ponderado
        self.direcionado = direcionado
        if not self.ponderado and not self.direcionado:
            self.grafo = Graph()
        elif not self.direcionado:
            self.grafo = Graph(ponderado = True)
        elif not self.ponderado:
            self.grafo = Graph(direcionado = True)
        else:
            self.grafo = Graph(ponderado = True, direcionado = True)

    def addVertice(self, id, local = None):
        if id not in self.lista:
            self.grafo.addVertice(id)
            codigo = self.tela.create_oval(0, 0, 20, 20, fill = "white")
            if local == None: self.tela.move(codigo, randrange(0,self.tela.winfo_width()-20,2), randrange(0,self.tela.winfo_height()-20,2))
            else: self.tela.move(codigo, local[0], local[1])
            coord = self.tela.coords(codigo)
            self.locals[tuple(coord[:2])] = id
            coord = tuple([(coord[x] + coord[x+2])/2 for x in range(2)])
            texto = self.tela.create_text(coord[0], coord[1], font = ("Purisa", 10), text = id)
            self.lista[id] = (codigo, texto)

    def addAresta(self, id, aresta, peso = None):
        if not self.grafo.arestaDe(id, aresta):
            if peso == None: self.grafo.addAresta(id, aresta)
            else: self.grafo.addAresta(id, aresta, peso)
            if aresta not in self.lista:
                self.addVertice(aresta)
            coord = self.tela.coords(self.lista[id][0])
            linha = tuple([(coord[x] + coord[x+2])/2 for x in range(2)])
            coord = self.tela.coords(self.lista[aresta][0])
            linha += tuple([(coord[x] + coord[x+2])/2 for x in range(2)])
            
            nova = self.tela.create_line(linha, arrow = LAST) if self.grafo.isDirecionado() else self.tela.create_line(linha)
            if peso != None:
                texto = self.tela.create_text(tuple([(linha[x] + linha[x+2])/2 for x in range(2)]), text = str(peso), font = ("Purisa", 10))
                self.lista[(id, aresta)] = (nova, texto)
            else:
                self.lista[(id, aresta)] = nova
    
    def tem(self, vertice):
        return self.grafo[vertice] != None

    def bfs(self, vertice):
        lista = self.grafo.buscaEmLargura(self.grafo[vertice])
        cor = choice(CORES)
        for i in lista:
            self.tela.itemconfig(self.lista[i][0], fill = cor)
            self.janela.update_idletasks()
            self.janela.update()
            sleep(1)

    def dfs(self, vertice):
        lista = self.grafo.buscaEmProfundidade(self.grafo[vertice])
        cor = choice(CORES)
        for i in lista:
            self.tela.itemconfig(self.lista[i][0], fill = cor)
            self.janela.update_idletasks()
            self.janela.update()
            sleep(1)

    def menorCaminho(self, escolha, vertice):
        if escolha == 'dijkstra': lista = self.grafo.dijkstra(self.grafo[vertice])
        else: lista = self.grafo.bellmanFord(self.grafo[vertice])
        etapas = [str(x[0].id) for x in lista] if escolha == 'dijkstra' else [str(x[0]) for x in lista]
        chaves = list(lista[0][1].keys())
        frame = Toplevel(self.janela)
        tabela = []
        for i in range(len(chaves)):
            tabela.append([])
            for j in range(len(etapas)):
                tabela[i].append(Button(frame, text = '', command = partial(self.path, tabela, i, j, chaves), width = 10))
                tabela[i][j].grid(row = i+1, column = j+1)
        Label(frame, text = 'Vertices').grid(row = 0, column = 0)
        for i in range(len(chaves)):
            Label(frame, text = f'{str(chaves[i].id)}').grid(row = i+1, column = 0)
        for i in range(len(etapas)):
            Label(frame, text = f'Etapa {etapas[i]}').grid(row = 0, column = i+1)
        coluna = 0
        for tuplas in lista:
            if escolha == 'dijkstra': self.select(tuplas[0].id)
            sleep(0.5) # PAUSA
            dic = tuplas[1]
            linha = 0
            for i in tuplas[1]:
                if dic[i] != None:
                    tabela[linha][coluna]['text'] = str(dic[i].id)
                    self.paint(i.id)
                    self.paint(dic[i].id)
                    sleep(0.5) # PAUSA
                    self.unselect(i.id)
                    self.unselect(dic[i].id)
                else:
                    if linha < len(tabela) and coluna < len(tabela[0]):
                        tabela[linha][coluna]['text'] = "NULL"
                    self.black(i.id)
                    sleep(0.5) # PAUSA
                    self.unselect(i.id)
                linha += 1
            if escolha == 'dijkstra': self.unselect(tuplas[0].id)
            coluna += 1

    def path(self, tabela, i, j, chaves):
        lista = []
        chaves = [x.id for x in chaves]
        self.paint(chaves[i])
        lista.append(chaves[i])
        escolhido = tabela[i][j]['text']
        if escolhido != 'NULL':
            while chaves[i] != tabela[i][j]['text']:
                self.paint(escolhido)
                lista.append(escolhido)
                i = chaves.index(escolhido)
                escolhido = tabela[i][j]['text']
                sleep(0.2) # PAUSA
            self.paint(tabela[i][j]['text'])
        sleep(1) # PAUSA
        for i in lista:
            self.unselect(i)

    def prim(self, vertice):
        relatorio = self.grafo.prim(self.grafo[vertice])
        lista = []
        for i in relatorio:
            try:
                lista.append(self.lista[(i[2].id, i[0].id)][0])
            except:
                lista.append(self.lista[(i[0].id, i[2].id)][0])
        for i in lista:
            self.arestaPaint(i, 'red')
            sleep(0.5)
        sleep(1)
        for i in lista:
            self.arestaPaint(i)
        
    def kruskal(self, vertice = None):
        relatorio = self.grafo.kruskal() if vertice == None else self.grafo.kruskal(self.grafo[vertice])
        lista = []
        for i in relatorio:
            try:
                lista.append(self.lista[(i[2].id, i[0].id)][0])
            except:
                lista.append(self.lista[(i[0].id, i[2].id)][0])
        for i in lista:
            self.arestaPaint(i, 'red')
            sleep(0.5)
        sleep(1)
        for i in lista:
            self.arestaPaint(i)
    
    def delete(self):
        self.tela.delete("all")
        if not self.ponderado and not self.direcionado:
            self.grafo = Graph()
        elif not self.direcionado:
            self.grafo = Graph(ponderado = True)
        elif not self.ponderado:
            self.grafo = Graph(direcionado = True)
        else:
            self.grafo = Graph(ponderado = True, direcionado = True)

    # Passar como parâmetro a cor!!
    def select(self, id): 
        self.tela.itemconfig(self.lista[id][0], fill = 'green')
        self.janela.update()
        self.janela.update_idletasks()
    def unselect(self, id): 
        self.tela.itemconfig(self.lista[id][0], fill = 'white')
        self.janela.update()
        self.janela.update_idletasks()
    def paint(self, id):
        self.tela.itemconfig(self.lista[id][0], fill = 'yellow')
        self.janela.update()
        self.janela.update_idletasks()
    def black(self, id):
        self.tela.itemconfig(self.lista[id][0], fill = 'black')
        self.janela.update()
        self.janela.update_idletasks()
    def arestaPaint(self, id, color = 'black'):
        self.tela.itemconfig(id, fill = color)
        self.janela.update()
        self.janela.update_idletasks()

grafo = Grafo()
