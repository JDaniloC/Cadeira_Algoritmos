class Grafo: # Grafo de números!!
  def __init__ (self, **kwargs):
    iteravel = kwargs.get("iteravel", None)
    self.ponderado = kwargs.get("ponderado", False)
    self.direcionado = kwargs.get("direcionado", False)
    self.matriz = kwargs.get("matriz", False)
    self.dict_adj = {}
    for tupla in iteravel:
      if type(tupla) == tuple:
        if self.ponderado: self.add(tupla[0], destino = tupla[1], peso = tupla[2])
        else: self.add(tupla[0], destino = tupla[1])
      else:
        self.add(tupla)
  
  def convert(self):
    if self.matriz:
      if not self.ponderado:
        for i in self.dict_adj:
          lista = self.dict_adj[i]
          self.dict_adj[i] = [x for x in range(len(lista)) if lista[x] == 1]
      else:
        for i in self.dict_adj:
          lista = self.dict_adj[i]
          self.dict_adj[i] = [(x,lista[x]) for x in range(len(lista)) if lista[x] != 0]
      self.matriz = False
    else:
      if not self.ponderado:
        for i in self.dict_adj:
          lista = self.dict_adj[i]
          self.dict_adj[i] = [0 for x in range(len(self.dict_adj))]
          for j in lista:
            self.dict_adj[i][j] = 1
      else:
        for i in self.dict_adj:
          lista = self.dict_adj[i]
          self.dict_adj[i] = [0 for x in range(len(self.dict_adj))]
          for tupla in lista:
            self.dict_adj[i][tupla[0]] = tupla[1]
      self.matriz = True
    
  def add(self, origem, **kwargs): # Adiciona um vértice e/ou aresta.
    verificador = False
    if self.matriz:
      self.convert()
      verificador = True
    if origem != 0 and origem-1 not in self.dict_adj:
      self.add(origem-1)
    destino = kwargs.get("destino", None)
    peso = kwargs.get("peso", None)
    tupla = (origem, destino, peso)
    if tupla[0] not in self.dict_adj:
        self.dict_adj[tupla[0]] = []
    if destino != None:
      if destino not in self.dict_adj:
        self.add(destino)
      if self.ponderado:
        par = (tupla[1], tupla[2])
        par2 = (tupla[0], tupla[2])
      else:
        par = tupla[1]
        par2 = tupla[0]
      self.dict_adj[tupla[0]].append(par)
      if not self.direcionado:
        if tupla[1] not in self.dict_adj:
          self.dict_adj[tupla[1]] = []
        self.dict_adj[tupla[1]].append(par2)
    if verificador:
      self.convert()
      
  def removeVertice(self, vertice):
    if vertice in self.dict_adj:
      if self.direcionado and not self.matriz:
        self.dict_adj[vertice] = []
      elif self.direcionado:
        self.dict_adj[vertice] = [0 for i in range(self.dict_adj)]
      else:
        if self.matriz:
          lista = [x for x in range(self.dict_adj[vertice]) if self.dict_adj[x] > 0]
        else:
          lista = self.dict_adj[vertice][:]
        if self.ponderado and not self.matriz:
          for i in lista:
            self.removeAresta(vertice, i[0])
        else:
          for i in lista:
            self.removeAresta(vertice, i)
    else:
      raise ValueError("Vértice não está no grafo!")
      
  def ligados(self, vertice1, vertice2):
    if not self.matriz:
      if not self.ponderado and vertice1 in self.dict_adj:
        return vertice2 in self.dict_adj[vertice1]
      elif self.ponderado and vertice1 in self.dict_adj:
        for i in self.dict_adj[vertice1]:
          if i[0] == vertice2:
            return True
        return False
      else:
          raise ValueError("Vértice não está no grafo!")
    else:
      if len(self.dict_adj) > vertice1:
        return self.dict_adj[vertice1][vertice2] > 0
      else:
        raise ValueError("Vértice não está no grafo!") 

  def removeAresta(self, vertice, aresta):
    if not self.matriz:
      if not self.ponderado:
        if vertice in self.dict_adj and aresta in self.dict_adj[vertice]:
          self.dict_adj[vertice].remove(aresta)
          if not self.direcionado:
            self.dict_adj[aresta].remove(vertice)
        else:
          raise ValueError("Vértice ou aresta não está no grafo!")
      else:
        if vertice in self.dict_adj and len([x for x in self.dict_adj[vertice] if x[0] == aresta]) > 0:
          for i in self.dict_adj[vertice]:
            if i[0] == aresta:
              self.dict_adj[vertice].remove(i)
          if not self.direcionado:
            for i in self.dict_adj[aresta]:
              if i[0] == vertice:
                self.dict_adj[aresta].remove(i)
        else:
          raise ValueError("Vértice ou aresta não está no grafo!")
    else:
      if vertice in self.dict_adj and self.dict_adj[vertice][aresta] > 0:
        self.dict_adj[vertice][aresta] = 0
        if not self.direcionado:
          self.dict_adj[aresta][vertice] = 0
      else:
        raise ValueError("Vértice ou aresta não está no grafo!")
      
  def inGrade(self, vertice):
    if self.matriz:
      if len(self.dict_adj) > vertice:
        result = 0
        for i in self.dict_adj.values():
          if i[vertice] > 0:
            result += 1
        return result
      else:
        raise ValueError("Vértice não está no grafo!")
    else:
      result = 0
      if not self.ponderado:
        for i in self.dict_adj.values():
          if vertice in i:
            result += 1
      else:
        for i in self.dict_adj.values():
          for j in i:
            if j[0] == vertice:
              result += 1
      return result

  def outGrade(self, vertice):
    if self.matriz and vertice in self.dict_adj:
      return len([x for x in self.dict_adj[vertice] if x > 0])
    elif vertice in self.dict_adj:
      return len(self.dict_adj[vertice])
    else:
      raise ValueError("Vértice não está no grafo!")

  def adjacente(self, vertice):
    if vertice in self.dict_adj:
      verificador = False
      result = []
      if self.matriz:
        self.convert()
        verificador = True
      if not self.direcionado:
        result = self.dict_adj[vertice] if not self.ponderado else [x[0] for x in self.dict_adj[vertice]]
      else:
        result = self.dict_adj[vertice] + [x for x in self.dict_adj if vertice in self.dict_adj[x]] if not self.ponderado else [x[0] for x in self.dict_adj[vertice]] + [x for x in self.dict_adj if vertice in [y[0] for y in self.dict_adj[x]]]
      if verificador:
        self.convert()
      return result
    else:
      raise ValueError("Vértice não está no grafo!")

  def menorAresta(self):
    if self.ponderado:
      verificador = False
      if not self.matriz:
        self.convert()
        verificador = True
      menor = min([min([y for y in self.dict_adj[x] if y > 0] + [99999999]) for x in self.dict_adj])
      menores = []
      for i in self.dict_adj:
        menores += [(i, x) for x in range(len(self.dict_adj[i])) if self.dict_adj[i][x] == menor]
      if verificador:
        self.convert()
      return menores

  def maiorAresta(self):
    if self.ponderado:
      verificar = False
      if not self.matriz:
        self.convert()
        verificador = True
      maior = max([max(self.dict_adj[x]) for x in self.dict_adj])
      maiores = []
      for i in self.dict_adj:
        maiores += [(i, x) for x in range(len(self.dict_adj[i])) if self.dict_adj[i][x] == maior]
      if verificador:
        self.convert()
      return maiores
    
  def buscaEmProfundidade(self, grafo = None):
    if grafo == None:
      grafo = self
    verificador = False
    if grafo.matriz:
      verificador = True
      grafo.convert()
    lista = []
    for i in grafo.dict_adj:
      self.visita(grafo, grafo.dict_adj[i], lista)
      if i not in lista:
        lista.append(i)
        print(i, end = " ")
    if verificador:
      grafo.convert()
  
  def visita(self, grafo, vertice, lista):
    vertice.sort()
    for i in vertice:
      if i not in lista:
        lista.append(i)
        self.visita(grafo, grafo.dict_adj[i], lista)
        print(i, end = " ")
   
  def buscaEmLargura(self, grafo = None): # Não terminado!!
    if grafo == None:
      grafo = self
    verificador = False
    if grafo.matriz:
      verificador = True
      grafo.convert()
    lista = []
    for vertice in grafo.dict_adj:
      if vertice not in lista:
        lista.append(vertice)
        print(vertice, end = " ")
        self.busca(lista, grafo, vertice)
    if verificador:
      grafo.convert()
  
  def busca(self, lista, grafo, vertice):
    lista.append(vertice)
    listinha = [str(x) for x in grafo.dict_adj[vertice] if x not in lista]
    print(" ".join(listinha) + " " if listinha != [] else "", end = "")
    for i in grafo.dict_adj[vertice]:
      if i not in lista:
        self.busca(lista, grafo, i)

  
  def __getitem__(self, index):
    if index in self.dict_adj:
      return self.dict_adj[index]
    else:
      raise IndexError("Item não consta no grafo!")
  
  def __str__(self):
    string = ""
    lista = list(self.dict_adj)
    if self.matriz:
      string += "   "
      for i in lista:
        string += str(i) + "  "
      string += "\n"
      for i in lista:
        string += str(i) + " " + str(self.dict_adj[i]) + "\n"
    else:
      for i in lista:
        string += str(i) + ": " + str(self.dict_adj[i]) + "\n"
    return string
    
  def __repr__(self):
    lista = []
    string = ""
    for i in self.dict_adj.keys():
      lista.append(i)
      if len(self.dict_adj[i]) > 0:
        for j in self.dict_adj[i]:
          if self.ponderado:
            string += ", (" + str(i) + ", " + str(j[0]) + ", " + str(j[1]) + ")" if self.direcionado or (not self.direcionado and j[0] not in lista) else "" 
          else:
            string += ", (" + str(i) + ", " + str(j) + ")" if self.direcionado or (not self.direcionado and j not in lista) else "" 
      else:
        string += ", " + str(i)
    string2 = ", ponderado = True" if self.ponderado else ""
    string2 += ", direcionado = True" if self.direcionado else ""
    return "Grafo(iteravel = [" + string[2:] + "]" + string2 + ")"

grafo = Grafo(iteravel = [(0, 1), (0, 2), (2, 3), (2, 4), (3, 5), (3, 6), (3, 7), (4, 7), (4, 8), (6, 8)])
print(grafo.buscaEmLargura())