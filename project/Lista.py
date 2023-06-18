class Item:
    def __init__(self, value):
        self.__prev = None
        self.value = value
        self.__next = None
    def __str__(self): return str(self.value)
    def __repr__(self): return "Item("+str(self.value)+")"
    def getNext(self): return self.__next
    def getPrev(self): return self.__prev
    def getValue(self): return self.value
        
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

    def compara(self, um, outro, criterio):
        '''
        compara(um, outro, criterio)
            Devolve 1, 0, -1 caso o primeiro objeto for menor que o outro

        um: Objeto do tipo Candidato
        outro: Objeto do tipo Candidato
        criterio:
          - Crescente
            - alfacres (Ordem alfabética)
            - benscres (Valor total de bens)
            - partidocres (Nome do partido)
            - datacres (Data de nascimento)
            
          - Decrescente
            - alfadec (Ordem alfabética)
            - bensdec (Valor total de bens)
            - partidodec (Nome do partido)
            - datadec (Data de nascimento)
        '''
        result = 0
        if criterio in ['alfacres', 'alfadec']:
            um = um.getNomeDoCandidato()
            outro = outro.getNomeDoCandidato()
        elif criterio in ['benscres', 'bensdec']:
            um = sum(um.getCodigoDeBem().values())
            outro = sum(outro.getCodigoDeBem().values())
        elif criterio in ['partidocres', 'partidodec']:
            um = um.getNomeDoPartido()
            outro = outro.getNomeDoPartido()
        elif criterio in ['datacres', 'datadec']:
            data = um.getDataDeNascimento().split('/')
            um = int(data[0]) + (int(data[1])-1)*30 + int(data[2])*365
            data = outro.getDataDeNascimento().split('/')
            outro = int(data[0]) + (int(data[1])-1)*30 + int(data[2])*365
        if not um == outro:
            if um == min(um, outro): result = 1
            else: result = -1
        return result

    def insereOrdenado(self, item, criterio):
        '''
        insereOrdenado(item, criterio)
            Insere ordenado de acordo com o criterio

        item: Objeto do tipo Candidato
        criterio:
           - Crescente
            - alfacres (Ordem alfabética)
            - benscres (Valor total de bens)
            - partidocres (Nome do partido)
            - datacres (Data de nascimento)
            
          - Decrescente
            - alfadec (Ordem alfabética)
            - bensdec (Valor total de bens)
            - partidodec (Nome do partido)
            - datadec (Data de nascimento)
        '''
        if len(self) == 0: self.append(item)
        else:
            ver = False
            if criterio in ['alfacres', 'benscres', 'partidocres', 'datacres']:
                main = self.main
                while main.getNext() != None and self.compara(item, main.getValue(), criterio) < 0:
                    main = main.getNext()
            else:
                main = self.end
                while main.getPrev() != None and self.compara(item, main.getValue(), criterio) < 0:
                    main = main.getPrev()
            result = self.compara(item, main.getValue(), criterio)
            if ((result > 0 and criterio in ['alfacres', 'benscres', 'partidocres', 'datacres']) or
            (result < 0 and criterio not in ['alfacres', 'benscres', 'partidocres', 'datacres'])):
                if main.getPrev() != None:
                    main._Item__prev._Item__next = Item(item)
                    main._Item__prev._Item__next._Item__next = main
                    main._Item__prev._Item__next._Item__prev = main._Item__prev
                    main._Item__prev = main._Item__prev._Item__next
                else:
                    main._Item__prev = Item(item)
                    main._Item__prev._Item__next = main
                    self.main = self.main._Item__prev
            else:
                if main.getNext() != None:
                    main._Item__next._Item__prev = Item(item)
                    main._Item__next._Item__prev._Item__prev = main
                    main._Item__next._Item__prev._Item__next = main._Item__next
                    main._Item__next = main._Item__next._Item__prev
                else:
                    main._Item__next = Item(item)
                    main._Item__next._Item__prev = main
                    self.end = self.end._Item__next
            self.length += 1

    def append(self, item):
        '''
        append(item)
            Adiciona mais um objeto no final da lista

        item: Qualquer objeto
        '''
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
        '''
        pop(indice = None)
            Retira um objeto de acordo com o indice

        indice: Se não for especificado será retirado o último.
        '''
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
        '''
        index(item)
            Devolve o indice de um objeto

        item: Recebe o objeto
        '''
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

    def remove(self, item):
        '''
        remove(item)
            Remove um objeto.

        item: Objeto a ser removido
        '''
        self.pop(self.index(item))

    def insert(self, indice, item):
        '''
        insert(indice, item)
            Insere um novo item

        indice: Local a ser colocado
        item: Objeto a ser inserido
        '''
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

if __name__ == '__main__':
    help(Lista)