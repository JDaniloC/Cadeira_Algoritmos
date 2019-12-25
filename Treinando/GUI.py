from random import choice, randrange
from time import sleep
from functools import partial
from tkinter import *
from tkinter import messagebox
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
        self.ponderado = True
        self.grafo = Vertices(self.janela, self.tela, True) # Escolher se o grafo é direcionado/ponderado

        self.entrada = Entry(self.foot)
        self.butCreate = Button(self.foot, text = "Adicionar Vértice", command = self.criar)
        self.butUpdate = Button(self.foot, text = "Adicionar Aresta", command = self.add)
        self.butBfs = Button(self.foot, text = "Busca em Largura", command = self.bfs)
        self.butDfs = Button(self.foot, text = "Busca em Profundidade", command = self.dfs)
        self.butDijk = Button(self.foot, text = "Dijkstra", command = self.dijkstra)

        self.top.pack(fill = BOTH, expand = YES)
        self.foot.pack()
        self.tela.pack(fill = BOTH, expand = YES)
        self.entrada.pack(side = 'left')
        self.butCreate.pack(side = 'left')
        self.butUpdate.pack(side = 'left')
        self.butBfs.pack(side = 'left')
        self.butDfs.pack(side = 'left')
        self.butDijk.pack(side = 'left')

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
        if not self.ponderado:
            self.grafo.addAresta(vertice, aresta)
        else:
            if self.entrada.get().isnumeric():
                self.grafo.addAresta(vertice, aresta, int(self.entrada.get()))
            else:
                messagebox.showinfo("ADICIONAR", "Coloque o peso corretamente!")
    def bfs(self): self.grafo.bfs(self.entrada.get())
    def dfs(self): self.grafo.dfs(self.entrada.get())
    def dijkstra(self): 
        if self.ponderado: 
            entrada = self.entrada.get()
            if self.grafo.tem(entrada):
                self.grafo.dijkstra(self.entrada.get())
            else:
                messagebox.showinfo("DIJKSTRA", "Coloque um vértice válido!")

class Vertices:
    def __init__(self, janela, canvas, ponderado = False):
        self.lista = {}
        self.locals = {}

        self.janela = janela
        self.tela = canvas
        if not ponderado:
            self.grafo = Graph()
        else:
            self.grafo = Graph(ponderado = True)

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

    def dijkstra(self, vertice): # Construir uma tabela :D
        lista = self.grafo.dijkstra(self.grafo[vertice])
        etapas = [str(x[0].id) for x in lista]
        chaves = list(lista[0][1].keys())
        frame = Toplevel(self.janela)
        tabela = []
        for i in range(len(lista)):
            tabela.append([])
            for j in range(len(lista)):
                tabela[i].append(Button(frame, text = '', command = partial(self.path, tabela, i, j, chaves), width = 10))
                tabela[i][j].grid(row = i+1, column = j+1)
        Label(frame, text = 'Vertices').grid(row = 0, column = 0)
        for i in range(len(lista)):
            Label(frame, text = f'{str(chaves[i].id)}').grid(row = i+1, column = 0)
            Label(frame, text = f'Etapa {etapas[i]}').grid(row = 0, column = i+1)
        coluna = 0
        for tuplas in lista:
            self.select(tuplas[0].id)
            sleep(0.5)
            dic = tuplas[1]
            linha = 0
            for i in tuplas[1]:
                if dic[i] != None:
                    tabela[linha][coluna]['text'] = str(dic[i].id)
                    self.paint(i.id)
                    self.paint(dic[i].id)
                    sleep(1)
                    self.unselect(i.id)
                    self.unselect(dic[i].id)
                else:
                    tabela[linha][coluna]['text'] = "NULL"
                    self.black(i.id)
                    sleep(1)
                    self.unselect(i.id)
                linha += 1
            self.unselect(tuplas[0].id)
            coluna += 1

    def path(self, tabela, i, j, chaves):
        lista = []
        chaves = [x.id for x in chaves]
        self.paint(chaves[i])
        lista.append(chaves[i])
        escolhido = tabela[i][j]['text']
        while chaves[i] != tabela[i][j]['text'] and escolhido != "NULL": # escolhido não muda
            self.paint(escolhido)
            lista.append(escolhido)
            i = chaves.index(escolhido)
            escolhido = tabela[i][j]['text']
            sleep(0.1)
        self.paint(tabela[i][j]['text'])
        sleep(1)
        for i in lista:
            self.unselect(i)

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

grafo = Grafo()
