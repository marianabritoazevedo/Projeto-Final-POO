from random import randint
from abc import ABC, abstractmethod
from datetime import datetime
import pandas as pd

class MaisDeDuasColunasDispersao(Exception):
  pass

class UmaColunaDispersao(Exception):
  pass

class ArquivoVazio(Exception):
  pass

class NotCSV(Exception):
  pass

class NenhumArquivo(Exception):
  pass

class HistogramaInvalido(Exception):
  pass

class BoxplotInvalido(Exception):
  pass

class FDAInvalida(Exception):
  pass

class Util:

  def percorre_lista(lista,num):
    igual = False
    for i in lista:
      if i == num:
        igual = True
    return igual

  def geraId(lista):
    num = randint(0,99999)
    igual = Util.percorre_lista(lista, num)
    while igual == True:
      num = randint(0,99999)
      igual = Util.percorre_lista(lista, num)
    return num

class Pessoa(ABC):
  
  __lista_ids_pessoas = []
  
  def __init__(self, nome):
    self.nome = nome
    self.id = Util.geraId(Pessoa.__lista_ids_pessoas)
    Pessoa.__lista_ids_pessoas.append(self.id)
    
  @property
  def lista(self):
    return Pessoa.__lista_ids_pessoas
  
  @lista.setter
  def lista(num):
    Pessoa.__lista_ids_pessoas.append(num)

  @abstractmethod
  def __str__(self):
    pass
  
class Cliente(Pessoa):
  def __init__(self, nome, montante):
    super().__init__(nome)
    self.montante = montante

  def __str__(self):
    return "Id: {} - Nome: {} - Valor em Conta: {}".format(self.id, self.nome, self.montante)

class Produto:

  __dicionario = {}

  def __init__(self, id, valor, estrategia_preco, categoria):
    self.id = id
    self.valor = valor
    self.estrategia_preco = estrategia_preco
    self.categoria = categoria
    Produto.__dicionario[self.id] = [self.valor, self.estrategia_preco, self.categoria]
    
  def __str__(self):
    return "Id: {} - Valor: {} - Estrategia de preco: {} - Categoria: {}".format(self.id, self.valor, self.estrategia_preco, self.categoria)

  @staticmethod
  def acesso_itens(self):
    return self.__dicionario

class SistemaProvedorCanal:
  def __init__(self):
    self._id_provedor = 1
    self._id_canal = 1
  
  @property
  def id_do_provedor(self):
    return self._id_provedor
  
  @id_do_provedor.setter
  def id_do_provedor(self, novo_id):
    self._id_provedor = novo_id

  @property
  def id_do_canal(self):
    return self._id_canal
  
  @id_do_canal.setter
  def id_do_canal(self, novo_id):
    self._id_canal = novo_id

  def __str__(self):
    return "Provedor: {} - Canal: {}".format(self._id_provedor, self._id_canal)

class Transacao:

  __lista_ids_transacoes = []

  def __init__(self, cliente, produto, provedorcanal, data, fraude):
    self.id = Util.geraId(Transacao.__lista_ids_transacoes)
    Transacao.__lista_ids_transacoes.append(self.id)
    self.cliente = cliente
    self.produto = produto
    self.provedorcanal = provedorcanal
    self.datetime = data
    self.fraude = fraude

  @property
  def id_transacao(self):
    return Transacao.__lista_ids_transacoes
  
  @id_transacao.setter
  def id_transacao(self, novo_id):
    Transacao.__lista_ids_transacoes.append(self.id)

  def getData(transacao):
    lista = [transacao.id, transacao.cliente.id, transacao.provedorcanal.id_do_provedor,
    transacao.produto.id, transacao.produto.categoria, transacao.provedorcanal.id_do_canal,
    transacao.cliente.montante, transacao.produto.valor, transacao.datetime, transacao.produto.estrategia_preco, transacao.fraude]
    return lista

  def __str__(self):
    return "Cliente:\n{}\nProduto:\n{}\nHardware:\n{}".format(Cliente.__str__(self.cliente), Produto.__str__(self.produto), SistemaProvedorCanal.__str__(self.provedorcanal))

if __name__ == "__main__":
  #Testando de Cliente
  c1 = Cliente('Mari',30)
  print(c1)
  c2 = Cliente('Mariana',30)
  print(c2)
  print(c2.lista)

  #Testado Produto
  p1 = Produto(1,20.00,1,"Netflix")
  print(p1)

  p2 = Produto(2,15.00,1,"Amazon")
  print(p2)

  #Testando provedor canal
  canal = SistemaProvedorCanal()
  print(canal)
  canal.id_do_canal = 2

  #Testando transacao
  t1 = Transacao(c1, p1, canal, "19/02/2021 13:00",1)
  print(t1)
  t2 = Transacao(c2, p2, canal, "19/02/2021 13:15",0)

  #Criando Dataframe usando Pandas
  lista_de_colunas= ['Transacao','Usuario','Provedor','Produto','Categoria do Produto','Canal','Valor Conta Cliente','Valor do Servico','Data/Hora','Estrategia Preco Produto','Fraude']
  pacote_de_transacoes = list()
  pacote_de_transacoes.append(t1.getData())
  pacote_de_transacoes.append(t2.getData())
  df = pd.DataFrame(pacote_de_transacoes, columns = lista_de_colunas)
  print(df) 
