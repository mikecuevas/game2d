import pygame

#Criei uma classe pro tiro do player, defini a escala, velocidade do tiro
class Tiro(pygame.sprite.Sprite):
    image = pygame.image.load("perso/vacina.png")
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.transform.scale(self.image, [80, 80])
        self.rect = pygame.Rect(50, 50, 50, 50)

        self.speed = 5

#Update da logica do tiro e também defini que se ele sair da largura da tela, o tiro é apagado
    def update(self, *args):
        self.rect.x += self.speed
        if self.rect.left > 840:
            self.kill()

#Criei uma classe para o tiro do Boss, com velocidade, escala, tamanho, de onde o tiro vai sair
class TiroBoss(pygame.sprite.Sprite):
    image = pygame.image.load("perso/coronahd.png")
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.transform.scale(self.image, [45, 45])
        self.rect = pygame.Rect(45, 45, 45, 45)

        self.speed = -5

#Update da logica do tiro do boss, se ele sair do tamanho da tela, o tiro será apagado.
    def update(self, *args):
        self.rect.x += self.speed
        if self.rect.left < 0:
            self.kill()

