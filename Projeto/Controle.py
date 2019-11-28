from Lista import Lista
from Candidato import Candidato
from Bens import Bem
import os
import time

class Controle:
  def __init__(self):
    self.__listaDeCandidatos = Lista()
  def loadCandidatos(self, folder):
    '''
    loadCandidatos(folder)
      Insere os candidatos na lista de candidatos

    folder: Nome da pasta onde está todos os csv's
    '''
    nomes = os.listdir(folder)
    for archive in nomes:
      if archive not in ["leiame.pdf", "consulta_cand_2014_BRASIL.csv"]:
        arquivo = open(folder+"/"+archive, "r", errors='ignore')
        candidatos = arquivo.readlines()
        arquivo.close()
        candidatos = [x.strip().replace('"', "").split(";") for x in candidatos]
        for informacoes in candidatos:
          if 'DT_GERACAO' not in informacoes: 
            candidato = Candidato(informacoes[2], informacoes[10], informacoes[13], informacoes[14],
                              informacoes[17], informacoes[15], informacoes[16], informacoes[20],
                              informacoes[18], informacoes[27], informacoes[29], informacoes[28],
                              informacoes[49], informacoes[50], informacoes[38], informacoes[42],
                              informacoes[44], informacoes[46], informacoes[35], informacoes[37],
                              informacoes[25], informacoes[23], informacoes[55])
            self.__listaDeCandidatos.append(candidato)
  
  def loadBens(self, folder):
    '''
    loadBens(folder)
      Insere os bens dos candidatos.

    folder: Nome da pasta onde está todos os csv's
    '''
    colecaoBens = {}
    nomes = os.listdir(folder)
    for archive in nomes:
      if archive not in ['leiame.pdf', 'bem_candidato_2014_BRASIL']:
        arquivo = open(folder+'/'+archive, 'r', errors = 'ignore')
        bens = arquivo.readlines()
        arquivo.close()
        bens = [x.strip().replace('"', "").split(";") for x in bens]
        for informacoes in bens:
          if 'DT_GERACAO' not in informacoes:
            if informacoes[11] not in colecaoBens:
              colecaoBens[informacoes[11]] = Lista()
            bem = Bem(informacoes[13], informacoes[14], informacoes[15], informacoes[16])
            if bem not in colecaoBens[informacoes[11]]: colecaoBens[informacoes[11]].append(bem)
    for candidato in self.__listaDeCandidatos:
      if candidato.getIdDoCandidato() in colecaoBens:
        candidato.setListaDeBens(colecaoBens[candidato.getIdDoCandidato()])

  def devolvePor(self, criterio, padrao):
    '''
    devolvePor(criterio, padrao)
      Devolve uma lista de acordo com o criterio estabelecido

    criterio:
     - SiglaDoPartido
     - SiglaDaUF
     - NomeDoMunicipioDeNascimento
     - DescricaoDoCargo
     - Valor total de bens
     - SituacaoDoCandidatoPosPleito
     - DataDeNascimento
    padrao:
      O valor a ser comparado, nos bens irá selecionar todos acima da margem.
    '''
    lista = Lista()
    if criterio == 'partido':
      for i in self.__listaDeCandidatos:
        if i.getSiglaDoPartido() == padrao:
          lista.append(i)
    elif criterio == 'UF':
      for i in self.__listaDeCandidatos:
        if i.getSiglaDaUf() == padrao:
          lista.append(i)
    elif criterio == 'municipio':
      for i in self.__listaDeCandidatos:
        if i.getNomeDoMunicipioDeNascimento() == padrao:
          lista.append(i)
    elif criterio == 'cargo':
      for i in self.__listaDeCandidatos:
        if i.getDescricaoDoCargo() == padrao:
          lista.append(i)
    elif criterio == 'bens':
      for i in self.__listaDeCandidatos:
        if sum(i.getCodigoDeBem().values()) >= padrao:
          lista.append(i)
    elif criterio == 'pleito':
      for i in self.__listaDeCandidatos:
        if i.getSituacaoDoCandidatoPosPleito() == padrao:
          lista.append(i)
    elif criterio == 'nascimento':
      for i in self.__listaDeCandidatos:
        if int(i.getDataDeNascimento()[6:]) == padrao:
          lista.append(i)
    return lista

  def exibeEmOrdem(self, criterio, ordem):
    '''
    exibeEmOrdem(criterio, ordem)
      Ordena a lista de candidatos e imprime ordenado.

    criterio:
      - alfabetica (Nome dos candidatos)
      - bens (Valor total dos bens)
      - partido (Nome do partido)
      - data (Data de nascimento)
    ordem:
      - crescente
      - decrescente
    '''
    if criterio == 'alfabetica': criterio = 'alfa'
    elif criterio in ['bens', 'partido', 'data']: pass
    else: criterio = 'alfa'
    if ordem == 'crescente': ordem = 'cres'
    elif ordem == 'decrescente': ordem = 'dec'
    else: ordem = 'cres'
    criterio += ordem
    nova = Lista()
    for candidato in self.__listaDeCandidatos:
      nova.insereOrdenado(candidato, criterio)
    self.__listaDeCandidatos = nova
    print(self)
  
  def exibePor(self, criterio, padrao):
    '''
    exibePor(criterio, padrao)
      Exibe todos os candidatos de acordo com o padrão

    criterio:
     - SiglaDoPartido
     - SiglaDaUF
     - NomeDoMunicipioDeNascimento
     - DescricaoDoCargo
     - Valor total de bens
     - SituacaoDoCandidatoPosPleito
     - DataDeNascimento
    padrao:
      O valor a ser comparado, nos bens irá exibir todos acima da margem.
    '''
    for i in self.devolvePor(criterio, padrao):
      print(i)

  def media(self, criterio, padrao):
    '''
    media(criterio, padrao)
      Devolve a media dos candidatos de acordo com o padrão.

    criterio:
     - SiglaDoPartido
     - SiglaDaUF
     - NomeDoMunicipioDeNascimento
     - DescricaoDoCargo
     - Valor total de bens
     - SituacaoDoCandidatoPosPleito
     - DataDeNascimento
    padrao:
      O valor a ser comparado, nos bens irá selecionar todos acima da margem.
    '''
    resultado = {'total':0, 'quantidade':0}
    lista = self.devolvePor(criterio, padrao)
    for candidato in lista:
      resultado['quantidade'] += 1
      resultado['total'] += sum(candidato.getCodigoDeBem().values())
    return resultado['total']/resultado['quantidade']

  def remove(self, criterio, padrao):
    '''
    remove(criterio, padrao)
      Retira da lista de candidatos os que forem de acordo com o padrão.

    criterio:
     - SiglaDoPartido
     - SiglaDaUF
     - NomeDoMunicipioDeNascimento
     - DescricaoDoCargo
     - Valor total de bens
     - SituacaoDoCandidatoPosPleito
     - DataDeNascimento
    padrao:
      O valor a ser comparado, nos bens irá tirar todos acima da margem.
    '''
    lista = self.devolvePor(criterio, padrao)
    for candidato in lista:
      print(f'Removendo:\n{candidato}')
      self.__listaDeCandidatos.remove(candidato)
  
  def __getitem__(self, index): return self.__listaDeCandidatos[index]
  def __str__(self): return str(self.__listaDeCandidatos)
  def __len__(self): return len(self.__listaDeCandidatos)
  def __repr__(self): return 'c = Controle()\nc.loadCandidatos(folder)\nc.loadBens(folder)'
  
if __name__ == '__main__':
  controle = Controle()
  help(controle)
  controle.loadCandidatos(input('Nome da pasta de candidatos: '))
  controle.loadBens(input('Nome da pasta de Bens: '))

  