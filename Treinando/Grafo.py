from Vertice import *

# Colocar grafo ponderado!
class Graph: 
    def __init__(self, **kwargs):
        self.__vertices = [] # Coloque a estrutura de dados aqui e no del!
        self.__verInd = []

        iteravel = kwargs.get("iteravel", None)
        self.__ponderado = kwargs.get("ponderado", False)
        self.__direcionado = kwargs.get("direcionado", False)

        if iteravel:
            if not self.ponderado:
                for i in iteravel:
                    if type(i).__name__ in ['tuple', 'list']:
                        self.addVertice(i[0])
                        for j in i[1:]: self.addAresta(i[0], j)
                    else: self.addVertice(i)

    def addVertice(self, vertice, aresta = None):
        if vertice not in self.verInd:
            self.vertices.append(Vertice(vertice))
            self.verInd.append(vertice)
        if aresta != None: self.addAresta(vertice, aresta)
    def addAresta(self, vertice, outro):
        if vertice not in self.verInd:
            self.addVertice(vertice)
        if outro not in self.verInd:
            self.addVertice(outro)
        if not self.arestaDe(vertice, outro):
            self.getVertice(vertice).append(self.getVertice(outro))
        if not self.direcionado and not self.arestaDe(outro, vertice):
            self.getVertice(outro).append(self.getVertice(vertice))

    def removeVertice(self, vertice):
        if vertice in self.verInd:
            objeto = self.getVertice(vertice)
            for i in self.vertices:
                if objeto in i.adjacentes:
                    i.adjacentes.remove(objeto)
            self.vertices.remove(objeto)
            self.verInd.remove(vertice)
    def removeAresta(self, vertice, aresta):
        vertice = self.getVertice(vertice)
        aresta = self.getVertice(aresta)
        if vertice != None:
            vertice.remove(aresta)
        if not self.direcionado and aresta != None:
            aresta.remove(vertice)

    def arestaDe(self, vertice, aresta):
        if vertice in self.verInd:
            lista = self.getVertice(vertice).adjacentes
            for i in lista:
                if vertice == i.id: return True
        return False
    def getVertice(self, vertice):
        if vertice in self.verInd: return self.vertices[self.verInd.index(vertice)]
        else: return None

    def buscaEmLargura(self, vertice = None):
        if vertice == None and len(self.vertices) == 0:
            return []
        else:
            if vertice == None:
                vertice = self.vertices[0]
            visitados = []
            visitar = [vertice]
            for vertice in visitar:
                visitados.append(vertice) 
                for aresta in vertice.adjacentes:
                    if aresta not in visitar:
                        visitar.append(aresta)
            return [x.id for x in visitados]

    def buscaEmProfundidade(self, vertice):
        selecionados = []
        self.visita(vertice, selecionados)
        return [x.id for x in selecionados] 

    def visita(self, vertice, selecionados):
        selecionados.append(vertice)
        for i in vertice.adjacentes:      
            if i not in selecionados:
                self.visita(i, selecionados)
        
    def isDirecionado(self): return self.direcionado
    def isPonderado(self): return self.ponderado
    def __getitem__(self, item):
        for i in self.vertices:
            if i.id == item:
                return i
    def __str__(self): return '\n'.join([str(x) for x in self.vertices])
    def __repr__(self): 
        referenciados = []
        string = 'iteravel = ['
        for x in self.vertices:
            if len(x.adjacentes) != 0:
                string += "(" + str(x.id)
                for y in x.adjacentes:
                    referenciados.append(y.id)
                    string += ', ' + str(y.id)
                string += "), "
            elif x.id not in referenciados:
                string += str(x.id) + ", "
            referenciados.append(x.id)
        string = string[:-2] + '], '
        string += "ponderado = True, " if self.ponderado else ''
        string += 'direcionado = True' if self.direcionado else ''
        return "Graph(" + string[:-2] + ")"

    def getVertices(self): return self.__vertices
    vertices = property(getVertices, )

    def getVerInd(self): return self.__verInd
    verInd = property(getVerInd, )

    def getDirecionado(self): return self.__direcionado
    def setDirecionado(self, novo): 
        if type(novo).__name__ == 'bool': self.__direcionado = novo
    direcionado = property(getDirecionado, setDirecionado, )

    def getPonderado(self): return self.__ponderado
    def setPonderado(self, novo): 
        if type(novo).__name__ == "bool": self.__ponderado = novo
    ponderado = property(getPonderado, setPonderado, )

if __name__ == "__main__":     
    g = Graph(iteravel = [('a', 'b', 's'), ('s', 'c', 'g'), ('c', 'd', 'e', 'f'), ('g', 'f', 'h'), ('e', 'h')])
    print(g)
    print(g.buscaEmProfundidade(g.vertices[0]))
