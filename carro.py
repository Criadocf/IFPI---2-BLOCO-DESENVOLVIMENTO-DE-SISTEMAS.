class Carro:
  def __init__(self, nome_param, ano_param, cor_param, velocidade_maxima_param, velocidade_atual_param, estado_param, ):
    self.nome = nome_param
    self.ano = ano_param
    self.cor = cor_param
    self.velocidade_maxima = velocidade_maxima_param
    self.velocidade_atual = velocidade_atual_param
    self.estado = estado_param

  def ligar(self):
    self.estado = True
    print('O carro está ligado')

  def desligar(self):
    self.estado = False
    self.velocidade_atual = 0
    print('O carro está desligado')

  def parar(self):
    self.velocidade_atual = 0
    print('O carro está parado')

  def acelerar(self, velocidade):
    if self.estado == True:
      if (self.velocidade_atual + velocidade) <= self.velocidade_maxima:
        self.velocidade_atual += velocidade
        print(f'A velocidade atual do carro é de {self.velocidade_atual}')
      
      else:
        self.velocidade_atual = self.velocidade_maxima
        print(f'Não é possível ultrapassar 300km/h, portanto a velocidade atual do carro é de {self.velocidade_atual}km/h')
    
    else:
      print('O carro não pode acelerar desligado')


fusca = Carro('fusca', 1965, 'preto', 80, 20, True)

ferrari = Carro('Ferrari_sr2000', '2014', 'vermelho', 300, 0, False)

# a) acelere o fusca para a velocidade 40.
fusca.acelerar(20)

# b) acelere a ferrari para a velocidade: 320
ferrari.ligar()
ferrari.acelerar(200)

# c) desligue o fusca.
fusca.parar()
fusca.desligar()

# d) ligue a ferrari.
ferrari.ligar()

# e) acelere a ferrari para: 320
ferrari.acelerar(320)

# g) desligue a ferrari
ferrari.parar()
ferrari.desligar()

# h)ligue o fusca
fusca.ligar()

# i) acelere o fusca para: 100
fusca.acelerar(100)

# j) desligue o fusca
fusca.parar()
fusca.desligar()
