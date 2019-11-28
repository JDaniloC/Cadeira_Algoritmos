class No:
  def __init__(self, key = None, value = None):
    self.key = key
    self.value = value
    self.daddy = None
    self.rt = None
    self.lt = None

  def __lt__(self, other): # Anteriormente eu comparava pelo value, mas agora pelo key por uma questão da arvore... Para pegar o valor só no get!
    if (type(other)) != type(self): raise TypeError("'<' não suportado entre instancias de "+type(other).__name__+" e "+type(self).__name__)
    if self.key < other.key: return True
    else: return False

  def __gt__(self, other):
    if (type(other)) != type(self): raise TypeError("'>' não suportado entre instancias de "+type(other).__name__+" e "+type(self).__name__)
    if self.key > other.key: return True
    return False
  
  def __le__(self, other):
    if (type(other)) != type(self): raise TypeError("'<=' não suportado entre instancias de "+type(other).__name__+" e "+type(self).__name__)
    if self.key <= other.key: return True
    return False
  
  def __ge__(self, other):
    if (type(other)) != type(self): raise TypeError("'>=' não suportado entre instancias de "+type(other).__name__+" e "+type(self).__name__)
    if self.key >= other.key: return True
    return False

  def __eq__(self, other):
    if type(other) != type(self):
      if self.key == other: return True
      return False
    if self.key == other.key: return True
    return False
  
  def __ne__(self, other):
    if type(other) != type(self):
      if self.key != other: return True
      return False
    if self.key != other.key: return True
    return False

  def __str__(self):
    valor = self.value
    if type(valor) == str: valor = "'"+str(valor)+"'"
    return str(valor)

  def __repr__(self):
    return "No("+str(self.key)+','+self.__str__()+")"
  
  def setValue(self, valor):
    self.value = valor
  
  def getValue(self):
    return self.value

  def __dict__(self):
    return {self.key:self.value}

