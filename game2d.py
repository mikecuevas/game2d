import pygame
import random
from player import Player
from zumbi import Zumbi, Boss
from tiro import Tiro
from menu import Menu, text_to_screen


#Iniciando o Jogo e criando o display.
pygame.init()
display = pygame.display.set_mode([840, 480]) #840 e 480 são os paramtros de largura e altura.



#Objetos do jogo(sprites):
drawGroup = pygame.sprite.Group()
zombieGroup = pygame.sprite.Group()
tiroGroup = pygame.sprite.Group()
playerGroup = pygame.sprite.Group()
bosstiroGroup = pygame.sprite.Group()
bossGroup = pygame.sprite.Group()


#Configurações do plano de fundo do display (background):
bg = pygame.sprite.Sprite(drawGroup)
bg.image = pygame.image.load("perso/riodejaneiro.jpg")
bg.image = pygame.transform.scale(bg.image, [840, 480])
bg.rect = bg.image.get_rect()


#Som do Jogo:
pygame.mixer.music.load("perso/Omae Wa Mou.mp3")
pygame.mixer.music.play(-1)
somtiro = pygame.mixer.Sound("perso/ah_rXlbB2E.mp3")


#Configurações do display do jogo:
def desenhoTela():

    drawGroup.draw(display)
    text_to_screen(display, f"PONTOS: {pontos}", 50, 10, 100)
    if Boss_ativo:
        text_to_screen(display,f"VIDA DO BOSS: {boss.vida}", 200, 10, 100)
pontos = 0



#Configurações da lógica do jogo:
gameover = False

clock = pygame.time.Clock()

player = 0

timer = 0

janela_do_jogo = True

menu = Menu(display)

sprite_player = 0

sprite_inimigo = 0

contador_zumbi = 0

Boss_ativo = False

#Loop do jogo:
while janela_do_jogo:
    clock.tick(60)     #Para definir um fps
    for event in pygame.event.get(): #Aqui eu utilizei um for para definir alguns parametros
        if event.type == pygame.QUIT: #para o jogo fechar
            janela_do_jogo = False
        elif event.type == pygame.KEYDOWN and gameover == False: #Utilizei o KEYDOWN para detectar se uma tecla foi pressionada
            if event.key == pygame.K_SPACE: #Aqui defini que quando for pressionado o espaço, o personagem
                somtiro.play()              #irá atirar e defini o som que sai quando acontecer tal interação
                novoTiro = Tiro(drawGroup, tiroGroup)
                novoTiro.rect.center = player.rect.center #Utilizei esse comando para definir que o tiro irá sair do centro do personagem.
            elif event.key == pygame.K_p:      #Caso seja pressionado a tecla "p", escolhe um personagem
                if menu.active:
                    bolsonaro = pygame.image.load("perso/bolsonarohd.png")
                    Player.image = bolsonaro   #Desenha o personagem escolhido
                    player = Player(drawGroup)
                    sprite_inimigo = pygame.image.load("perso/zombiehd.png")
                    Zumbi.image = sprite_inimigo  #Desenha o inimigo
                    menu.active = False
            elif event.key == pygame.K_q:   #Caso seja pressionado a tecla "q", seleciona um personagem
                if menu.active:
                    lula = pygame.image.load("perso/lulahd.png")
                    Player.image = lula     #Desenha o personagem escolhido
                    player = Player(drawGroup)
                    sprite_inimigo = pygame.image.load("perso/zombiehd.png")
                    Zumbi.image = sprite_inimigo  #Desenha o inimigo
                    menu.active = False

    # Para criar uma tela inicial definido pela sprite
    if menu.active:
        display.fill([0, 0, 0])
        if gameover == True:
            menu.gameover()
        else:
            menu.draw()
        pygame.display.update()
        continue

    #Update da logica do jogo
    drawGroup.update()

    timer += 1
    if timer > 30:  #Aqui significa que a cada meio segundo(metade do fps) existe a possibilidade de surgir um zumbi novo
        timer = 0
        if random.random() < 0.8 and Boss_ativo == False: #Coloquei 0.8 para criar 80% de chance de surgir um zumbi novo a cada meio segundo
            newZumbi = Zumbi(drawGroup, zombieGroup)      #Desenha o zumbi

        if random.random()< 0.5 and Boss_ativo == True:  #Como no caso do zumbi, existe 50% de chance do Boss atirar um tiro novo
            boss.atirar(drawGroup, bosstiroGroup)        #Desenha o boss



    #Defini a colisão entre o Player e o Zumbi
    colisao = pygame.sprite.spritecollide(player, zombieGroup, True, pygame.sprite.collide_mask)
    if colisao:  #Caso aconteça a colisão, o player irá perder 1 de vida
            player.vida -= 1
            print(player.vida)
            if player.vida == 0:  #Se a vida do player chegar a Zero
                menu.active = True#O jogo vai para a tela de GameOver
                gameover = True

    # Aqui eu defini a colisão entre o tiro do player e Zumbi
    tiros = pygame.sprite.groupcollide(tiroGroup, zombieGroup, True, True, pygame.sprite.collide_mask)
    if tiros:  #Caso aconteça a colisão entre o tiro e o zumbi, o zumbi é deletado e soma 1 ponto na pontuação
        pontos += 1
        if pontos == 100: #Defini 100 pontos para que o boss possa surgir, ou seja, o player precisa matar 100 zumbis
            boss = Boss(drawGroup, bossGroup)
            Boss_ativo = True

    #Defini também a colisão entra o tiro do Boss e player, se repete o mesmo caso se ocorrer a colisão do zumbi com o player
    tiroboss = pygame.sprite.spritecollide(player, bosstiroGroup, True , pygame.sprite.collide_mask)
    if tiroboss: #Como anteriormente, caso o tiro do boss pegue no player, ele perde 1 de vida
        player.vida -= 1
        print(player.vida)
        if player.vida == 0: #Se chegar a zero o jogo vai para a tela de GameOver
            menu.active = True
            gameover = True

    #Além disso, defini o tiro do player quando pega no Boss
    playerboss = pygame.sprite.groupcollide(tiroGroup, bossGroup, True, False, pygame.sprite.collide_mask)
    if playerboss:  #Se o tiro do player pegar no boss, ele perde 1 de vida
        boss.vida -= 1
        print(boss.vida)
        if boss.vida == 0: #Quando a vida do boss chegar a zero, o jogo muda para a tela de GameOver
            boss.kill()
            menu.active = True
            gameover = True

    desenhoTela()
    pygame.display.update()
