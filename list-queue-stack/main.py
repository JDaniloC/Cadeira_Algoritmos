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

class Fila (Lista):
    def __init__(self, iteravel = None):
        self.main = Item(None)
        self.length = 0
        if iteravel != None:
            try:
                for i in iteravel:
                    self.append(i)
            except:
                while self.lenght > 0:
                    self.pop()
    
    def append(self, item):
        if self.main.value == None:
            self.main = Item(item)
        else:
            main = self.main
            while main._Item__next != None:
                main = main._Item__next
            main._Item__next = Item(item)
        self.length += 1
    
    def pop(self):
        if self.length != 0:
            main = self.main
            self.main = self.main._Item__next
            value = main.value
            del main
            self.length -= 1
            return value
        else:
            raise IndexError("Tirando de uma fila vazia.")

    def insert(self):
        return None

    def __getitem__(self, value, seta = "None"):
        cont = 0
        if value > self.length -1 or value < (self.length)*-1:
            raise IndexError("Item fora de alcance!")
        if value >= 0:
            main = self.main
            while value > cont:
                if main._Item__next != None:
                    main = main._Item__next
                    cont += 1
                else: raise IndexError("Item fora de alcance!")
        else:
            raise IndexError("Aqui não mano, aqui não!")
        if main.value != None:
            if seta != "None":
                return main
            return main.value
        else:
            raise IndexError("Item fora de alcance!")
        
    def __str__(self):
        text = "["
        if self.length != 0:
            main = self.main
            while main._Item__next != None:
                if type(main.value) == str:
                    text += "'" + main.value + "', "
                else:
                    text += str(main.value) + ", "
                main = main._Item__next
            if type(main.value) == str:
                text += "'" + main.value + "'"
            else:
                text += str(main.value)
        return text + "]"

    def __repr__(self):
        return "Fila("+self.__str__()+")"

class Pilha(Fila):
    def pop(self):
        if self.length == 1:
            value = self.main.value
            self.main = Item(None)
            self.length -= 1
            return value
        elif self.length != 0:
            main = self.main
            while main._Item__next._Item__next != None:
                main = main._Item__next
            prox = main._Item__next
            value = prox.value
            main._Item__next = None
            del prox
            self.length -= 1
            return value
        else:
            raise IndexError("Tirando de uma pilha vazia.")

    def __repr__(self):
        return "Pilha("+self.__str__()+")"