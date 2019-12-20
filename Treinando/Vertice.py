class Vertice: # Não devolver nenhum raise é proposital.
    def __init__(self, identificador = None, arestas = None):
        self.__id = identificador
        self.__adjacentes = [] # Modifique a estrutura de dados aqui e no del!
        if type(arestas).__name__ == type(self.adjacentes).__name__:
            self.adjacentes = arestas
    
    def append(self, novo): 
        if type(self).__name__ == type(novo).__name__: # Saber se ele é um vértice!
            self.adjacentes.append(novo)
        else: print("Tipos incompatíveis.")
    def remove(self, aresta):
        if aresta in self.adjacentes: self.adjacentes.remove(aresta)
        else: print("Não está na lista de adjacentes.")

    def __str__(self): return str(self.id) + ": [" + ', '.join([str(x.id) for x in self.adjacentes]) + "]"
    def __repr__(self): return f"Vertice({self.__str__()})"

    def getId(self): return self.__id
    def setId(self, novo): 
        if type(self.id).__name__ == type(novo).__name__: 
            self.id = novo
    def delId(self): self.__id = None
    id = property(getId, setId, delId,)

    def getAdjacentes(self): return self.__adjacentes
    def setAdjacentes(self, novo): 
        if type(self.adjacentes).__name__ == type(novo).__name__ : 
            self.__adjacentes = novo
    def delAdjacentes(self): self.__adjacentes = []
    adjacentes = property(getAdjacentes, setAdjacentes, delAdjacentes,)
