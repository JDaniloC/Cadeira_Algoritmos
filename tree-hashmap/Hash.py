import numpy as np

class Item:
    def __init__(self, value):
        self.__prev = None
        self.value = value
        self.__next = None
    def __str__(self):
        return str(self.value)
    def __repr__(self):
        return "Item("+str(self.value)+")"
        
class Lista:
    def __init__(self, *iteravel):
        self.main = Item(None)
        self.length = 0
        self.end = Item(None)
        if len(iteravel) != 0:
            try:
                for i in iteravel:
                    for o in i:
                        self.append(o)
            except:
                while self.main._Item__next != None:
                    self.pop()
                if self.main.value != None:
                    self.pop()
                for i in iteravel:
                    self.append(i)

    def append(self, item):
        if self.main.value == None: 
            self.main = Item(item)
            self.end = self.main
        else:
            main = self.main
            while main._Item__next != None:
                main = main._Item__next
            main._Item__next = Item(item)
            self.end = main._Item__next
            main._Item__next._Item__prev = main
        self.length += 1

    def pop(self, indice = None):
        if self.main.value == None: raise IndexError("Tirando de uma lista vazia!")
        else:
            main = self.main
            if indice == None or indice == 0:
                if main._Item__next == None: 
                    aux = self.main.value
                    self.main = Item(None)
                    self.length -= 1 
                    return aux
                elif indice == 0:
                    aux = self.main.value
                    self.main = self.main._Item__next
                    self.main._Item__prev = None
                    del main
                    self.length -= 1 
                    return aux
                else:
                    while main._Item__next._Item__next != None:
                        main = main._Item__next
                    aux = main._Item__next.value
                    del main._Item__next
                    main._Item__next = None
                    self.length -= 1 
                    return aux
            else:
                cont = 1
                while indice > cont:
                    if main._Item__next != None:
                        main = main._Item__next
                        cont += 1
                    else: raise IndexError("Item fora de alcance!")
       
                if main.value != None and main._Item__next != None:
                    aux = main._Item__next.value
                    prox = main._Item__next._Item__next
                    del main._Item__next
                    main._Item__next = prox
                    self.length -= 1      
                    return aux
                else:
                    raise IndexError("Item fora de alcance!")

    def index(self, item):
        main = self.main
        cont = 0
        while main._Item__next != None:
            if main.value == item:
                return cont
            cont += 1
            main = main._Item__next
        if main.value == item:
            return cont
        raise ValueError(str(item)+" não está na lista")

    def concatenar(self, other):
        for i in range(len(other)):
            self.append(other[i])
            #self.append(other.pop(0)) mas não gosto da ideia de destruir a outra lista.
        return self

    def insert(self, indice, item):
        if indice >= self.length: self.append(item)
        else:
            if indice < 0: raise IndexError("Mano, preguiça de implementar spoakspo")
            elif indice < self.length//2:
                cont = 0
                main = self.main
                while indice > cont:
                    main = main._Item__next
                    cont += 1
            else:
                cont = self.length - 1
                main = self.end
                while indice < cont:
                    main = main._Item__prev
                    cont -= 1
            main._Item__prev._Item__next = Item(item)
            main._Item__prev._Item__next._Item__next = main
            main._Item__prev._Item__next._Item__prev = main._Item__prev
            main._Item__prev = main._Item__prev._Item__next
            self.length += 1

    def __str__(self):
        result = "["
        main = self.main
        if main.value != None:
            while main._Item__next != None:
                if type(main.value) == str: result += "'"+str(main.value)+"'" + ", "
                else:result += str(main.value) + ", "
                main = main._Item__next
            if type(main.value) == str: result += "'"+str(main.value)+"'"
            else: result += str(main.value)
        return result + "]"
    
    def __len__(self):
        return self.length
    def __repr__(self):
        return "Lista("+self.__str__()+")"

    def __getitem__(self, value, seta = 'None'):
        cont = 0
        if value > self.length-1 or value < (self.length)*-1:
            raise IndexError("Item fora de alcance!")
        if value < self.length//2 and value >= 0:
            main = self.main
            while value > cont:
                if main._Item__next != None:
                    main = main._Item__next
                    cont += 1
                else: raise IndexError("Item fora de alcance!")
        else:
            if value > 0:
                cont = self.length - 1
            else:
                cont -= 1
            main = self.end
            while value < cont:
                if main._Item__prev != None:
                    main = main._Item__prev
                    cont -= 1
                else: raise IndexError("Item fora de alcance!")
        if main.value != None:
            if seta != "None":
                return main
            return main.value
        else:
            raise IndexError("Item fora de alcance!")

    def __setitem__(self, index, item):
        try:
            main = self.__getitem__(index, "Sim")
            main.value = item
        except:
            raise IndexError("Item fora de alcance!")
    
    def __add__(self, other):
        lista2 = Lista()
        for i in range(self.length):
            lista2.append(self.__getitem__(i))
        for i in range(len(other)):
            lista2.append(other[i])
        return lista2
    
    def __iter__(self):
        return Ponteiro(self)

