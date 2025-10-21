import random
import pygame
from pygame.locals import *

caminho_cano_baixo = './images/cano_baixo.png'
caminho_cano_cima = './images/cano_cima.png'

caminho_cano_baixo_invencivel = './images/cano_baixo_transparente.png'
caminho_cano_cima_invencivel = './images/cano_cima_transparente.png'

class Obstaculo:

    def __init__(self, x_pos, largura, margem, altura_tela, largura_tela, altura_chao):

        self.x_pos = x_pos
        self.altura_topo =None
        self.altura_baixo = None
        self.largura = largura
        self.margem = margem
        self.altura_tela = altura_tela
        self.retangulo_topo =None
        self.retangulo_baixo = None
        self.largura_tela = largura_tela
        self.altura_chao = altura_chao
        self.personagem_esta_invencivel = False

        self.imagem_cano_baixo_original = pygame.image.load(caminho_cano_baixo).convert_alpha()
        self.imagem_cano_cima_original = pygame.image.load(caminho_cano_cima).convert_alpha()

        self.imagem_cano_baixo = self.imagem_cano_baixo_original
        self.imagem_cano_cima = self.imagem_cano_cima_original

        self.imagem_cano_baixo_invencivel_original = pygame.image.load(caminho_cano_baixo_invencivel).convert_alpha()
        self.imagem_cano_cima_invencivel_original = pygame.image.load(caminho_cano_cima_invencivel).convert_alpha()

        self.imagem_cano_baixo_invencivel = self.imagem_cano_baixo_invencivel_original
        self.imagem_cano_cima_invencivel = self.imagem_cano_cima_invencivel_original

        self.definirAlturaTopo()

    def getObstaculoTopo(self):
        return self.retangulo_topo

    def getObstaculoBaixo(self):
        return self.retangulo_baixo
    
    def definirAlturaTopo(self):

        altura_tela = self.altura_tela
        margem = self.margem

        altura_topo = random.randint(20, altura_tela - margem - self.altura_chao)
        altura_baixo = altura_tela - altura_topo - margem

        self.altura_topo = altura_topo
        self.altura_baixo = altura_baixo

        
        #Cálculo das imagens dos canos
        self.imagem_cano_baixo = pygame.transform.scale(self.imagem_cano_baixo_original, (self.largura, self.altura_baixo))
        self.imagem_cano_cima = pygame.transform.scale(self.imagem_cano_cima_original, (self.largura, self.altura_topo))

        self.imagem_cano_baixo_invencivel = pygame.transform.scale(self.imagem_cano_baixo_invencivel_original, (self.largura, self.altura_baixo))
        self.imagem_cano_cima_invencivel = pygame.transform.scale(self.imagem_cano_cima_invencivel_original, (self.largura, self.altura_topo))


    def desenharObstaculo(self, superficie):

        margem = self.margem
        x_obstaculo = self.x_pos
        largura_obstaculo = self.largura

        altura_topo = self.altura_topo
        altura_baixo = self.altura_baixo

        retangulo_topo = pygame.Rect(x_obstaculo, 0 ,largura_obstaculo, altura_topo)
        retangulo_baixo = pygame.Rect(x_obstaculo, altura_topo + margem ,largura_obstaculo, altura_baixo)

        self.retangulo_topo = retangulo_topo
        self.retangulo_baixo = retangulo_baixo

        if self.personagem_esta_invencivel:
            superficie.blit(self.imagem_cano_cima_invencivel, self.retangulo_topo)
            superficie.blit(self.imagem_cano_baixo_invencivel, self.retangulo_baixo)
        else:
            superficie.blit(self.imagem_cano_cima, self.retangulo_topo)
            superficie.blit(self.imagem_cano_baixo, self.retangulo_baixo)
        

    def teleportarParaDireita(self):

        self.definirAlturaTopo()

        largura_tela = self.largura_tela
        
        self.x_pos = largura_tela

    def reiniciarPosicao(self, distancia_entre_obstaculos, n_distancia_entre_obstaculos):

        largura_tela = self.largura_tela

        self.definirAlturaTopo()

        self.x_pos = largura_tela - (n_distancia_entre_obstaculos * distancia_entre_obstaculos)

