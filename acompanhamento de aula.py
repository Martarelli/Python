# class ObjetoGrafico(object):
#     def __init__(self, cor):
#         self.cor = cor
#
#     def area(self):
#         pass
#
#     def perimetro(self):
#         pass
#
#     def info(self):
#         print('%f metros quadrados serão preenchidos com a cor %s' % (self.area(), self.cor))
#
# class Cachorro:
#     nome = 'Rex'
#     cor = 'Marrom'
class Conta(object):
    __total = 10000
    reserva = 0.1

    def __init__(self, ID, saldo):
        self.__ID = ID
        self.saldo = saldo

    def deposito(self, valor):
        self.saldo += valor
        Conta.__total += self.saldo

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            Conta.__total -= valor
        Conta.__imprimeReserva()

    def __imprimeReserva():
        print(Conta.__total * Conta.reserva)


itau = Conta(123, 5000)
itau.deposito(1000)
itau.saque(5000)
