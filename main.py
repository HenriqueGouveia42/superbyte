#classes de elementos do jogo
from Obstaculo import Obstaculo
from Personagem import Personagem
from Telas import Telas
from Pontuador import Pontuador
from Coletaveis import Coletaveis

import pygame
from pygame.locals import *
from sys import exit

#dimensões da tela
largura_tela = 1200
altura_tela = 650
imagem_fundo = pygame.image.load('images/fundo.png')
imagem_chao = pygame.image.load('images/chao.png')
altura_chao = 58

#parametros iniciais do personagem
y_inicial_personagem = altura_tela / 2
x_personagem = largura_tela / 8
y_personagem = y_inicial_personagem
vy_personagem = 0
largura_personagem = 50
altura_personagem =  45
periodo_de_invencibilidade = 8000

#parametros do personagem
personagem_obstaculo_colidindo = False
personagem_coletavel_colidindo = False

#parametros dos obstaculos
largura_cano = 120
margem_obstaculo = altura_personagem * 4

#parametros fisicos
gravidade = 1500
relogio = pygame.time.Clock()
passo_obstaculo_original = 150
passo_obstaculo_atual = passo_obstaculo_original


#parametros do jogo
rodando_partida = True
distancia_entre_obstaculos = largura_tela / 3
relogio = pygame.time.Clock() #relogio para controlar FPS e delta_t
tela_principal = pygame.display.set_mode((largura_tela, altura_tela))
fator_velocidade = 8

obstaculo1_foi_passado = False
obstaculo2_foi_passado = False
obstaculo3_foi_passado = False
apareceu_tela_inicial = False

font_path = 'fonts/04B_19.TTF'

coletados = {
    'estrelinha': 0,
    'relogio': 0,
}

#
#
#
#
# JOGO COMECA DAQUI PRA BAIXO
#
#
#
#
#

pygame.init()

pygame.mixer.init()

pygame.display.set_caption('Super Byte')

telas = Telas(font_path, 36, largura_tela, altura_tela, tela_principal)

pygame.mixer.music.load('sound/sound/ts.mp3')
pygame.mixer.music.set_volume(0.2)
som_de_ponto = pygame.mixer.Sound('sound/sound/sfx_point.wav')
som_de_ponto.set_volume(0.6)
som_das_asas_batendo = pygame.mixer.Sound('sound/sound/sfx_wing.wav')
som_das_asas_batendo.set_volume(0.3)
som_batida_no_cano = pygame.mixer.Sound('sound/sound/sfx_hit.wav')
som_batida_no_cano.set_volume(0.6)
som_clique_opcoes_jogo = pygame.mixer.Sound('sound/sound/sfx_swooshing.wav')
som_clique_opcoes_jogo.set_volume(0.5)
som_invencivel = pygame.mixer.Sound('sound/sound/musicsupermario.mp3')
som_invencivel.set_volume(0.3)
tocou_som_invencivel = False

personagem = Personagem(x_personagem, y_personagem, tela_principal)

placar = Pontuador(tela_principal)

obstaculo1 = Obstaculo(largura_tela, largura_cano, margem_obstaculo, altura_tela, largura_tela, altura_chao)
obstaculo2 = Obstaculo(largura_tela - (distancia_entre_obstaculos), largura_cano, margem_obstaculo, altura_tela, largura_tela, altura_chao)
obstaculo3 = Obstaculo(largura_tela - (2 * distancia_entre_obstaculos), largura_cano, margem_obstaculo, altura_tela, largura_tela, altura_chao)

coletavel = Coletaveis(tela_principal)
icone_estrelinha = pygame.image.load("images/estrelinha.png")
icone_relogio = pygame.image.load("images/relogio.png")

tempo_inicial_jogo = pygame.time.get_ticks()

instante_em_que_foi_pego_a_invencibilidade = 0

chao_pos_x = 0

