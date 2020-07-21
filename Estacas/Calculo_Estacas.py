from Mod_Estaca import *  # importação dos dados das estacas
from Mod_Solos import *  # importação dos dados dos solos


def recebe_estaca():
    """ATRIBUI OS VALORES DOS FATORES DE PONDERAÇÃO F1(PONTA) E F2(LATERAL) PARA O TIPO DE ESTACA"""


def recebe_solo():
    """ATRIBUI OS VALORES DE K E RAZÃO DE ATRITO α PARA O TIPO DE SOLO"""
    print('AREIAS -> Areia(A), Areia Siltosa(AS), Areia Silto Argilosa(ASA), Areia Argilosa(AA), Areia Argilo '
          'Siltosa(AAS)\nSILTES -> Silte(S), Silte Arenoso(SA), Silte Areno Argiloso(SAA), Silte Argiloso(SA), '
          'Silte Argilo Arenoso(SCA)\nARGILAS -> Argila(C), Argila Arenosa(CA), Argila Areno Siltosa(CAS), '
          'Argila Siltosa(CS), Argila Silto Arenosa(CSA)')
    solo =input("Qual o tipo de solo do terreno?: ").upper()
    print(solo)
    print(A[0])
    print(A[1])
def calculo():
    """REALIZA O CALCULO DE RESISTENCIA"""


def main():
    """FUNÇÃO PRINCIPAL DO SISTEMA"""
    print("SEJA BEM VINDO A CALCULADORA DE ESTACAS ELABORADA POR: ENG° RENAN MARTARELLI")

    recebe_solo()
    # diam = input("Qual o diâmetro da estaca?(m): ")
    # prof = input("Qual o a profundidade da estaca?(m): ")
    # nl = input("Qual o valor do Nspt da camada a ser avaliada?: ")
    # np = input("Qual o valor do Nspt da camada de apoio da ponta da estaca?: ")
    # recebe_estaca()


main()
