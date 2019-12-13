class Vertice:
    def __init__(self, identificador = None, arestas = None):
        self.__id = identificador
        self.__adjacentes = []
    
    def append(self, novo): 
        if type(getId()).__name__ == type(novo).__name__: 
            self.__adjacentes.append(novo)
    def __str__(self): return self.docId() + ":" + self.docAdjacentes()

    def getId(self): return self.__id
    def setId(self, novo): 
        if type(getId()).__name__ == type(novo).__name__: 
            self.__id = novo
    def delId(self): self.__id = None
    def docId(self): return str(self.__Id)
    id = property(getId, setId, delId, docId)

    def getAdjacentes(self): return self.__adjacentes
    def setAdjacentes(self, novo): 
        if type(getAdjacentes()).__name__ == type(novo).__name__ : 
            self.__adjacentes = novo
    def delAdjacentes(self): self.__adjacentes = []
    def docAdjacentes(self): return str(self.__adjacentes)
    adjacentes = property(getAdjacentes, setAdjacentes, delAdjacentes, docAdjacentes)