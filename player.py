import pygame
#Criando uma classe pro player
class Player(pygame.sprite.Sprite):
    def __init__(self, *groups):
        #Configurando os diametros da img do player
        super().__init__(*groups)
        self.image = pygame.transform.scale(self.image, [80, 80])
        self.rect = pygame.Rect(50, 50, 80, 80)
        self.vida = 3  #Defini que o player tem 3 de vida

        #Configurações da movimentação do player
    def update(self, *args):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.rect.y -= 7
        elif keys[pygame.K_s]:
            self.rect.y += 7
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > 480:
            self.rect.bottom = 480
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > 840:
            self.rect.right = 840
