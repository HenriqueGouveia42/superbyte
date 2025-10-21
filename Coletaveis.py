import pygame
import random

class Coletaveis:

    def __init__(self, tela):
        
        self.visivel = False
        self.pos_x = -40
        self.pos_y = tela.get_height()/2
        self.tela = tela
        self.gerarColetavel()

    def gerarColetavel(self):

        self.imagem_relogio = pygame.image.load("images/relogio.png")
        self.imagem_invencibilidade = pygame.image.load("images/estrelinha.png")
        self.rect = pygame.Rect(self.pos_x, self.pos_y, 20,20)
        self.definirTipoDeColetavel()

        
    
    def definirTipoDeColetavel(self):
    
        number = random.randint(1,100)

        if number >= 1 and number <= 50:
            self.tipo = 'relogio'
        else:
            self.tipo = 'invencibilidade'
    
    def desenharColetavel(self):

        if self.tipo == 'relogio':
            imagem_coletavel = self.imagem_relogio
        elif self.tipo == 'invencibilidade':
            imagem_coletavel = self.imagem_invencibilidade

        self.rect = pygame.Rect(self.pos_x, self.pos_y, 20,20)
        if self.pos_x <= -40:
            self.visivel = False

        self.tela.blit(imagem_coletavel, self.rect)

    
    def teleportarColetavelParaDireita(self, distancia_entre_obstaculos, altura_topo_obstaculo, margem_obstaculo, personagem):

        chance = random.randint(1,100)

        if chance >=1 and chance <= 50 and self.visivel == False:

            self.definirTipoDeColetavel()

            largura_tela = self.tela.get_width()

            self.pos_x = largura_tela + (distancia_entre_obstaculos/2) + 40
            
            self.pos_y = altura_topo_obstaculo + (margem_obstaculo/2)
            
            self.visivel = True
            
    def reiniciaPosicao(self):
        self.visivel = False
        self.pos_x = -40
    
    def desenhar_inventario(self, tela, coletados, icone_estrelinha, icone_relogio):
        fonte_inv = pygame.font.Font('fonts/04B_19.TTF', 28)

        # Posição inicial
        x = 10
        y = 50

        # Estrelinha
        tela.blit(icone_estrelinha, (x, y))
        texto_estrelinha = fonte_inv.render(str(coletados['estrelinha']), True, (255, 255, 255))
        tela.blit(texto_estrelinha, (x + 50, y + 5))

        # Relógio
        tela.blit(icone_relogio, (x, y + 60))
        texto_relogio = fonte_inv.render(str(coletados['relogio']), True, (255, 255, 255))
        tela.blit(texto_relogio, (x + 50, y + 65))