pygame.mixer.music.play(loops=-1)
while rodando_partida:

    delta_t = relogio.tick(60) / 1000

    tela_principal.blit(imagem_fundo, (0,0))

    #eventos
    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
            exit()
        
        if event.type == KEYDOWN:

            if event.key == K_SPACE:
                
                personagem.pular()
                som_das_asas_batendo.play()
    
    #tela inicial do jogo
    if not apareceu_tela_inicial:
        
        telas.tela_inicial() #fica preso nesse looping
        som_clique_opcoes_jogo.play()
        pygame.time.delay(500)
        relogio.tick()
        tempo_inicial_jogo = pygame.time.get_ticks()
        

        personagem.pos_y = y_inicial_personagem
        personagem.vy = 0
        
        apareceu_tela_inicial = True
        continue
    
    personagem.cair(gravidade, delta_t)
    
    #limitação de movimento do personagem - topo da tela
    if personagem.pos_y < 0:
        personagem.pos_y = 0
        personagem.vy = 0

    #limitação de movimento do personagem - fundo da tela
    if personagem.pos_y > altura_tela - altura_personagem - altura_chao:
        personagem.pos_y = altura_tela - altura_personagem - altura_chao
        personagem.vy = 0

    #passos dos obstaculos
    obstaculo1.x_pos -= passo_obstaculo_atual * delta_t
    obstaculo2.x_pos -= passo_obstaculo_atual * delta_t
    obstaculo3.x_pos -= passo_obstaculo_atual * delta_t
    if coletavel.pos_x >= -40:
        coletavel.pos_x -= passo_obstaculo_atual * delta_t

    #teleporte dos obstaculos para o lado direito da tela se tiverem chegado ao fim
    if obstaculo3.x_pos <= -largura_cano:
        obstaculo3.teleportarParaDireita()
        coletavel.teleportarColetavelParaDireita(distancia_entre_obstaculos, obstaculo3.altura_topo, margem_obstaculo, personagem)
        obstaculo3_foi_passado = False
        #placar.aumentar()

    if obstaculo2.x_pos <= -largura_cano:
        obstaculo2.teleportarParaDireita()
        coletavel.teleportarColetavelParaDireita(distancia_entre_obstaculos, obstaculo2.altura_topo, margem_obstaculo, personagem)

        obstaculo2_foi_passado = False
        #placar.aumentar()

    if obstaculo1.x_pos <= -largura_cano:
        obstaculo1.teleportarParaDireita()
        coletavel.teleportarColetavelParaDireita(distancia_entre_obstaculos, obstaculo1.altura_topo, margem_obstaculo, personagem)

        obstaculo1_foi_passado = False
        #placar.aumentar()
        
    #estado atual de invencibilidade do personagem
    invencivel = personagem.sob_feito_de_invencibilidade
    #os obstaculos precisam 'saber' se o personagem está ou não invencivel para saberem se desenham o cano TRANSPARENTE (invencivel) ou não
    obstaculo1.personagem_esta_invencivel = invencivel
    obstaculo2.personagem_esta_invencivel = invencivel
    obstaculo3.personagem_esta_invencivel = invencivel

    #desenhos dos obstaculos
    obstaculo1.desenharObstaculo(tela_principal)
    obstaculo2.desenharObstaculo(tela_principal)
    obstaculo3.desenharObstaculo(tela_principal)

    #desenho do placar, por cima dos obstaculos
    placar.desenhar()

    #desenho do coletavel
    coletavel.desenharColetavel()

    #desenho do chão
    tela_principal.blit(imagem_chao, (chao_pos_x, altura_tela - altura_chao))

    #passo do chão
    chao_pos_x -= passo_obstaculo_atual * delta_t

    #limitacao da imagem do chão para dar impressao de ser infinito
    if abs(chao_pos_x) >= largura_tela - 200:
        chao_pos_x = 0

    #verifica se o personagem passou com sucesso de algum obstaculo
    if personagem.pos_x > obstaculo1.retangulo_topo.right and not obstaculo1_foi_passado:
        placar.aumentar()
        som_de_ponto.play()
        obstaculo1_foi_passado = True
    
    if personagem.pos_x > obstaculo2.retangulo_topo.right and not obstaculo2_foi_passado:
        placar.aumentar()
        som_de_ponto.play()
        obstaculo2_foi_passado = True

    if personagem.pos_x > obstaculo3.retangulo_topo.right and not obstaculo3_foi_passado:
        placar.aumentar()
        som_de_ponto.play()
        obstaculo3_foi_passado = True

    

    #verifica se personagem está invencivel e se colidiu com obstaculo

    if not invencivel:
        if personagem.colidiuComObstaculo(obstaculo3):
            personagem_obstaculo_colidindo = True
            som_batida_no_cano.play()
        elif personagem.colidiuComObstaculo(obstaculo2):
            personagem_obstaculo_colidindo = True
            som_batida_no_cano.play()
        elif personagem.colidiuComObstaculo(obstaculo1):
            personagem_obstaculo_colidindo = True
            som_batida_no_cano.play()

    if personagem_obstaculo_colidindo == True:

        passo_obstaculo_atual = passo_obstaculo_original
        
        #tela de tentar de novo
        telas.tela_tentar_denovo(placar.pontos, coletados) #fica preso nesse looping

        #saiu do looping da tela de tentar de novo, reinicia o while principal do jogo ressetando os valores
        pygame.time.delay(500)
        som_clique_opcoes_jogo.play()
        tempo_inicial_jogo = pygame.time.get_ticks()
        relogio.tick()

        obstaculo3.reiniciarPosicao(distancia_entre_obstaculos, 2)
        obstaculo2.reiniciarPosicao(distancia_entre_obstaculos, 1)
        obstaculo1.reiniciarPosicao(distancia_entre_obstaculos, 0)

        coletavel.reiniciaPosicao()

        personagem.pos_y = y_inicial_personagem
        personagem.vy = 0
        placar.zerar()
        coletados['estrelinha'] = 0
        coletados['relogio'] = 0
                    
        personagem_obstaculo_colidindo = False
    

    #verifica se colidiu com o coletavel
    if personagem.colidiuComColetavel(coletavel):

        if coletavel.tipo == 'relogio':

            coletados['relogio'] += 1
            passo_obstaculo_atual = passo_obstaculo_original

            #o tempo inicial do jogo passa a ser o presente instante da execucao
            tempo_inicial_jogo = pygame.time.get_ticks()

        elif coletavel.tipo == 'invencibilidade':
            
            coletados['estrelinha'] += 1
            if not tocou_som_invencivel:
                som_invencivel.play()
                tocou_som_invencivel = True
            personagem.sob_feito_de_invencibilidade = True
            instante_em_que_foi_pego_a_invencibilidade = pygame.time.get_ticks()

        coletavel.pos_x = -40 #joga o coletavel para fora da tela pelo lado esquerdo

    #desenha o personagem
    personagem.desenhar(tela_principal)

    #desenha o inventario
    coletavel .desenhar_inventario(tela_principal, coletados, icone_estrelinha, icone_relogio)

    #desenho do timer de invencibilidade
    if personagem.sob_feito_de_invencibilidade:
        tempo_passado_ms = pygame.time.get_ticks() - instante_em_que_foi_pego_a_invencibilidade
        personagem.desenharTemporizadorInvecibilidade(tela_principal, tempo_passado_ms, periodo_de_invencibilidade)

        if tempo_passado_ms >= periodo_de_invencibilidade:
            personagem.sob_feito_de_invencibilidade = False
            som_invencivel.stop()
            tocou_som_invencivel = False
        
    
    #print(f"Sob efeito de invencibilidade: {personagem.sob_feito_de_invencibilidade} ")
    #print(f"Sob efeito de invencibilidade há {pygame.time.get_ticks() - instante_em_que_foi_pego_a_invencibilidade} ms")
    #print()

    #tempo decorrido em segundos desde o time zero do comeco do jogo
    tempo_decorrido_segundos = (pygame.time.get_ticks() - tempo_inicial_jogo)/1000

    #incremento do passo
    passo_obstaculo_atual = passo_obstaculo_original + (1 + fator_velocidade * tempo_decorrido_segundos)

    pygame.display.update()