class Tree:
  def __init__(self, *iteravel):
    self.dad = No()
    self.height = 0
    self.lenght = 0
    if len(iteravel) > 0:
      try:
        for i in iteravel:
          for o in i:
            if type(i) == dict:
              self.inserir(o, i[o])
            else:
              self.inserir(o)
      except:
        for i in iteravel:
          self.inserir(i)

  def inserir(self, key, valor = None):
    if self.height == 0:
      self.dad = No(key, valor)
      self.lenght += 1
      self.height += 1
    else:
      dad = self.dad
      valor = No(key, valor)
      height = 2
      while (dad > valor and dad.lt != None) or (dad < valor and dad.rt != None):
        if valor < dad:
          dad = dad.lt
          height += 1
        elif valor > dad:
          dad = dad.rt
          height += 1          
      if valor < dad:
        dad.lt = valor
        self.lenght += 1
        valor.daddy = dad
      elif valor > dad:
        dad.rt = valor
        valor.daddy = dad
        self.lenght += 1
      else:
        if type(dad.value) == int: dad.value += 1
        elif dad.value == None: dad.value = 1
        else:
          dad.value = valor 
      if height > self.height: self.height = height   

  def __delitem__(self, no):
    if self.lenght == 0: raise IndexError("Tirando de uma árvore vazia!")
    else:
      main = self.dad
      while (no < main.key and main.lt != None) or (no > main.key and main.rt != None):
        if no < main.key:
          main = main.lt
        elif no > main.key:
          main = main.rt
      if main == no:
        self.remove(main)
      else:
        raise KeyError(no)     

  def remove(self, main):
    if main != None:
      if main.lt == None and main.rt == None:
        if main.daddy != None:
          pai = main.daddy
          if main == pai.lt: pai.lt = None
          else: pai.rt = None
        else: self.dad = No()
        self.lenght -= 1
        self.height = self.altura(self.dad)
      elif (main.lt != None and main.rt == None) or (main.lt == None and main.rt != None):
        if main.lt != None:
          if main.daddy != None:
            if main.daddy.rt == main:
              main.daddy.rt = main.lt
            else:
              main.daddy.lt = main.lt
          main.lt.daddy = main.daddy
        else:
          if main.daddy != None:
            if main.daddy.rt == main:
              main.daddy.rt = main.rt
            else:
              main.daddy.lt = main.rt
          main.rt.daddy = main.daddy
        self.lenght -= 1
        self.height = self.altura(self.dad)
      else:
        no = self.sucessor(main)
        main.key = no.key
        main.value = no.value
        self.remove(no)
    else:
      raise IndexError("Item fora de alcance!")

  def reiniciar(self):
    if self.lenght != 0:
      lista = self.posOrdem(self.dad)
      for i in range(len(lista)):
        self.remove(lista[i])
        lista[i] = lista[i].key
      return lista

  def posOrdem(self, no):
    if self.lenght == 0: return []
    else:
      valor = []
      if no.lt != None:
        valor += self.posOrdem(no.lt)
      if no.rt != None:
        valor += self.posOrdem(no.rt)
      return valor + [no]

  def maxTree(self, no):
    while no.rt != None:
      no = no.rt
    return no

  def sucessor(self, no):
    if no.rt != None:
      no = no.rt
      while no.lt != None:
        no = no.lt
      return no
    else:
      pai = no.daddy
      while pai != None and no == pai.rt:
        no = pai
        pai = pai.daddy
      return pai

  def antecessor(self, no):
    if no.lt != None:
      self.maxTree(no.lt)
    else:
      pai = no.daddy
      while pai != None and no == pai.lt:
        no = pai
        pai = pai.daddy
      return pai

  def altura(self, no):
    if no == None:
      return 0
    else:
      esquerda = self.altura(no.lt)
      direita = self.altura(no.rt)
      if esquerda > direita:
        valor = 1 + esquerda
      else:
        valor = 1 + direita
      return valor

  def keys(self):
    if self.height != 0:
      return self.string(self.dad)

  def values(self, no = None):
    if self.height != 0:
      if no == None:
        no = self.dad
      valores = []
      if no.lt != None:
        valores += self.values(no.lt)
      if no.value != None:
        valores += [no.value]
      if no.rt != None:
        valores += self.values(no.rt)
      return valores 

  def __len__(self):
    return self.lenght

  def __bool__(self):
    if self.height == 0:
      return False
    else:
      return True

  def __str__(self):
    a = self.string(self.dad)
    return str(a)
  
  def string(self, no):
    valores = []
    if no.lt != None:
      valores += self.string(no.lt)
    if no.key != None:
      valores += [no.key]
    if no.rt != None:
      valores += self.string(no.rt)
    return valores            

  def __repr__(self):
    return "Tree("+str(self.preOrdem())+")"

  def __getitem__(self, chave):
    if self.height == 0: raise IndexError("Item fora de alcance!")
    else:
      no = self.get(chave, self.dad)
      if no != None:
        return no.getValue()
      else:
        raise IndexError("Item fora de alcance!")

  def get(self, key, no):
    if no != None:
      if key == no:
        return no
      elif key < no.key:
        return self.get(key, no.lt)
      else:
        return self.get(key, no.rt)

  def __setitem__(self, chave, valor):
    if self.height == 0: raise IndexError("Item fora de alcance!")
    else:
      no = self.get(chave, self.dad)
      if no != None:
        no.value = valor
      else:
        raise IndexError("Item fora de alcance!")

  def __iter__(self):
    return Pont(self)

  def preOrdem(self, dad = ''):
    if self.lenght == 0: return []
    else:
      if dad == '': dad = self.dad
      if dad.rt == None and dad.lt == None:
        return [dad.key]
      elif dad.rt == None:
        return [dad.key]+ self.preOrdem(dad.lt)
      elif dad.lt == None:
        return [dad.key]+ self.preOrdem(dad.rt)
      else:
        return [dad.key]+ self.preOrdem(dad.lt)+ self.preOrdem(dad.rt)

  def recursive(self, dad = ''):
    if self.lenght == 0: return {}
    else:
      if dad == '': dad = self.dad
      if dad.rt == None and dad.lt == None:
        return dad.key
      elif dad.rt == None:
        return {dad.key: self.recursive(dad.lt)}
      elif dad.lt == None:
        return {dad.key: self.recursive(dad.rt)}
      else:
        return {dad.key: [self.recursive(dad.lt), self.recursive(dad.rt)]}
  
  def __contains__(self, chave):
    if self.get(chave, self.dad) != None: return True
    return False

  def __dict__(self):
      return self.recursive()

