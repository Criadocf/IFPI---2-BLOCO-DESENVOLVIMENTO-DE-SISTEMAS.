#PROVA DO LUCAS
from random import randint

class Lanterninha:
  def __init__(self, bateria, creditos, sinal=True, ligado=True, estado=None):
    self.__bateria = bateria
    self.__creditos = creditos
    self.__aparelho_conectado = None
    self.__caixa_sms = []
    self.__sinal = sinal
    self.__ligado = ligado
    self.__estado = estado
  
  @property
  def bateria(self):
    return self.__bateria

  @property
  def creditos(self):
    return self.__creditos

  @property
  def aparelho_conectado(self):
    return self.__aparelho_conectado
  
  @property
  def caixa_sms(self):
    return self.__caixa_sms
  
  @property
  def sinal(self):
    return self.__sinal

  @property
  def ligado(self):
    return self.__ligado

  @property
  def estado(self):
    return self.__estado
  
  def ligar(self):
    if self.__ligado == True:
      print('O celular já está ligado')
    else:
      self.__ligado = True
      self.__estado = 'Stand by'
      print('O celular está ligado')


  
  
  def desligar(self):
    self.__ligado = False
    self.__estado = None
    self.__sinal = False
    print(f'O celular foi desligado')
  
  def colocar_creditos(self, valor):
    self.__creditos += valor
    print(f'O saldo do seu celular é de R${self.__creditos}')

  def carregar_bateria(self):
    self.__bateria = 100
    print(f'bateria carregada 100%')
    
  def fazer_ligacao(self, aparelho):
      if type(aparelho) == type(self):
        if self.__sinal and aparelho.sinal == True:
          if self.__estado == 'Standy by' and aparelho.__estado == 'Stand by':
            if self.__creditos >= 1:
              self.__estado = 'Em chamada'
              aparelho.estado = 'Em chamada'
              self.__aparelho_conectado = aparelho
              aparelho.__aparelho_conectado = self
              self.__creditos -= 1
            else:
              print('Você não tem créditos suficientes para efetuar esta chamada')
  
  def encerrar_ligacao(self, tempo):
    if tempo > self.__bateria and tempo > self.__aparelho_conectado.bateria:
      self.__estado = 'Stand by'
      self.__aparelho_conectado.__estado = 'Stand by'
      self.__bateria -= tempo
      self.__aparelho_conectado.__bateria -= tempo
      self.__aparelho_conectado = None
      self.__aparelho_conectado__aparelho_conectado = None
    else:
      if tempo > self.__bateria:
        self.__bateria = 0
        self = desligar(self)
      if tempo > self.__aparelho_conectado.__bateria:
        self.__aparelho_conectado__bateria = 0
        self.__aparelho_conectado = desligar(self)


  def enviar_sms(self, mensagem, aparelho):
    if self.__sinal and aparelho.__sinal == True:
      if self.__creditos >= 0.50:
        if self.__ligado and aparelho.__ligado == True:
          aparelho.__caixa_sms = mensagem
        else:
          print('Os dois celulares têm que estar ligados')
      else:
        print('Você não tem créditos suficientes! Recarregue Já!')
    
  def ver_sms(self):
    if len(self.__caixa_sms) > 1:
      for c in self.__caixa_sms:
        print(c)
    else:
      print('Sua caixa de mensagens está vazia')
  
  def esvaziar_caixa_sms(self):
    self.__caixa_sms.clear()
    print('A caixa de mensagens foi esvaziada')


celular1 = Lanterninha(59, 10)

celular1.bateria

celular2 = Lanterninha(99, 0)
celular2.ligar()

celular3 = Lanterninha(67, 5)

celular4 = Lanterninha(22, 40)
celular4.desligar()

celular1.fazer_ligacao(celular3)

celular1.enviar_sms('OI', celular3)

celular3.caixa_sms

celular3.esvaziar_caixa_sms()
celular3.caixa_sms