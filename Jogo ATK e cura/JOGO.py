#importa modulo random
import random

#armazenar vida e sp
player_life = 500
player_sp = 100

#vida padrão inimigo
enemy_life = 50

#numero de inimigos
n = int(input("Digite o número de inimigos: "))

#vetor que armazena inimigos
enemies = []

#add ao vetor um vetor com 2 componentes : numero inimigo + hp
for i in range (n):
    enemies.append([i+1,enemy_life])

#Enquanto essa variavel for True estaremos rodando o jogo
jogando = True
while jogando:    #loop do jogo
    #imprime na tela a vida e sp do jogador
    print("Vida:", player_life)
    print("SP:", player_sp)

    #pede para escolher a opção de ação

    atk = int(input("Deseja atacar (1) ou curar (2): "))

    #se escolher atacar
    if atk == 1:
        #escolher aleatoriamente inimigo para ser atacado
        sel_en = random.choice(enemies)
        #determinar o dano causado
        damage = random.randint (10, 15)
        #imprimir informações
        print("Você causou %i de dano ao inimigo %i"%(damage, sel_en[0]))
        #diminuir da vida do inimigo o dano
        sel_en[1] -= damage

        #se HP inimigo zerar
        if sel_en[1] <= 0:
            #informa que inimigo morreu
            print("O inimigo %i morreu!"%sel_en[0])
            #remove inimigo da lista
            enemies.remove(sel_en)

    #Se a escolha foi curar
    else:
        #só pode curar se SP > 10
        if player_sp >= 10:
            #escolhe um valor aleatório para a cura
            heal = random.randint(10,15)
            #informa quanto foi curado
            print("Você recebeu %i pontos de vida!"%heal)
            #adiciona isso a vida do player e diminui SP
            player_life += heal
            player_sp -= 10
        #se SP < 10
        else:
            #imprime que não pode curar
            print("SP insuficiente!")

    #turno dos inimigos
    for enemy in enemies:
        #escolhe se inimigo vai acertar ou errar - 75% de chance de acerto
        hit = bool(random.choice([1, 1, 1, 0]))
        if hit:
            #escolher dano causado ao player
            dam_en = random.randint(1,3)
            #imprime o dano
            print("O inimigo %i causou %i de dano!"%(enemy[0], dam_en))
            #diminui vida do player
            player_life -= dam_en
        else:
            #informar que inimigo errou
            print("O inimigo %i errou o ataque!"%enemy[0])

    #aumentar o SP do player
    if player_sp < 100:
        #aumenta 3 a cada rodada
        player_sp += 3
    #player n pode ter mais de 100 de SP
    if player_sp > 100:
        player_sp = 100

    #se a vida acabar
    if player_life <= 0:
        print("Você perdeu, Game Over T.T")
        jogando = False
    #se numero de inimigos zerar ele ganha
    if len(enemies) == 0:
        print("You done! Você matou todos os inimigos ^.^")
        jogando = False
