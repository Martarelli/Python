# importação dos dados de solos e estacas

from Solos.Solos_parametros import *
from Estaca.Estacas_parametros import *


def recebe_estaca():
    """ATRIBUI OS VALORES DOS FATORES DE PONDERAÇÃO F1(PONTA) E F2(LATERAL) PARA O TIPO DE ESTACA"""
    print('Franki(F), Metalica(M), Pre_Moldada(PM), Escavada(E), Pre_Moldada_Pqna(PMP)')
    estaca = input("Qual o tipo de estaca a ser utilizada?: ")


def recebe_solo():
    """ATRIBUI OS VALORES DE K E RAZÃO DE ATRITO α PARA O TIPO DE SOLO"""

    print(
        'AREIAS -> Areia(A), Areia Siltosa(AS), Areia Silto Argilosa(ASA), Areia Argilosa(AA), Areia Argilo Siltosa(AAS)\nSILTES -> Silte(S), Silte Arenoso(SA), '
        'Silte Areno Argiloso(SAA), Silte Argiloso(SA), Silte Argilo Arenoso(SCA)\nARGILAS -> Argila(C), Argila Arenosa(CA), Argila Areno Siltosa(CAS), '
        'Argila Siltosa(CS), Argila Silto Arenosa(CSA)')
    solo = input("Qual o tipo de solo do terreno?: ")

    

    K =  solo(0)
    alfa = solo(1)
    return K, alfa


def main():
    """FUNÇÃO PRINCIPAL DO SISTEMA"""

    solo = recebe_solo()


main()
