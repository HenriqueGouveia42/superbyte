import pygame
caminho_sprite_neutro = 'images/byte-reto.png'
caminho_sprite_caindo = 'images/byte-caindo.png'
caminho_sprite_subindo = 'images/byte-subindo.png'

class Personagem:

    FORCA_PULO = -400

    def __init__(self, pos_x, pos_y, tela, largura=50, altura=50, vy=0):

        self.pos_x = pos_x
        self.pos_y = pos_y
        self.vy = vy
        self.tela_rect = tela.get_rect()
        self.rect = pygame.Rect(pos_x, pos_y, largura, altura)
        self.perso_imagem_neutro = pygame.image.load(caminho_sprite_neutro).convert_alpha()
        self.perso_imagem_caindo = pygame.image.load(caminho_sprite_caindo).convert_alpha()
        self.perso_imagem_subindo = pygame.image.load(caminho_sprite_subindo).convert_alpha()
        self.sob_feito_de_invencibilidade = False
        self.largura = largura
        self.altura = altura

        self.temporizador_invencibilidade = pygame.Rect
    

    def pular(self):

        self.vy = self.FORCA_PULO

    def cair(self, gravidade, delta_t):
        self.vy = self.vy + (gravidade * delta_t)
        self.pos_y = self.pos_y + (self.vy * delta_t)
        self.rect.y = self.pos_y

    def desenhar(self, tela_principal):

        if self.vy > 0:
            perso_imagem = self.perso_imagem_subindo
        elif self.vy <= 0 and self.vy >= -300:
            perso_imagem = self.perso_imagem_neutro
        else:
            perso_imagem = self.perso_imagem_caindo

        tela_principal.blit(perso_imagem, self.rect)

    def colidiuComObstaculo(self, obstaculo):

        rect_sup = obstaculo.getObstaculoTopo()

        rect_inf = obstaculo.getObstaculoBaixo()

        personagem_rect = pygame.Rect(self.pos_x, self.pos_y, self.largura, self.altura)

        if personagem_rect.colliderect(rect_sup) or personagem_rect.colliderect(rect_inf):
            return True
        else:
            return False
    
    def colidiuComColetavel(self, coletavel):

        rect_coletavel = coletavel.rect

        rect_personagem = pygame.Rect(self.pos_x, self.pos_y, self.largura, self.altura)

        if rect_personagem.colliderect(rect_coletavel):
            return True
        else:
            return False
    
    def desenharTemporizadorInvecibilidade(self, tela, tempo_ms_passado, duracao_ms):
        tempo_restante = max(0, (duracao_ms - tempo_ms_passado) / 1000)  # converte para segundos

        # Fonte padrão do pygame (tamanho 32)
        fonte_temporizador = pygame.font.Font('fonts/04B_19.TTF', 32)

        # Renderiza o texto com tempo restante
        texto_temporizador = fonte_temporizador.render(f"Invencivel: {tempo_restante:.1f}s", True, (255, 255, 0))  # Amarelo

        # Desenha no canto superior esquerdo (10,10)
        tela.blit(texto_temporizador, (10, 10))

