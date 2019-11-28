import textwrap

class Bem:
  def __init__(self, CodigoDoTipoDeBem, DescricaoDoTipoDeBem, DescricaoDetalhadaDoBem, ValorDoBem):
    self.__CodigoDoTipoDeBem = CodigoDoTipoDeBem
    self.__DescricaoDoTipoDeBem = DescricaoDoTipoDeBem
    self.__DescricaoDetalhadaDoBem = DescricaoDetalhadaDoBem
    self.__ValorDoBem = ValorDoBem
  
  def __str__(self):
    string = f'''
    {self.__CodigoDoTipoDeBem} -- {self.__DescricaoDoTipoDeBem} -- R$ {self.__ValorDoBem} Descrição: {textwrap.wrap(self.__DescricaoDetalhadaDoBem, width=80)[0]}
    '''
    return string
  def __repr__(self): return self.__str__() 
  def __eq__(self, outro):
    if type(outro) != type(self): return False
    return self.__CodigoDoTipoDeBem == outro.getCodigoDoTipoDeBem() and self.__DescricaoDetalhadaDoBem == outro.getDescricaoDetalhadaDoBem()
  def __ne__(self, outro):
    if type(outro) != type(self): return True
    return not self.__CodigoDoTipoDeBem == outro.getCodigoDoTipoDeBem() and not self.__DescricaoDetalhadaDoBem == outro.getDescricaoDetalhadaDoBem()

  def getCodigoDoTipoDeBem(self): return self.__CodigoDoTipoDeBem
  def getDescricaoDoTipoDeBem(self): return self.__DescricaoDoTipoDeBem
  def getDescricaoDetalhadaDoBem(self): return self.__DescricaoDetalhadaDoBem
  def getValorDoBem(self): return self.__ValorDoBem

  def setCodigoDoTipoDeBem(self, novo): self.__CodigoDoTipoDeBem = novo
  def setDescricaoDoTipoDeBem(self, novo): self.__DescricaoDoTipoDeBem = novo
  def setDescricaoDetalhadaDoBem(self, novo): self.__DescricaoDetalhadaDoBem = novo
  def setValorDoBem(self, novo): self.__ValorDoBem = novo

if __name__ == '__main__':
  help(Bem)