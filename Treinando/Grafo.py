from Treinando.Vertice import *

class Graph:
    def __init__(self):
        self.__vertices = []
    
    def addVertice(self, novo):
        self.getVertuces().append(Vertice(novo))

    def addAresta(self, vertice, nova):
        if vertice in self.getVertices():
            indice = self.getVertices().index(vertice)
            self.getVertices()[indice].append(Vertice(nova))

    def getVertices(self): return self.__main
    vertices = property(getVertices, )