class Pont:
  def __init__(self, main):
    self.main = main.preOrdem() # Assim fica mais intuitivo, já que faz a mesma coisa.
    if len(self.main) > 0: self.fim = False
    else: self.fim = True
  def iter(self):
    if len(self.main) != 0:
      self.valor = self.main.pop(0)
    return self
  def __next__(self):
    if self.fim: raise StopIteration
    else:
      self.valor = self.main.pop(0)
      if len(self.main) == 0:
        self.fim = True
      return self.valor
    
class Avl(Tree):
  @staticmethod
  def balanceada(arvore):
    if isinstance(arvore, Tree):
      return Avl.balanco(arvore, arvore.dad)
    else:
      raise TypeError("Não é uma árvore!")
  @staticmethod
  def balancear(arvore):
    if not Avl.balanceada(arvore):
      no = Avl.findenemy(arvore, arvore.dad)
      if Avl.coef_balanceamento(arvore, no) < -1:
        if Avl.coef_balanceamento(arvore, no.lt) <= 0:
          Avl.girar_direita(arvore, no)
        else:
          Avl.girar_esquerda(arvore, no.lt)
          Avl.girar_direita(arvore, no)
      else:
        if Avl.coef_balanceamento(arvore, no.rt) >= 0:
          Avl.girar_esquerda(arvore, no)
        else:
          Avl.girar_direita(arvore, no.rt)
          Avl.girar_esquerda(arvore, no)
  
  def inserir(self, key, valor = None):
    super().inserir(key, valor)
    Avl.balancear(self)
  
  def __delitem__(self, no):
    super().__delitem__(no)
    Avl.balancear(self)

  def coef_balanceamento(self, no):
    if no != None:
      a = self.altura(no.lt)
      b = self.altura(no.rt)
      return b - a
    return 0
  
  def findenemy(self, no):
    resposta = None
    if no != None:
      if abs(Avl.coef_balanceamento(self, no)) < 2:
        if no.lt != None: resposta = self.findenemy(no.lt)
        if no.lt != None: resposta = self.findenemy(no.rt)
      else: resposta = no
    return resposta
  
  def balanco(self, no):
    resposta = False
    if no != None:
      if abs(Avl.coef_balanceamento(self, no)) < 2:    
        resposta = True
        if no.lt != None: resposta = self.balanco(no.lt)
        if no.rt != None and resposta: resposta = self.balanco(no.rt)
    return resposta

  def girar_esquerda(self, no):
    pai = no.rt
    filho = pai.lt
    pai.daddy = no.daddy
    if no.daddy != None:
      if no.daddy.lt == no: no.daddy.lt = pai
      else: no.daddy.rt = pai
    no.daddy = pai
    pai.lt = no
    no.rt = filho
    if filho != None: 
      filho.daddy = no
    if no == self.dad: self.dad = pai
    
  def girar_direita(self, no):
    pai = no.lt
    filho = pai.rt
    pai.daddy = no.daddy
    if no.daddy != None:
      if no.daddy.lt == no: no.daddy.lt = pai
      else: no.daddy.rt = pai
    no.daddy = pai
    pai.rt = no
    no.lt = filho 
    if filho != None: 
      filho.daddy = no
    if no == self.dad: self.dad = pai
    
  def __repr__(self):
    return "Avl("+str(self.preOrdem())+")"