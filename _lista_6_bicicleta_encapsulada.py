class Bicicleta:
  def __init__(self, peso, altura, cor, veloc_atual=0, altura_cela=0, calibragem_pneus=20):
    self.peso = peso
    self.altura = altura
    self.cor = cor
    self.__veloc_atual = veloc_atual
    self.altura_cela = altura_cela
    self.calibragem_pneus = calibragem_pneus
    self.calibragem_pneus_maxima = 30
    self.veloc_max = 50
  
  @property
  def velocidade_atual(self):
    return self.__veloc_atual

  @velocidade_atual.setter
  def velocidade_atual(self, velocidade):
    if velocidade > 1:
      self.__veloc_atual += velocidade
      if self.__veloc_atual > self.veloc_max:
        self.__veloc_atual = self.veloc_max
    print(f'A velocidade da bicicleta é de {self.__veloc_atual}km/h')
    

  def parar(self):
    if self.__veloc_atual == 0:
      print('A bicicleta já está parada')
    else:
      self.__veloc_atual = 0
      print('a bicicleta está parada')

  def calibrar(self, calibrada):
      self.calibragem_pneus += calibrada
      if self.calibragem_pneus > self.calibragem_pneus_maxima:
        self.calibragem_pneus = self.calibragem_pneus_maxima
      if self.calibragem_pneus > 0:
        print(f'A calibragem dos pneus é de {self.calibragem_pneus}psi.')
      else:
        print('Você só pode secar seus pneus até 0 psi')

bicicleta1 = Bicicleta(14, 1.85, 'preta',50)
bicicleta1.velocidade_atual

