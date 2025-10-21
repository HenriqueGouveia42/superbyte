import pygame
#font_path = 'fonts/04B_19.TTF'

class Pontuador:

    def __init__(self, tela, tamanho_fonte=80, cor=(255, 255, 0)):

        self.tela = tela
        self.tela_rect = tela.get_rect()
        self.cor = cor
        self.pontos = 0
        self.fonte = pygame.font.Font('fonts/04B_19.TTF', tamanho_fonte)

        # Prepara a imagem inicial do placar para definir a posição
        self.preparar_imagem()

    def preparar_imagem(self):

        # Converte o valor numérico dos pontos para string
        pontos_str = str(self.pontos)

        # Cria a imagem da pontuação
        self.imagem_pontos = self.fonte.render(pontos_str, True, self.cor)

        # Pega o retângulo da imagem do texto
        self.rect_pontos = self.imagem_pontos.get_rect()

        # Posicionamento
        # Centraliza no eixo X
        self.rect_pontos.centerx = self.tela_rect.centerx
        
        # Alinha no topo
        self.rect_pontos.top = 25

    def desenhar(self):
        # Desenha o placar na tela
        self.tela.blit(self.imagem_pontos, self.rect_pontos)

    def aumentar(self, valor=1):
        # Função para aumentar pontuação
        self.pontos += valor
        self.preparar_imagem()

    def zerar(self):
        # Função para zerar pontuação
        self.pontos = 0
        self.preparar_imagem()