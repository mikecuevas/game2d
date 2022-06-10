import pygame

#Defini uma função para escrever na tela do jogo, com tamanhos, tipo de texto, cor, e a tela que vai aparecer
def text_to_screen(screen, text, x, y, tamanho, color = (255, 255, 255)):


    text = str(text)
    #Defini alguns criterios para as letras, como o estilo da letra que é "SansitaOne.tff" e o tamanho.
    font = pygame.font.SysFont("SansitaOne.tff", 30)
    text = font.render(text, True, color)
    screen.blit(text, (x, y))
#Criei uma classe para o menu
class Menu:
    def __init__(self, screen):

        self.active = True
        self.screen = screen
   #Defini uma função onde irá aparecer tudo que eu escrevi no menu inicial, configurei as posições x e y.
    def draw(self):
        text_to_screen(self.screen, "Comandos:", 100, 100, 500)
        text_to_screen(self.screen, "W - UP", 100, 120, 500)
        text_to_screen(self.screen, "S - DOWN", 100, 140, 500)
        text_to_screen(self.screen, "SPACE - SHOOT", 100, 200, 500)
        text_to_screen(self.screen, "Regras:", 400, 100, 500)
        text_to_screen(self.screen, "Tiro e Zumbi causam 1 de dano", 400, 120, 500)
        text_to_screen(self.screen, "Vida do player - 3", 400, 140, 500)
        text_to_screen(self.screen, "Vida do boss - 40", 400, 160, 500)
        text_to_screen(self.screen, "Mate 100 zumbis para chegar ao BOSS", 400, 180, 500)
        text_to_screen(self.screen, "Mate o BOSS para ganhar o JOGO", 400, 200, 500)
        text_to_screen(self.screen, "Selecione o personagem para iniciar o jogo:", 100, 300, 500)
        text_to_screen(self.screen, "Lula (Q)", 100, 320, 500)
        text_to_screen(self.screen, "Bolsonaro (P)", 100, 340, 500)
    #Defini uma função de gameover para criar uma tela onde está escrito GameOver, com o posicionamento x e y.
    def gameover(self):
        text_to_screen(self.screen, "GAME OVER", 330, 200, 300)
