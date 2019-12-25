class Vertice: # Não devolver nenhum raise é proposital.
    def __init__(self, identificador = None, arestas = None):
        self.__id = identificador
        self.__adjacentes = [] # Modifique a estrutura de dados aqui.
        if type(arestas).__name__ == type(self.adjacentes).__name__:
            self.adjacentes = arestas
    
    def append(self, novo, peso = None): 
        if type(self).__name__ == type(novo).__name__ and peso == None: # Saber se ele é um vértice!
            self.adjacentes.append(novo)
        elif peso != None:
            self.adjacentes.append((novo, peso))
    def remove(self, aresta, peso = False):
        if not peso:
            if aresta in self.adjacentes: self.adjacentes.remove(aresta)
        else:
            for i in range(len(self.adjacentes)):
                if self.adjacentes[i][0] == aresta:
                    self.adjacentes.pop(i)
                    break
    def peso(self, aresta):
        for i in self.adjacentes:
            if i[0] == aresta:
                return i[1]

    def __str__(self): 
        string = ''
        try:
            string = str(self.id) + ": [" + ', '.join([str(x.id) for x in self.adjacentes]) + "]"
        except:
            string = str(self.id) + ": [" + ", ".join([str(x[0].id) + "." + str(x[1]) for x in self.adjacentes]) + "]"
        return string
    def __repr__(self): return f"Vertice({self.__str__()})"

    def getId(self): return self.__id
    def setId(self, novo): 
        if type(self.id).__name__ == type(novo).__name__: 
            self.id = novo
    def delId(self): self.__id = None
    id = property(getId, setId, delId,)

    def getAdjacentes(self): return self.__adjacentes
    adjacentes = property(getAdjacentes, )
