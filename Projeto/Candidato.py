from Bens import Bem
from Lista import Lista

class Candidato:
  def __init__(self, ano, ufEleicao, codigoCargo, descricaoCargo, nome, idCandidato, numero, 
               cpf, urna, numPartido, partido, siglaPartido, codigoOcupacao, 
               descricaoOcupacao, nascimento, sexo, escolaridade, estadoCivil, ufNascimento,
               municipio, situacaoPleito, situacaoCandidatura, listaDeBens):
    self.__ano = ano
    self.__ufEleicao = ufEleicao
    self.__codigoCargo = codigoCargo
    self.__descricaoCargo = descricaoCargo
    self.__nome = nome
    self.__idCandidato = idCandidato
    self.__numero = numero
    self.__cpf = cpf
    self.__urna = urna
    self.__numPartido = numPartido
    self.__partido = partido
    self.__siglaPartido = siglaPartido
    self.__codigoOcupacao = codigoOcupacao
    self.__descricaoOcupacao = descricaoOcupacao
    self.__nascimento = nascimento
    self.__sexo = sexo
    self.__escolaridade = escolaridade
    self.__estadoCivil = estadoCivil
    self.__ufNascimento = ufNascimento
    self.__municipio = municipio
    self.__situacaoPleito = situacaoPleito
    self.__situacaoCandidatura = situacaoCandidatura
    self.__listaDeBens = Lista()

  def incluirBem(self, novo):
    '''
    incluirBem(novo)
      Insere um novo bem ao candidato

    novo: Objeto do tipo Bem
    '''
    self.__listaDeBens.append(novo)
  def exibirBens(self):
    '''
    exibirBens()
      devolve uma string com os bens do candidato.
    '''
    string = ''
    for i in self.__listaDeBens:
      string += str(i)
    return string
  def __str__(self):
    string =f'''
    {self.__urna} -- {self.__numero} -- {self.__siglaPartido}
    {self.__descricaoCargo} ({self.__ufEleicao}) {self.__municipio} {self.__nascimento} ({self.__ufNascimento})
    Resumo dos bens:
    '''
    registrados = self.getCodigoDeBem()
    string += f'- Total declarado: R$ {sum(registrados.values())}\n'
    for i in registrados:
      string += f'    - Total por tipo de bem: R$ {registrados[i]}\n'
    return string
  def __repr__(self): return self.__str__()
  def __eq__(self, outro):
    if type(outro) != type(self): return False
    return self.__nome == outro.getNomeDoCandidato() and self.__cpf == outro.getCpf()
  def __ne__(self, outro): 
    if type(outro) != type(self): return True
    return self.__nome != outro.getNomeDoCandidato() or not self.__cpf != outro.getCpf()
  def getCodigoDeBem(self):
    '''
    getCodigoDeBem()
      Devolve um dicionario com os bens separados por codigo
    '''
    registrados = {}
    if len(self.__listaDeBens) == 0: registrados[0] = 0
    else:
      for bem in self.__listaDeBens:
        if bem.getCodigoDoTipoDeBem() not in registrados:
          registrados[bem.getCodigoDoTipoDeBem()] = float(bem.getValorDoBem().replace(',', '.'))
        else:
          registrados[bem.getCodigoDoTipoDeBem()] += float(bem.getValorDoBem().replace(',', '.'))
    return registrados
  def getAnoDaEleicao(self): return self.__ano
  def getSiglaDaUf(self): return self.__ufEleicao
  def getCodigoDoCargo(self): return self.__codigoCargo
  def getDescricaoDoCargo(self): return self.__descricaoCargo
  def getNomeDoCandidato(self): return self.__nome
  def getIdDoCandidato(self): return self.__idCandidato
  def getNumeroNaUrna(self): return self.__numero
  def getCpf(self): return self.__cpf
  def getNomeNaUrna(self): return self.__urna
  def getNumeroDoPartido(self): return self.__numPartido
  def getNomeDoPartido(self): return self.__partido
  def getSiglaDoPartido(self): return self.__siglaPartido
  def getCodigoDeOcupacaoDoCandidato(self): return self.__codigoOcupacao
  def getDescricaoDaOcupacao(self): return self.__descricaoOcupacao
  def getDataDeNascimento(self): return self.__nascimento
  def getSexoDoCandidato(self): return self.__sexo
  def getGrauDeInstrucao(self): return self.__escolaridade
  def getEstadoCivil(self): return self.__estadoCivil
  def getUfNascimento(self): return self.__ufNascimento
  def getNomeDoMunicipioDeNascimento(self): return self.__municipio
  def getSituacaoDoCandidatoPosPleito(self): return self.__situacaoPleito
  def getSituacaoDaCandidatura(self): return self.__situacaoCandidatura
  def getListaDeBens(self): return self.__listaDeBens

  def setAnoDaEleicao(self, novo): self.__ano = novo
  def setSiglaDaUf(self, novo): self.__ufEleicao = novo
  def setCodigoDoCargo(self, novo): self.__codigoCargo = novo
  def setDescricaoDoCargo(self, novo): self.__descricaoCargo = novo
  def setNomeDoCandidato(self, novo): self.__nome = novo
  def setIdDoCandidato(self, novo): self.__idCandidato = novo
  def setNumeroNaUrna(self, novo): self.__numero = novo
  def setCpf(self, novo): self.__cpf = novo
  def setNomeNaUrna(self, novo): self.__urna = novo
  def setNumeroDoPartido(self, novo): self.__numPartido = novo
  def setNomeDoPartido(self, novo): self.__partido = novo
  def setSiglaDoPartido(self, novo): self.__siglaPartido = novo
  def setCodigoDeOcupacaoDoCandidato(self, novo): self.__codigoOcupacao = novo
  def setDescricaoDaOcupacao(self, novo): self.__descricaoOcupacao = novo
  def setDataDeNascimento(self, novo): self.__nascimento = novo
  def setSexoDoCandidato(self, novo): self.__sexo = novo
  def setGrauDeInstrucao(self, novo): self.__escolaridade = novo
  def setEstadoCivil(self, novo): self.__estadoCivil = novo
  def setUfNascimento(self, novo): self.__ufNascimento = novo
  def setNomeDoMunicipioDeNascimento(self, novo): self.__municipio = novo
  def setSituacaoDoCandidatoPosPleito(novo): self.__situacaoPleito = novo
  def setSituacaoDaCandidatura(self, novo): self.__situacaoCandidatura = novo
  def setListaDeBens(self, novo): self.__listaDeBens = novo

if __name__ == '__main__':
  help(Candidato)