import pygame
from pygame.locals import *
from sys import exit

relogio = pygame.time.Clock()


class Telas:

    def __init__(self, font_path, font_size, largura_tela_principal, altura_tela_princial, superficie_tela_principal):

        self.font_path = font_path
        self.font_size = font_size
        self.largura_tela_principal = largura_tela_principal
        self.altura_tela_princial = altura_tela_princial
        self.superficie_tela_principal = superficie_tela_principal

    def getSuperficieTelaPrincipal(self):
        return self.superficie_tela_principal
    
    def getLarguraTelaPrincipal(self):
        return self.largura_tela_principal

    def getAlturaTelaPrincipal(self):
        return self.altura_tela_princial
    
    def getFontPath(self):
        return self.font_path

    def getFontSize(self):
        return self.font_size
    
    def setLarguraTelaPrincipal(self, largura):
        self.largura_tela_principal = largura
    
    def setAlturaTelaPrincipal(self, altura):
        self.altura_tela_princial = altura

    def tela_inicial(self):
        fonte_titulo = pygame.font.Font('fonts/04B_19.TTF', 72)
        fonte_botao = pygame.font.Font('fonts/04B_19.TTF', 36)

        largura_botao = 300
        altura_botao = 70
        x_botao = (self.largura_tela_principal - largura_botao) // 2
        y_botao = (self.altura_tela_princial - altura_botao) // 2
        botao = pygame.Rect(x_botao, y_botao, largura_botao, altura_botao)

        esperando_clique = True
        while esperando_clique:
            self.superficie_tela_principal.fill((30, 30, 30))

            # Título
            texto_titulo = fonte_titulo.render("FLAPPY BYTE", True, (255, 255, 0))
            rect_titulo = texto_titulo.get_rect(center=(self.largura_tela_principal//2, 150))
            self.superficie_tela_principal.blit(texto_titulo, rect_titulo)

            # Botão
            pygame.draw.rect(self.superficie_tela_principal, (0, 120, 250), botao, border_radius=15)
            texto = fonte_botao.render("INICIAR JOGO", True, (255, 255, 255))
            rect_texto = texto.get_rect(center=botao.center)
            self.superficie_tela_principal.blit(texto, rect_texto)

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == MOUSEBUTTONDOWN:
                    if botao.collidepoint(event.pos):
                        esperando_clique = False

                        
            pygame.display.update()

        self.contagem_regressiva(3)
        relogio.tick()
    
    def tela_tentar_denovo(self, pontuacao, coletados):
        fonte_titulo = pygame.font.Font('fonts/04B_19.TTF', 72)
        fonte_botao = pygame.font.Font('fonts/04B_19.TTF', 36)
        fonte_pontos = pygame.font.Font('fonts/04B_19.TTF', 50)

        largura_botao = 300
        altura_botao = 70
        x_botao = 425
        y_botao = ((self.altura_tela_princial - altura_botao) // 2) + 200

        botao_tentar_de_novo = pygame.Rect(x_botao, y_botao, largura_botao + 50, altura_botao)

        esperando_clique = True
        while esperando_clique:
            self.superficie_tela_principal.fill((50, 0, 0))

            # Mensagem de game over
            texto_morreu = fonte_titulo.render("GAME OVER", True, (255, 0, 0))
            rect_morreu = texto_morreu.get_rect(center=(self.largura_tela_principal//2, 150))
            self.superficie_tela_principal.blit(texto_morreu, rect_morreu)

            # Pontuação
            texto_pontos = fonte_pontos.render(f"Pontos: {pontuacao}", True, (255, 255, 255))
            texto_estrelinhas = fonte_pontos.render(f"Estrelinhas: {str(coletados['estrelinha'])}", True, (255, 255, 255))
            texto_relogios = fonte_pontos.render(f"Relogios: {str(coletados['relogio'])}", True, (255, 255, 255))
            rect_pontos = texto_pontos.get_rect(center=(self.largura_tela_principal//2, 250))
            rect_estrlinhas = texto_estrelinhas.get_rect(center=(self.largura_tela_principal//2, 300))
            rect_relogios = texto_relogios.get_rect(center=(self.largura_tela_principal//2, 350))
            self.superficie_tela_principal.blit(texto_pontos, rect_pontos)
            self.superficie_tela_principal.blit(texto_estrelinhas, rect_estrlinhas)
            self.superficie_tela_principal.blit(texto_relogios, rect_relogios)

            # Botão tentar de novo
            pygame.draw.rect(self.superficie_tela_principal, (0, 120, 250), botao_tentar_de_novo, border_radius=15)
            texto_tentar = fonte_botao.render("TENTAR DE NOVO", True, (255, 255, 255))
            rect_texto = texto_tentar.get_rect(center=botao_tentar_de_novo.center)
            self.superficie_tela_principal.blit(texto_tentar, rect_texto)

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == MOUSEBUTTONDOWN:
                    if botao_tentar_de_novo.collidepoint(event.pos):
                        esperando_clique = False

            pygame.display.update()
        self.contagem_regressiva(3)
        relogio.tick()

    def contagem_regressiva(self, segundos=3):
        fonte = pygame.font.Font('fonts/04B_19.TTF', 80)
        for i in range(segundos, 0, -1):
            self.superficie_tela_principal.fill((0, 0, 0))
            texto = fonte.render(str(i), True, (255, 255, 255))
            rect = texto.get_rect(center=(self.largura_tela_principal//2, self.altura_tela_princial//2))
            self.superficie_tela_principal.blit(texto, rect)
            pygame.display.update()
            pygame.time.delay(1000)  # espera 1 segundo




    