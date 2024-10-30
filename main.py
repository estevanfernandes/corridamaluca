import pygame
import random

pygame.init()  
tamanho = (1000, 592)
clock = pygame.time.Clock()
tela = pygame.display.set_mode( tamanho )
pygame.display.set_caption("Corrida Maluca")
branco = (255,255,255)
preto = (0,0,0)
fundo = pygame.image.load("assets/fundo.png")
carro1 = pygame.image.load("assets/carro1.png")
carro2 = pygame.image.load("assets/carro2.png")
acabou = False

moveXcar1 = 0
moveXcar2 = 0
posYcar1 = 50
posYcar2 = 180
pygame.mixer.music.load("assets/trilha.mp3")
pygame.mixer.music.play(-1) #looping
vitoria = pygame.mixer.Sound("assets/vitoria.mp3")

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            quit()
            
    tela.fill( branco )
    tela.blit(fundo, (0,0))
    tela.blit(carro1, (moveXcar1,posYcar1))
    tela.blit(carro2, (moveXcar2,posYcar2))
    
    if not acabou:
        moveXcar1 = moveXcar1 + random.randint(0,10)
        moveXcar2 = moveXcar2 + random.randint(0,10)
    
    if moveXcar1 > 1000:
        moveXcar1 = 0
        posYcar1 = 350
        
    if moveXcar2 > 1000:
        moveXcar2 = 0
        posYcar2 = 480
        
    fonte = pygame.font.Font("freesansbold.ttf", 60)
    textoVermelho = fonte.render("Vermelho Ganhou!", True, branco)
    textoAmarelo = fonte.render("Amarelo Ganhou!", True, branco)
    
    if posYcar1 == 350 and moveXcar1 >= 900 and moveXcar1 > moveXcar2:
        tela.blit(textoVermelho, (240,70))
        acabou = True
        pygame.mixer.music.stop()
        pygame.mixer.Sound.play(vitoria)
        
    elif posYcar2 == 480 and moveXcar2 >= 900 and moveXcar2 > moveXcar1:
        acabou = True
        tela.blit(textoAmarelo, (270,180))
        pygame.mixer.music.stop()
        pygame.mixer.Sound.play(vitoria)
        
    pygame.display.update()
    clock.tick(60)
pygame.quit()