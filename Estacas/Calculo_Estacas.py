import math

solo = ''
k = 0
alfa = 0
diam = 0
estaca = ''
f1 = 0
f2 = 0
prof = 0
nl = 0
np = 0


def recebe_estaca():
    """ATRIBUI OS VALORES DOS FATORES DE PONDERAÇÃO F1(PONTA) E F2(LATERAL) PARA O TIPO DE ESTACA"""

    check = True
    while check:
        global diam, estaca, f1, f2

        diam = float(input("Qual o diâmetro da estaca?(m): "))
        while diam <= 0:
            diam = float(input("O diâmetro tem que ser maior do que 0!\nQual o diâmetro da estaca?(m): "))

        print('Franki(F), Metalica(M), Pre_Moldada(PM), Escavada(E), Raiz, Hélice Continua ou Ômega(RHO)')
        estaca = input("Qual o tipo de estaca a ser utilizada?: ").upper()

        if estaca == 'F':  # Franki = [2.50, 5.00]
            f1 = 2.50
            f2 = 5
            check = False
        elif estaca == 'M':  # Metalica = [1.75, 3.50]
            f1 = 1.75
            f2 = 3.50
            check = False
        elif estaca == 'PM':  # Pre_Moldada = [1+(diam/0,8), 2f1]
            f1 = 1 + (diam / 0.8)
            f2 = 2 * f1
            check = False
        elif estaca == 'E':  # Escavada = [3.00, 6.00]
            f1 = 1.75
            f2 = 3.50
            check = False
        elif estaca == 'RHO':  # Raiz, Hélice Continua ou Ômega = [2, 4]
            f1 = 2.00
            f2 = 4.00
            check = False
        else:
            print('Entrada inválida!')


def recebe_solo():
    """ATRIBUI OS VALORES DE K E RAZÃO DE ATRITO α PARA O TIPO DE SOLO"""
    check = True
    while check:
        global solo, k, alfa
        print('AREIAS -> Areia(A), Areia Siltosa(AS), Areia Silto Argilosa(ASA), Areia Argilosa(AA), Areia Argilo '
              'Siltosa(AAS)\nSILTES -> Silte(S), Silte Arenoso(SA), Silte Areno Argiloso(SAA), Silte Argiloso(SC), '
              'Silte Argilo Arenoso(SCA)\nARGILAS -> Argila(C), Argila Arenosa(CA), Argila Areno Siltosa(CAS), '
              'Argila Siltosa(CS), Argila Silto Arenosa(CSA)')
        solo = (input("Qual o tipo de solo do terreno?: ").upper())
        if solo == 'A':
            k = 1000
            alfa = 0.014
            check = False
        elif solo == 'AS':  # AS = (800, 0.02)
            k = 800
            alfa = 0.02
            check = False
        elif solo == 'ASA':  # ASA = (700, 0.024)
            k = 700
            alfa = 0.024
            check = False
        elif solo == 'AA':  # AA = (600, 0.028)
            k = 600
            alfa = 0.028
            check = False
        elif solo == 'AAS':  # AAS = (500, 0.03)
            k = 500
            alfa = 0.03
            check = False
        elif solo == 'S':  # S = (400, 0.03)
            k = 400
            alfa = 0.03
            check = False
        elif solo == 'SA':  # SA = (550, 0.022)
            k = 550
            alfa = 0.022
            check = False
        elif solo == 'SAA':  # SAA = (450, 0.028)
            k = 450
            alfa = 0.028
            check = False
        elif solo == 'SC':  # SC = (230, 0.034)
            k = 230
            alfa = 0.034
            check = False
        elif solo == 'SCA':  # SCA = (250, 0.03)
            k = 250
            alfa = 0.03
            check = False
        elif solo == 'C':  # C = (200, 0.06)
            k = 200
            alfa = 0.06
            check = False
        elif solo == 'CA':  # CA = (350, 0.024)
            k = 350
            alfa = 0.024
            check = False
        elif solo == 'CAS':  # CAS = (300, 0.028)
            k = 300
            alfa = 0.028
            check = False
        elif solo == 'CS':  # CS = (220, 0.04)
            k = 220
            alfa = 0.04
            check = False
        elif solo == 'CSA':  # CSA = (330, 0.03)
            k = 330
            alfa = 0.03
            check = False
        else:
            print('Entrada inválida')


def calculo():
    """REALIZA O CALCULO DE RESISTENCIA"""
    global prof, nl, np
    prof = float(input("Qual o a profundidade da estaca?(m): "))
    while prof <= 0:
        prof = float(input("A profundidade tem que ser maior do que 0!\nQual o a profundidade da estaca?(m): "))
    nl = float(input("Qual o valor do Nspt da camada a ser avaliada?: "))
    while nl <= 0:
        nl = float(input("O valor de NL tem que ser maior do que 0!\nQual o valor do Nspt da camada a ser avaliada?: "))
    np = float(input("Qual o valor do Nspt da camada de apoio da ponta da estaca?: "))
    while np <= 0:
        np = float(input("O valor de NP tem que ser maior do que 0!\nQual o valor do Nspt da camada de apoio da ponta "
                         "da estaca?: "))

    ap = (math.pi*(math.pow(diam, 2)))/4
    u = math.pi*diam
    rl = (u/f2)*(k*alfa*nl*prof)
    rp = (k*np*ap)/f1
    rt = rl+rp
    ta = rt/2
    tatf = ta/10

    carga = float(input("Qual a solicitada na estaca?(tf): "))
    while carga <= 0:
        carga = float(input("A carga tem que ser maior do que 0!\nQual a solicitada na estaca?(tf): "))

    calc_est = carga/tatf

    if calc_est == 1:
        print('Cada estaca suporta %.3f(tf), Desse modo, será necessária %f estaca para a carga solicitada'%(tatf,math.ceil(calc_est)))
    else:
        print('Cada estaca suporta %.3f(tf), Desse modo, Serão necessárias %i estacas para a carga solicitada'%(tatf,math.ceil(calc_est)))
def main():
    """FUNÇÃO PRINCIPAL DO SISTEMA"""
    print("SEJA BEM VINDO A CALCULADORA DE ESTACAS ELABORADA POR: ENG° RENAN MARTARELLI")

    recebe_solo()
    recebe_estaca()
    calculo()



main()
