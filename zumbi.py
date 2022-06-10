import pygame
import random
from tiro import TiroBoss

#Criando uma classe para o Zumbi:
class Zumbi(pygame.sprite.Sprite):
    def __init__(self, *groups):
        #Definições do zumbi, como escala, velocidade, locais onde vai spawnar zumbi na tela do jogo
        super().__init__(*groups)
        self.image = pygame.image.load("perso/zombiehd.png")
        self.image = pygame.transform.scale(self.image, [100, 100])
        self.rect = pygame.Rect(50, 50, 100, 100)
        self.rect.x = 840
        self.rect.y = random.randint(1, 400)
        self.speed = 7
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > 480:
            self.rect.bottom = 480
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > 840:
            self.rect.right = 840
    #Update das configurações do Zumbi e se ele sair do tamanho da tela, o zumbi é apagado
    def update(self, *args):
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.kill()
#Criando uma classe para o Boss
class Boss(pygame.sprite.Sprite):
    def __init__(self, *groups):
        # Definições do Boss, como escala, velocidade, movimentação do boss que é pra cima e pra baixo.
        super().__init__(*groups)
        self.image = pygame.image.load("perso/zombiehd.png")
        self.image = pygame.transform.scale(self.image, [150, 150])
        self.rect = pygame.Rect(50, 50, 150, 150)
        self.rect.x = 840
        self.rect.y = random.randint(1, 400)
        self.speed = 3
        self.vida = 40
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > 480:
            self.rect.bottom = 480
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > 840:
            self.rect.right = 840
    #Update da logica do boss
    def update(self, *args):
        self.rect.y -= self.speed
        if self.rect.bottom > 480 and self.speed < 0:
            self.speed = -self.speed
        if self.rect.top < 0 and self.speed > 0:
            self.speed = -self.speed
    #Aqui eu defini uma função de tiro do boss.
    def atirar(self, drawGroup, tiroGroup):
        novoTiro = TiroBoss(drawGroup, tiroGroup)
        novoTiro.rect.center = self.rect.center

