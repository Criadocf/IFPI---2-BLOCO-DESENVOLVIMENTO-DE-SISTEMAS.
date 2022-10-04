class Pessoa:
  def __init__(self, nome, idade, peso, altura, sexo, estado_civil='solteiro(a)', conjuge=None):
    self.__nome = nome #SÓ GET
    self.__idade = idade #SÓ GET
    self.__peso = peso #SÓ GET
    self.__altura = altura #SÓ GET
    self.__sexo = sexo #SÓ GET
    self.__vivo = True # SÓ GET
    self.__estado_civil = estado_civil #SÓ GET
    self.__conjuge = conjuge #SÓ GET


  @property
  def nome(self):
    return self.__nome
  
  @property
  def idade(self):
    if self.__vivo == True:
      return self.__idade
    else:
      print(f'{self.__nome} está morto.')

  @idade.setter
  def idade(self,idade):
    print('sem permissão')

  @property
  def peso(self):
    return self.__peso

  @property
  def altura(self):
    return self.__altura

  @property
  def sexo(self):
    return self.__sexo

  @property
  def vivo(self):
    return self.__vivo

  @property
  def estado_civil(self):
    return self.__estado_civil

  @property
  def conjuge(self):
    return self.__conjuge

  def envelhecer(self):
    if self.__vivo != False:
      self.__idade += 1
      if self.__idade < 21:
        self.__altura += 5
    print(f'{self.nome} está com {self.idade} anos e {self.altura} cm de altura')
  

  def engordar(self, peso):
    if self.__vivo != False:
      self.__peso += peso
    else:
      print(f'Operação não realizada. {self.nome} está morta.')

  def emagrecer(self, peso):
    if self.__vivo != False:
      self.__peso -= peso 

  def crescer(self, altura):
    if self.__vivo != False:
      if self.__idade <= 21:
        self.__altura += altura
      else:
        print(f'{self.nome} não pode mais crescer pois está com 21 anos ou mais')


  def casar(self, alguem):
    if type(self) == type(alguem):
      if self.__vivo and alguem.vivo == True:
        if self.__idade and alguem.idade >= 18:
          if self.__estado_civil == 'solteiro(a)' and alguem.estado_civil == 'solteiro(a)':
            self.__estado_civil = 'casado(a)'
            self.__conjuge = alguem
            alguem.__conjuge = self
            if self.__sexo == 'F':
              print(f'{self.nome} está casada com {alguem.nome}.')
            elif self.__sexo == 'M':
              print(f'{self.nome} está casado com {alguem.nome}.')
          else:
            print(f'{self.nome} está casado com {alguem.nome}')
        else:
          print(f'Casamento não permitido. {alguem.nome} é de menor.')
      else:
        print(f'Casamento não realizado. {self.nome} está morto.')
        
  
  def morrer(self):
    if self.__vivo!= False:
      if self.__conjuge != None:
        self.__conjuge.__estado_civil = 'viúvo(a)'
        self.__conjuge.__conjuge = None
        self.__vivo = False
      else:
        self.__vivo = False
      print(f'{self.__nome} morreu')



maria = Pessoa('Maria', 5, 20, 100,'F')

joao = Pessoa('João',12,40,140,'M')

pedro = Pessoa('Pedro', 22, 65, 170, 'M')

bia = Pessoa('Bia', 18, 55, 160, 'F')

julia = Pessoa('Julia', 30, 65, 170, 'F')

carlos = Pessoa('Carlos', 2, 11, 80, 'M')

jonas = Pessoa('Jonas', 34, 70, 180, 'M')

#a)
maria.idade = 10

#b)
maria.envelhecer()
maria.altura

#c)
pedro.crescer(2)

#d)
bia.casar(carlos)

#e)
pedro.casar(maria)

#f)
pedro.casar(julia)

#g)
pedro.casar(bia)

#h)
maria.morrer()

#i)
maria.engordar(40)

#j)
bia.casar(jonas)

#k)
bia.morrer()

#l)
pedro.morrer()

#m)
jonas.casar(julia)

#n)
pedro.casar(bia)

#o)
pedro.idade

#p)
joao.idade = 50

