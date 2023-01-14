import time

import pygame
import sys
from funciones import *

# Inicializamos la librería pygame
pygame.init()

# Declaramos las constantes de imagenes y texto
ICONO = pygame.image.load("recursos/IconoW.jpg")
FONDOV = pygame.image.load("recursos/Fondo Victoria.jpg")
FONDOD = pygame.image.load("recursos/Fondo Derrota.jpg")
FUENTEG = pygame.font.SysFont("segoeuiblack", 40)
FUENTEP = pygame.font.SysFont("segoeuiblack", 24)

# Declaramos las constantes generales
SIZE_SCREEN = (500, 650)
PANTALLA = pygame.display.set_mode(SIZE_SCREEN)
CLOCK = pygame.time.Clock()

# Asignamos atributos a la ventana
pygame.display.set_caption("Adivina la palabra")
pygame.display.set_icon(ICONO)

def PantallaInicial (screen):
    screen.blit (FONDOV, (0, 0))
    fuente_creditos = pygame.font.SysFont("arial", 12)
    creditos = fuente_creditos.render('\u00A9' + '  by JAMF', True, "white")
    posicion_creditos = creditos.get_rect(center=(SIZE_SCREEN[0] / 10 * 9, 640))
    PANTALLA.blit(creditos, posicion_creditos)
    pygame.display.update()
    return screen

def JugarOtraVez (screen):
    linea1 = FUENTEG.render('¿ Juegas otra vez ?', True, '#222424')
    linea2 = FUENTEG.render('Pulsa (S)', True, '#222424')
    linea3 = FUENTEG.render('Pulsa (N)', True, '#222424')
    posiciontexto1 = linea1.get_rect(center=(250, 350))
    posiciontexto2 = linea2.get_rect(center=(300, 460))
    posiciontexto3 = linea3.get_rect(center=(300, 560))
    screen.blit(linea1, posiciontexto1)
    screen.blit(linea2, posiciontexto2)
    screen.blit(linea3, posiciontexto3)
    pygame.draw.rect(screen, '#222424', (100, 420, 80, 80), 0, 2)
    pygame.draw.rect(screen, '#222424', (100, 520, 80, 80), 0, 2)
    tecla1 = FUENTEG.render('Si', True, '#EBEBEB')
    tecla2 = FUENTEG.render('No', True, '#EBEBEB')
    PosicionTecla1 = tecla1.get_rect(center=(140, 460))
    PosicionTecla2 = tecla2.get_rect(center=(140, 560))
    screen.blit(tecla1, PosicionTecla1)
    screen.blit(tecla2, PosicionTecla2)

def PantallaVictoria (screen):
    screen.blit (FONDOV, (0, 0))
    linea1 = FUENTEG.render('¡¡¡ ENHORABUENA !!!', True, '#222424')
    linea2 = FUENTEP.render('Has conseguido Averiguar', True, '#222424')
    linea3 = FUENTEP.render('La palabra oculta', True, '#222424')
    posiciontexto1 = linea1.get_rect(center=(250, 100))
    posiciontexto2 = linea2.get_rect(center=(250, 200))
    posiciontexto3 = linea3.get_rect(center=(250, 250))
    screen.blit(linea1, posiciontexto1)
    screen.blit(linea2, posiciontexto2)
    screen.blit(linea3, posiciontexto3)
    JugarOtraVez(screen)
    pygame.display.update()

def PantallaDerrota (screen):
    screen.blit (FONDOD, (0, 0))
    linea1 = FUENTEG.render('¡¡¡ LO SENTIMOS !!!', True,  '#222424')
    linea2 = FUENTEP.render('NO has conseguido Averiguar', True,  '#222424')
    linea3 = FUENTEP.render('La palabra oculta', True,  '#222424')
    posiciontexto1 = linea1.get_rect(center=(250, 100))
    posiciontexto2 = linea2.get_rect(center=(250, 200))
    posiciontexto3 = linea3.get_rect(center=(250, 250))
    screen.blit(linea1, posiciontexto1)
    screen.blit(linea2, posiciontexto2)
    screen.blit(linea3, posiciontexto3)
    JugarOtraVez(screen)
    pygame.display.update()

def JugarJuego (JuegoActual):
    while JuegoActual.Estado:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                 pygame.quit()
                 sys.exit()
            elif evento.type == pygame.KEYDOWN:
                JuegoActual.PulsaTecla(evento)
        pygame.display.update()
        CLOCK.tick(60)
    if JuegoActual.PalabraIntento == JuegoActual.PalabraSecreta:
        PantallaVictoria(JuegoActual.Pantalla)
    else:
        PantallaDerrota(JuegoActual.Pantalla)

    while True:
        for evento in pygame.event.get():
            if (evento.type == pygame.QUIT):
                pygame.quit()
                sys.exit()
            elif (evento.type == pygame.KEYDOWN) and (evento.key == pygame.K_s):
                NuevoJuego = Juego(PantallaInicial(PANTALLA))
                JugarJuego(NuevoJuego)
            elif (evento.type == pygame.KEYDOWN) and (evento.key == pygame.K_n):
                pygame.quit()
                sys.exit()

NuevoJuego = Juego(PantallaInicial(PANTALLA))
JugarJuego(NuevoJuego)

