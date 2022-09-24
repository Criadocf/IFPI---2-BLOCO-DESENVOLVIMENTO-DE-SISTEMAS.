# RADIO

estacoes = {89.5:'Cocais', 91.5:'Mix', 94.1:'Boa', 99.1:'Clube'}

class RadioFM:
  def __init__(self, vol_max, estacoes1):
    self.volume_min = 0
    self.__volume_max = vol_max
    self.freq_min = 88
    self.freq_max = 108
    self.estacoes = estacoes1
    self.volume = 0
    self.ligado = False
    self.estacao_atual = None
    self.frequencia_atual = None
    self.antena_habilitada = False

  @property
  def volumee(self):
      return self.__volume_max

  @volumee.setter
  def volumee(self, volume=1):
      if self.ligado == True:
        self.volume += volume
        if self.volume > self.__volume_max:
          self.volume = self.__volume_max
        print(f'O volume está em {self.volume}')
  
  def ligar(self):
    if self.ligado == True:
      print('O rádio já está ligado')
    else:
      if self.antena_habilitada == True:
        self.frequencia_atual = 89.5
        print('O rádio está ligado')
        print(f'Frequência inicializada - 89.5')
        print(f'Volume do rádio - {self.volume_min}')
        self.estacao_atual = estacoes[89.5]
        print(f'A estação atual é {self.estacao_atual}')
      else:
        self.ligado = True
        self.volume = self.volume_min
        print(f'O rádio está ligado')
    

  def desligar(self):
    self.estado = False
    self.frequencia_atual = None
    self.estacao_atual = None
    print('O rádio está desligado')

  def aumentar_volume(self, volumee=1):
    if self.ligado == True:
      self.volume += volumee
      if self.volume > self.__volume_max:
        self.volume = self.__volume_max
      print(f'O volume está em {self.volume}')


  def diminuir_volume(self, volumee=1):
    if self.ligado == True:
      self.volume -= volumee
      if self.volume < self.volume_min:
        self.volume = self.volume_min
      print(f'O volume está em {self.volume}')

  def mudar_frequencia(self, frequencia=0):
      if self.ligado == True:
        if self.antena_habilitada == True:
          if frequencia > 0 and frequencia !=0:
            self.frequencia_atual = frequencia
            for c in estacoes.keys():
              if frequencia == c:
                self.estacao_atual = estacoes[c]
          elif frequencia == 0:
            self.frequencia_atual = 89.5
            self.estacao_atual = estacoes[89.5]
            if self.frequencia_atual == 99.1:
              self.frequencia_atual = 89.5
              self.estacao_atual = estacoes[89.5]
          
          else: 
                print('Estação inexistente')
        
 

  def habilitar_antena(self):
      self.antena_habilitada = True
      self.frequencia_atual = 89.5
      self.estacao_atual = estacoes[89.5]
      print('A antena está habilitada')

radio1 = RadioFM(30, 56.9)
radio1.ligar()
radio1.habilitar_antena()
radio1.mudar_frequencia(89.5)
radio1.frequencia_atual
radio1.estacao_atual
print(' ')

radio2 = RadioFM(-60, 89.5)
radio2.desligar()
print(' ')

radio3 = RadioFM(100, 99.1)
radio3.aumentar_volume()
radio3.ligar()
radio3.ligar()
radio3.aumentar_volume(110)
radio3.mudar_frequencia(99.1)
radio3.habilitar_antena()
radio3.mudar_frequencia(2)
radio3.mudar_frequencia(99.1)
radio3.estacao_atual
print(' ')
radio4 = RadioFM(70, 78)
radio4.ligar()
radio4.mudar_frequencia(45)
radio4.habilitar_antena()
radio4.mudar_frequencia(60)
radio4.frequencia_atual
radio4.mudar_frequencia(89.5)
radio4.estacao_atual
print(' ')

radio5 = RadioFM(45, 89.1)
radio5.ligar()
radio5.habilitar_antena()
radio5.mudar_frequencia()
radio5.volumee