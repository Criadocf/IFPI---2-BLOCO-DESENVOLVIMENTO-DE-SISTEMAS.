class Gato:

  def __init__(self, nome, fertil, cio, prenhe, puerperio, peso, idade, sexo):
        self.nome = nome
        self.fertil = fertil
        self.cio = cio
        self.prenhe = prenhe
        self.puerperio = puerperio
        self.peso = peso
        self.idade = idade
        self.sexo = sexo
        self.filhos = []

  def engordar(self, peso_ganho):
        self.peso = self.peso + peso_ganho
        print("O gato "+self.nome+" engordou " + str(peso_ganho) +
              " kg, e agora seu peso é " + str(self.peso) + " kg.")

  def envelhecer(self):
        self.idade = self.idade + 1
        print('Eu, ' + self.nome + ', completo hoje ' +
              str(self.idade)+' anos de idade.')

  def entrar_no_cio(self):
        if (self.idade >= 1):
            self.cio = True
            print(self.nome + ' entrou no cio.')
        else:
            print('Apenas gatos com 1 ano ou mais podem entrar no cio.')

  def sexos_opostos(self, outro_gato):
        return self.sexo != outro_gato.sexo

  def femea_no_cio(self, outro_gato):
        if (self.sexo == 'F' and self.cio):
            return self
        elif (outro_gato.sexo == 'F' and outro_gato.cio):
            return outro_gato
        return None

  def parir(self):
        if (self.sexo == 'F' and self.prenhe == True):
            self.prenhe = False
            self.puerperio = True
            print(self.nome + ' pariu um filho cujo pai é o ' +
                  self.filhos[-1].pai.nome + '. Ela está agora em estado puerperal.')
        else:
            print(self.nome + ' não pode parir')

  def cruzar(self, outro_gato):
        femeaNoCio = self.femea_no_cio(outro_gato)
        if (not self.sexos_opostos(outro_gato)):
            print('O sexo dos gatos devem ser opostos para o cruzamento.')
        elif (femeaNoCio == None):
            print('A fêmea deve estar no cio.')
        else:
            femeaNoCio.prenhe = True
            filho = Gato("Filho de "+self.nome+" e "+outro_gato.nome,
                         False, False, False, False, 0.1, 0, 'M')
            filho.mae = femeaNoCio
            filho.pai = self if self.sexo == 'M' else outro_gato
            self.filhos.append(filho)
            outro_gato.filhos.append(filho)
            print(self.nome + ' e ' + outro_gato.nome + ' cruzaram')

  def tem_filho_de(self, outro_gato):
        for filho in self.filhos:
            if (filho in outro_gato.filhos):
                print('Eu, ' + self.nome + ', tenho filho de ' +
                      outro_gato.nome + '. O nome dele é ' + filho.nome + '.')
                return True
        print('Eu, ' + self.nome + ', não tenho filho de ' + outro_gato.nome + '.')
        return False


if __name__ == "__main__":
    meianoite = Gato("meianoite", False, True, False, False, 2.0, 3, 'M')
    cibelle = Gato("cibelle", True, False, False, False, 2.0, 3, 'F')
    lorao = Gato("lorao", True, True, False, False, 2.0, 3, 'M')

    # a) Bambino tenta cruzar com o Bambinao
    meianoite.cruzar(lorao)

    # b) Bambino cruza com a Bambina quando ela não está no cio
    meianoite.cruzar(cibelle)

    # c) Bambina entra no cio
    cibelle.entrar_no_cio()

    # d) Bambino cruza com a Bambina quando ela está no cio
    meianoite.cruzar(cibelle)

    # e) Bambina fica preenhe de Bambino
    meianoite.tem_filho_de(cibelle)

    # f) Bambina pariu
    cibelle.parir()

    # g) Bambino engorda 1 kg
    meianoite.engordar(1.0)

    # h) Bambino envelhece 1 ano
    meianoite.envelhecer()

