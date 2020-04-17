"""vetor = [5]

for i in range (1,6):
    num = int(input("Digite o número %i de 5: "%i))
    vetor.append(num)

print(vetor)

vetor = []
vetor2 = []
for i in range (1,21):
    if i % 2 != 0:
        vetor.append(i)
    else:
        vetor2.append(i)

print(vetor)
print(vetor2)"""
"""lista = []

num = int(input("Digite um número da sequência: "))

while num != -1:
    lista.append(num)
    num = int(input("Digite um número da sequência: "))

elemento = int(input("Digite o elemento a ser procurado: "))


cont = 0

for i in range (len(lista)):
    if lista[i] == elemento:
        cont += 1

print("O elemento %i aparece %i vezes na sequência"%(elemento,lista.count(elemento)))
"""
"""
import random

vetor = []

n = int(input("Digite o número de lançamentos: "))

for i in range (n):
    vetor.append(random.randint(1,6))
for i in range (1,7):
    print("A face %i apareceu %.2f %% vezes."%(i, 100*vetor.count(i)/n))"""
"""
alunos = 10
medias = []

for i in range (1, alunos+1):
    notas = 0
    for j in range (1,5):
        notas += float(input("Digite a nota %i de 4 do aluno %i de %i: "%(j, i, alunos)))

    notas /= 4

    medias.append(notas)

num = 0

for media in medias:
    if media >= 7.0:
        num += 1

print("o número de alunos com media maior que 7 é",num)"""

