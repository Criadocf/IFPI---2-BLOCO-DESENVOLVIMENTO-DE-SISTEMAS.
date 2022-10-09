##PROVA DO 1º BIMESTRE DE PROGRAMAÇÃO ORIENTADA A OBJETOS.
##DUPLA: KLEBER JUNIOR E JONATAS LAERT.
from datetime import datetime

class CartaoCredito:
    def __init__(self, numero, titular, mes_validade, ano_validade, cod_seguranca, limite_compras=100.0):
        self.__numero = numero
        self.__titular = titular
        self.__mes_validade = mes_validade
        self.__ano_validade = ano_validade
        self.__cod_seguranca = cod_seguranca
        self.__senha = None
        self.__fatura_a_pagar = 0
        self.__status = 'bloqueado'
        self.__limite_compras = limite_compras
        self.__valor_minimo_a_pagar = 0.3 * self.__fatura_a_pagar

    @property
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular

    @property
    def ano_validade(self):
        return self.__ano_validade

    @property
    def mes_validade(self):
        return self.__mes_validade

    @property
    def cod_seguranca(self):
        return self.__cod_seguranca

    @property
    def senha(self):
        return self.__senha

    @property
    def fatura_a_pagar(self):
        return self.__fatura_a_pagar

    @property
    def status(self):
        return self.__status

    @property
    def limite_compras(self):
        return self.__limite_compras

    def desbloquear(self):
        self.__status = 'liberado'
        print('O cartão está desbloqueado')

    def bloquear(self):
        self.__status = 'bloqueado'
        print('O cartão está bloqueado')


    def mudar_senha(self):
        codigo_seguranca = input('DIGITE O CÓDIGO DO CARTÃO: ')
        if codigo_seguranca == self.__cod_seguranca:
            senha_cartao = input('DIGITE A SENHA DO CARTÃO: ')
            self.__senha = senha_cartao
            return 'A SENHA FOI ALTERADA COM SUCESSO'
        else:
            return 'O CÓDIGO FOI DIGITADO ERRADO'

    def cartao_vencido(self):
        cardYear = self.__ano_validade
        cardMonth = self.__mes_validade

        currentMonth = datetime.now().month
        currentYear = datetime.now().year

        return cardYear < currentYear or cardMonth < currentMonth

    def validar_compra(self, valor_compra):
        if self.__limite_compras < valor_compra:
            return "O valor da compra deve ser menor ou igual ao limite de compras."
        if self.__status == 'bloqueado':
            return "O cartão deve estar desbloqueado."
        if self.cartao_vencido():
            return "O cartão não pode estar vencido na data da compra."
        return None

    def comprar(self, valor_compra):
        erro = self.validar_compra(valor_compra)
        if (erro == None):
            if self.__senha == None:
                retorno = self.mudar_senha()
                if (retorno == 'A SENHA FOI ALTERADA COM SUCESSO'):
                    senha = input('Digite a senha: ')
                    if (self.__senha != senha):
                        print('Senha incorreta.')
                    else:
                        self.__limite_compras -= valor_compra
                        self.__fatura_a_pagar += valor_compra
                        self.__valor_minimo_a_pagar = 0.30 * self.__fatura_a_pagar
            else:
              senha = input('Digite a senha: ')
              if (self.__senha != senha):
                  print('Senha incorreta.')
              else:
                  self.__limite_compras -= valor_compra
                  self.__fatura_a_pagar += valor_compra
                  self.__valor_minimo_a_pagar = 0.30 * self.__fatura_a_pagar
        else:
            print(erro)

    # def valor_parcial_ou_total(self):
    #     try:
    #         valor = int(input('Digite se você quer pagar o valor parcial ou total [0 - Parcial; 1 - Total]: '))
    #         if (valor != 0 and valor != 1):
    #             print('Opção inválida. Tente novamente.')
    #             self.valor_parcial_ou_total()
    #         return valor
    #     except:
    #         print('Opção inválida. Tente novamente.')
    #         self.valor_parcial_ou_total()

    def validar_pagamento_fatura(self, valor):
        if valor < self.__valor_minimo_a_pagar:
            return "O valor a ser pago deve ser maior ou igual ao valor mínimo."
        if self.fatura_a_pagar == 0:
            return "Não há saldo em aberto nesta fatura."
        return None

    def pagar_fatura(self, valor):
        # pagamento_total = self.valor_parcial_ou_total()
        erro = self.validar_pagamento_fatura(valor)
        if (erro == None):
            self.__fatura_a_pagar -= valor
            self.__limite_compras += valor
            self.__valor_minimo_a_pagar = 0.30 * self.__fatura_a_pagar
        else:
            print(erro)

    def __str__(self):
        return 'Número do cartão: %s\nNome do titular: %s\nValor da fatura: %.2f\nValor mínimo a pagar: %.2f\n' % (self.numero, self.titular, self.fatura_a_pagar, self.__valor_minimo_a_pagar)

#__init__(self, numero, titular, validade, cod_seguranca, limite_compras=100):
if __name__ == '__main__':

    print('Operações com o PicPay:')
    meu_picpay = CartaoCredito('111', 'Jonatas Laet', 10, 2030, '940', 500.0)
    meu_picpay.comprar(500.0)
    meu_picpay.desbloquear()
    # meu_picpay.comprar(500.0)
    meu_picpay.fatura_a_pagar
    meu_picpay.senha
    # print('\nOperações com o NuBank:')
    # meu_nubank = CartaoCredito('112', 'Jonatas Laet', '09/2030', '941', 500.0)
    # meu_nubank.comprar(600.0)
    # meu_nubank.comprar(499.0)
    # meu_nubank.desbloquear()
    # meu_nubank.comprar(499.0)
    # meu_nubank.pagar_fatura(333.3)

    # print('\nOperações com o Inter:')
    # meu_inter = CartaoCredito('113', 'Jonatas Laet', '08/2030', '942', 500.0)
    # meu_inter.comprar(600.0)
    # meu_inter.comprar(499.0)
    # meu_inter.desbloquear()
    # meu_inter.comprar(499.0)
    # meu_inter.pagar_fatura(333.3)

    # print('\nOperações com o CEF:')
    # meu_cef = CartaoCredito(114, 'Jonatas Laet', '07/2030', '943', 500.0)
    # meu_cef.comprar(601.0)
    # meu_cef.comprar(499.1)
    # meu_cef.desbloquear()
    # meu_cef.comprar(499.1)
    # meu_cef.pagar_fatura(333.4)

    # print()
    # print(meu_picpay)
    # print()
    # print(meu_nubank)
    # print()
    # print(meu_inter)
    # print()
    # print(meu_cef)