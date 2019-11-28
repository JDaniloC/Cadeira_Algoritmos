from time import clock

class Cronometro:
    def __init__(self):
        self.__inicio = 0
        self.__final = 0
        self.__parou = False
        self.__ligado = True

    def getInicio(self): return self.__inicio
    def getFinal(self): return self.__final
    def getCondicao(self): return self.__parou
    def getEstado(self): return self.__ligado

    def ligar(self): self.__ligado = True
    def desligar(self):
        self.__ligado = False
        self.zerar()
        self.parar()
    
    def iniciar(self):
        self.__parou = False
        self.__inicio = clock()
        
    def parar(self):
        self.__parou = True
        self.__final = clock() - self.__inicio + self.__final

    def exibir(self):
        if self.__ligado:
            if self.__parou:
                print(int(self.__final))
            else:
                print(int(clock() - self.__inicio + self.__final))
        else:
            print("Cronometro desligado!")

    def zerar(self):
        self.__final = 0   
        self.__inicio = clock()
        
    def __str__(self):
        if self.__ligado:
            if self.__parou:
                return str(int(self.__final))
            else:
                return str(int(clock() - self.__inicio + self.__final))
        else:
            return "Cronometro desligado!"
        
    def __repr__(self):
        return "time.clock()"