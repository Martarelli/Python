import math
from Estacas.datas import *

k = 0
alfa = 0
f1 = 0
f2 = 0
prof = 0
nl = 0
np = 0
carga = 0
cond = ''


def recebe_estaca():
    """ATRIBUI OS VALORES DOS FATORES DE PONDERAÇÃO F1(PONTA) E F2(LATERAL) PARA O TIPO DE ESTACA"""

    check = True
    while check:
        global diam, f1, f2

        print('Franki(F), Metalica(M), Pre_Moldada(PM), Escavada(E), Raiz, Hélice Continua ou Ômega(RHO)')
        est = input("Qual o tipo de estaca a ser utilizada?: ").upper()

        if est == "F" or est == "M" or est == "E" or est == "RHO":
            estesc = estaca[est]
            f1 = estesc[0]
            f2 = 2*f1
            check = False
        elif est == "PM":
            f1 = 1 + (diam / 0.8)
            f2 = 2*f1
            check = False
        else:
            print('Entrada inválida!')


def recebe_solo():
    """ATRIBUI OS VALORES DE K E RAZÃO DE ATRITO α PARA O TIPO DE SOLO"""
    check = True
    while check:
        global k, alfa
        print('AREIAS -> Areia(A), Areia Siltosa(AS), Areia Silto Argilosa(ASA), Areia Argilosa(AA), Areia Argilo '
              'Siltosa(AAS)\nSILTES -> Silte(S), Silte Arenoso(SA), Silte Areno Argiloso(SAA), Silte Argiloso(SC), '
              'Silte Argilo Arenoso(SCA)\nARGILAS -> Argila(C), Argila Arenosa(CA), Argila Areno Siltosa(CAS), '
              'Argila Siltosa(CS), Argila Silto Arenosa(CSA)')
        solo_escolha = input("Qual o tipo de solo do terreno?: ").upper()

        if solo_escolha == 'A' or solo_escolha == 'AS' or solo_escolha == 'ASA' or solo_escolha == 'AA' or\
                solo_escolha == 'AAS' or solo_escolha == 'S' or solo_escolha == 'SA' or solo_escolha == 'SAA' or\
                solo_escolha == 'SC' or solo_escolha == 'SCA'or solo_escolha == 'C'or solo_escolha == 'CA' or\
                solo_escolha == 'CAS' or solo_escolha == 'CS' or solo_escolha == 'CSA':
            se = solo[solo_escolha]
            k = se[0]
            alfa = se[1]
            check = False
        else:
            print('Entrada inválida" Tente novamente')


def calculo():
    """REALIZA O CALCULO DE RESISTENCIA"""

    ap = (math.pi * (math.pow(diam, 2))) / 4
    u = math.pi * diam
    rl = (u / f2) * (k * alfa * nl * prof)
    rp = (k * np * ap) / f1
    rt = rl + rp
    ta = rt / 2
    tatf = ta / 10

    calc_est = carga / tatf

    if calc_est == 1:
        print('Cada estaca suporta %.3f(tf), Desse modo, será necessária %f estaca para a carga solicitada' % (
            tatf, math.ceil(calc_est)))
    else:
        print('Cada estaca suporta %.3f(tf), Desse modo, Serão necessárias %i estacas para a carga solicitada' % (
            tatf, math.ceil(calc_est)))


def main():
    """FUNÇÃO PRINCIPAL DO SISTEMA"""
    print("SEJA BEM VINDO A CALCULADORA DE ESTACAS ELABORADA POR: ENG° RENAN MARTARELLI")

    global diam, prof, nl, np, carga, cond
    rodando = True
    while rodando:
        diam = float(input("Qual o diâmetro da estaca?(m): "))
        while diam <= 0:
            diam = float(input("O diâmetro tem que ser maior do que 0!\nQual o diâmetro da estaca?(m): "))
        recebe_estaca()
        recebe_solo()

        prof = float(input("Qual o a profundidade da estaca?(m): "))
        while prof <= 0:
            prof = float(input("A profundidade tem que ser maior do que 0!\nQual o a profundidade da estaca?(m): "))
        nl = float(input("Qual o valor do Nspt da camada a ser avaliada?: "))
        while nl <= 0:
            nl = float(
                input("O valor de NL tem que ser maior do que 0!\nQual o valor do Nspt da camada a ser avaliada?: "))
        np = float(input("Qual o valor do Nspt da camada de apoio da ponta da estaca?: "))
        while np <= 0:
            np = float(
                input("O valor de NP tem que ser maior do que 0!\nQual o valor do Nspt da camada de apoio da ponta "
                      "da estaca?: "))
        carga = float(input("Qual carga a solicitada na estaca?(tf): "))
        while carga <= 0:
            carga = float(input("A carga tem que ser maior do que 0!\nQual a solicitada na estaca?(tf): "))
        calculo()
        cond = input('Você deseja trocar algum dado(T) ou sair(S): ').upper()
        if cond == 'S':
            break
        elif cond == 'T':
            break
        else:
            cond = input('Opção Inválida!!!\nVocê deseja trocar algum dado(T) ou sair(S): ')



main()
