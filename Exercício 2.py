"""
Faça um Programa para uma loja de tintas.

O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados
e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou
em galões de 4 litros, que custam R$ 25,00.

Informe ao usuário as quantidades de tinta a serem compradas e os respectivos
preços em 3 situações:
    comprar apenas latas de 18 litros;
    comprar apenas galões de 4 litros;
    misturar latas e galões, de forma que o preço seja o menor.

Acrescente 10% de folga e sempre arredonde os valores para cima, isto é,
considere latas cheias
    int()
    //
    %
    if
"""
#Entrada de metragem quadrada
area = int(input("Informe os m² a serem pintados: "))

#calculo rendimento da tinta
litros = area//6
if area % 6 > 0:
    litros = litros+1

#calculo litros com sobra

ls = litros*1.1
if ls % litros > 0:
    ls= int(litros * 1.1)+1

#calculo latas e galao

latas = ls//18
if ls % 18 > 0:
    latas = latas+1

galao = ls//4
if ls % 4 > 0:
    galao = galao+1

#calculo monetário

custol = latas*80
custog = galao*25

clts = ls//18
if clts % 18 > 0:
    cgl = 1

cec = clts*80 + cgl*25     #cec= custo economico     clts=custo latas    cgl=custo galao

print(ls)
print("Você vai precisar de",ls,"litros de tinta")
print("Você vai precisar de",latas,"latas de 18L, que custará R$", custol)
print("Você vai precisar de",galao,"galão de 4L, que custará R$",custog)
print("Você pode levar",clts,"latas de 18L e",cgl,"latas de 4L, com um valor total de R$",cec)

