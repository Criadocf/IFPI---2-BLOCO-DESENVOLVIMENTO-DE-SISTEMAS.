#1. BICICLETA COM PARÂMETROS OPCIONAIS.
class Bicicleta:
  def __init__(self, peso, altura, cor, veloc_atual=0, altura_cela=0, calibragem_pneus=20):
    self.peso = peso
    self.altura = altura
    self.cor = cor
    self.veloc_atual = veloc_atual
    self.altura_cela = altura_cela
    self.calibragem_pneus = calibragem_pneus
    self.calibragem_pneus_maxima = 30
    self.veloc_max = 50
  
  def acelerar(self, velocidade):
    if velocidade > 1:
      self.veloc_atual += velocidade
      if self.veloc_atual > self.veloc_max:
        self.veloc_atual = self.veloc_max
    print(f'A velocidade da bicicleta é de {self.veloc_atual}km/h')

  def parar(self):
    if self.veloc_atual == 0:
      print('A bicicleta já está parada')
    else:
      self.veloc_atual = 0
      print('a bicicleta está parada')

  def calibrar(self, calibrada):
      self.calibragem_pneus += calibrada
      if self.calibragem_pneus > self.calibragem_pneus_maxima:
        self.calibragem_pneus = self.calibragem_pneus_maxima
      if self.calibragem_pneus > 0:
        print(f'A calibragem dos pneus é de {self.calibragem_pneus}psi.')
      else:
        print('Você só pode secar seus pneus até 0psi')



bicicleta2 = Bicicleta(15,1.50,'roxa')
bicicleta2.calibrar(-90)

bicicleta1 = Bicicleta(12, 1.43, 'preta/amarelo',35)
bicicleta1.acelerar(30)
bicicleta1.parar()
bicicleta1.parar()





