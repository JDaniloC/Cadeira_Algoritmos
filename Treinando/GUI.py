from random import choice, randrange
from time import sleep
from tkinter import *
from Grafo import *

CORES = ['cornflower blue', 'dark slate blue', 'light sea green', 'lawn green', 'lime green', 'dark khaki', 'goldenrod',  'rosy brown', 'saddle brown', 'dark orange', 'red', 'hot pink', 'pale violet red', 'snow4', 'SlateBlue1', 'DeepSkyBlue2', 'turquoise1', 'SeaGreen1', 'OliveDrab1']

class Grafo:
    def __init__(self):
        self.select = False
        self.janela = Tk()
        self.janela.title("Grafo")

        self.top = Frame(self.janela)
        self.foot = Frame(self.janela)

        self.tela = Canvas(self.top, width=1280, height=700, bd=0, highlightthickness=0)
        self.tela.bind('<ButtonPress-1>', self.selecionar)
        self.grafo = Vertices(self.janela, self.tela) # Escolher se o grafo é direcionado/ponderado

        self.entrada = Entry(self.foot)
        self.butCreate = Button(self.foot, text = "Adicionar Vértice", command = self.criar)
        self.butUpdate = Button(self.foot, text = "Adicionar Aresta", command = self.add)
        self.butBfs = Button(self.foot, text = "Busca em Largura", command = self.bfs)
        self.butDfs = Button(self.foot, text = "Busca em Profundidade", command = self.dfs)

        self.top.pack(fill = BOTH, expand = YES)
        self.foot.pack()
        self.tela.pack(fill = BOTH, expand = YES)
        self.entrada.pack(side = 'left')
        self.butCreate.pack(side = 'left')
        self.butUpdate.pack(side = 'left')
        self.butBfs.pack(side = 'left')
        self.butDfs.pack(side = 'left')
        
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
                self.criar(str(randrange(0, 100)), (event.x, event.y))
            

    def estaEm(self, tupla, seq):
        if tupla[0] >= seq[0] and tupla[0] <= seq[0] + 21:
            if tupla[1] >= seq[1] and tupla[1] <= seq[1] + 21:
                return True
        return False

    def criar(self, vertice = None, local = None):
        if vertice == None: self.grafo.addVertice(self.entrada.get())
        else: self.grafo.addVertice(vertice, local)
    
    def add(self, vertice = None, aresta = None):
        if vertice == None:
            vertice, aresta = self.entrada.get().split()
        self.grafo.addAresta(vertice, aresta)
    
    def bfs(self): self.grafo.bfs(self.entrada.get())
    def dfs(self): self.grafo.dfs(self.entrada.get())

class Vertices:
    def __init__(self, janela, canvas):
        self.lista = {}
        self.locals = {}

        self.janela = janela
        self.tela = canvas
        self.grafo = Graph()

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

    def addAresta(self, id, aresta):
        if not self.grafo.arestaDe(id, aresta):
            self.grafo.addAresta(id, aresta)
            if aresta not in self.lista:
                self.addVertice(aresta)
            coord = self.tela.coords(self.lista[id][0])
            linha = tuple([(coord[x] + coord[x+2])/2 for x in range(2)])
            coord = self.tela.coords(self.lista[aresta][0])
            linha += tuple([(coord[x] + coord[x+2])/2 for x in range(2)])
            
            nova = self.tela.create_line(linha, arrow = LAST) if self.grafo.isDirecionado() else self.tela.create_line(linha)
            self.lista[(id, aresta)] = nova
    
    def bfs(self, vertice):
        lista = self.grafo.buscaEmLargura(self.grafo[vertice])
        cor = choice(CORES)
        print(f"Pintando de {cor}")
        for i in lista:
            self.tela.itemconfig(self.lista[i][0], fill = cor)
            self.janela.update_idletasks()
            self.janela.update()
            sleep(1)

    def dfs(self, vertice):
        lista = self.grafo.buscaEmProfundidade(self.grafo[vertice])
        cor = choice(CORES)
        print(f"Pintando de {cor}")
        for i in lista:
            self.tela.itemconfig(self.lista[i][0], fill = cor)
            self.janela.update_idletasks()
            self.janela.update()
            sleep(1)

    def select(self, id): 
        self.tela.itemconfig(self.lista[id][0], fill = 'green')
        self.janela.update()
        self.janela.update_idletasks()
    def unselect(self, id): 
        self.tela.itemconfig(self.lista[id][0], fill = 'white')
        self.janela.update()
        self.janela.update_idletasks()

grafo = Grafo()
