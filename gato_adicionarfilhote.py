#Implemente o método PARIR() parar gerar vários filhotes.
from random import randint as rd, choice, random

populacao = []

class Gato():
    def __init__(self, sexo, fertil, cio, prenhe, puerperio):
        self.sexo = sexo
        self.fertil = fertil
        self.cio = cio
        self.prenhe = False
        self.puerperio = puerperio
        self.nome = None
        self.idade = 0
        self.peso = 0

    def engordar(self, peso):
        self.peso += peso
        print(f'O {self.nome} agora pesa {self.peso} quilo(s)')

    def envelhecer(self):
        self.idade += 1
        if self.idade >= 1:
            self.fertil = True
        print(f'A idade do {self.nome} agora é de {self.idade} ano(s)')

    def entrar_cio(self):
        if self.sexo == 'F' and self.idade >= 1:
            self.cio = True

    def cruzar(self, gato):
        if type(gato) == type(self):
            print('CRUZAMENTO INICIADO...')
            if (self.sexo != gato.sexo) and (self.cio == True or gato.cio == True) and (self.fertil and gato.fertil) and (self.puerperio == False and gato.puerperio == False):
                if self.sexo == 'F':
                    self.prenhe = True
                else:
                    gato.prenhe == True
                print('Deu certo os bichos cruzarem, agora só aguardar as crias')
            
            else:
                print('Falha no cruzamento')
        else:
            print('Digite um animal do tipo válido')


    def parir(self):  # O COMPORTAMENTE PARIR SEMPRE VAI MUDAR UM ESTADO, NESSE CASO, QUAL OU QUAIS?
        if (self.sexo == 'F' and self.prenhe):
          self.prenhe = False
          self.puerperio = True
          filhotes = []
          for c in range(rd(1,8)):
            ##lista_raca = choice(['siames', 'vira-lata', 'cockspainer', 'gatinho angorá'])
            sexo_filhote = choice(['M', 'F'])
            print(f'Sexo do filhote: {sexo_filhote}')
            peso_filhote = random().__round__(2)
            nome_gato = input('DIGITE O NOME DO GATO: ')
            filhotinho = Gato(sexo_filhote, False, False, False, False)
            filhotinho.nome = nome_gato
            filhotinho.peso = peso_filhote
            filhotes.append(filhotinho)
          return filhotes





meia_noite = Gato('M', True, True, False, False)
meia_noite.engordar(0.8)
meia_noite.envelhecer()
populacao.append(meia_noite)

cibelle = Gato('F', True, True, False, False)
cibelle.engordar(2)
cibelle.cruzar(meia_noite)
populacao.append(cibelle)

listagem_filhotes = cibelle.parir()

for c in listagem_filhotes:
    print(c.nome)