class Ponteiro:
    def __init__(self, lista):
        self.place = lista.main
        self.fim = False
    
    def __iter__(self):
        self.valor = self.place.value
        return self

    def __next__(self):
        if self.fim:
            raise StopIteration
        else:
            self.valor = self.place.value
            if self.place._Item__next == None:
                self.fim = True
            else:
                self.fim = False
            self.place = self.place._Item__next
            return self.valor


class Table:
  def __init__(self, tamanho = 366):
    self.tamanho = tamanho
    self.hash_table = np.full(tamanho, Lista)
    for i in range(len(self.hash_table)):
      self.hash_table[i] = Lista()
    self.days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    self.dict_months = {
    'JANEIRO': 0, 'FEVEREIRO': 1, 'MARÇO': 2, 'ABRIL': 3, 'MAIO': 4, 'JUNHO': 5,
    'JULHO': 6, 'AGOSTO': 7, 'SETEMBRO': 8, 'OUTUBRO': 9, 'NOVEMBRO': 10,
    'DEZEMBRO': 11
    }
    self.MONTHLY_NAMES = {
    0: 'JANEIRO', 1: 'FEVEREIRO', 2: 'MARÇO', 3: 'ABRIL', 4: 'MAIO', 5: 'JUNHO',
    6: 'JULHO', 7: 'AGOSTO', 8: 'SETEMBRO', 9: 'OUTUBRO', 10: 'NOVEMBRO',
    11: 'DEZEMBRO'
    }
    self.colision = {"quant":0, "local":[]}
  def add(self, data):
    if len(self.hash_table[data[1]]) != 0:
      self.colision["quant"] += 1
      if data[1] not in self.colision["local"]:
        self.colision["local"].append(data[1])
    self.hash_table[data[1]].append(data[0])
  def format_data(self, string):
    string = string.split(" ")
    nome = " ".join(string[:2])
    dia = int(string[2])
    mes = string[4]
    if mes.strip() == "MARO": mes = "MARÇO" #Quando dá encode, ele tira o Ç
    data = self.func_hash((dia, mes.strip()))
    return nome[:len(nome)-1], data
  def read_data(self, arquivo = 'pessoas.txt'):
    with open(arquivo, 'r', encoding="utf-8", errors="ignore") as arquivo:
      linhas = arquivo.readlines()
      for i in linhas:
        self.add(self.format_data(i))
      arquivo.close()
  def func_hash(self, data):
    result = data[0] - 1
    for i in range(self.dict_months[data[1]]):
      result += self.days[i];
    return result % self.tamanho
  def func_off(self, num):
    cont = 0
    while num > self.days[cont]:
        num -= self.days[cont]
        cont += 1
    return str(num+1) +" "+ self.MONTHLY_NAMES[cont]
  def equals(self):
    nomes = ""
    if self.colision["quant"] > 0:
      for i in self.colision["local"]:
        nomes += self.func_off(i) + "\n"
        for j in self.hash_table[i]:
          nomes += j + "\n"
    return nomes
  def __str__(self):
    result = ''
    for i in self.hash_table:
        if len(i) > 0:
            result += i.__str__() + "\n"
    return result + str(self.colision["quant"]) + " colisões."

t = Table() # Aqui ele cria a tabela com 366 lugares por padrão, mas se colocar outro valor de boa, ele vai fazer o módulo pelo valor ;D
t.read_data() # Aqui abre o arquivo e adiciona todas as pessoas dele no banco de dados, tudo automático, por padrão o nome do arquivo é pessoas.txt
print(t)# Aqui vai devolver o nome da glr pelo mais jovem, e diz se houve colisões.
print() 
print(t.equals()) #Isso devolve o nome da glr que colidiu