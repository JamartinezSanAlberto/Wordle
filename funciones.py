import pygame
import random
ALFABETO = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
COLOR_TECLA_C='#edebeb'
COLOR_TECLA_O='#222424'
COLOR_TECLA_V='#298032'
COLOR_TECLA_A='#D9CB11'
COLOR_LETRA_O='#363535'
COLOR_LETRA_C='#EBEBEB'

def ListaPalabras(letras):
    archivo_palabras = open('recursos/mayusculas.txt', 'r', encoding='utf-8')
    Palabras = []
    for linea in archivo_palabras:
        if (len(linea) == letras + 1):
            Palabras.append(linea[:letras])
    archivo_palabras.close()
    return Palabras


class Juego ():
    def __init__(self, screen):
        self.Pantalla= screen
        self.Estado = True
        self.Palabras = ListaPalabras(5)
        self.PalabraSecreta = self.Palabras[random.randint(0,len(self.Palabras)-1)]
        self.PalabraIntento =''
        self.Intento = [0,0]
        self.PosicionesIntentos = (((80,25), (150,25), (220,25), (290,25), (360,25)),
                                   ((80,95), (150,95), (220,95), (290,95), (360,95)),
                                   ((80,165),(150,165),(220,165),(290,165),(360,165)),
                                   ((80,235),(150,235),(220,235),(290,235),(360,235)),
                                   ((80,305),(150,305),(220,305),(290,305),(360,305)),
                                   ((80,375),(150,375),(220,375),(290,375),(360,375)))

        self.PosicionesTeclas   = (((30,460), (75,460),(120,460),(165,460),(210,460),(255,460),(300,460),(345,460),(390,460),(435,460)),
                                   ((30,520), (75,520),(120,520),(165,520),(210,520),(255,520),(300,520),(345,520),(390,520),(435,520)),
                                   ((100,580),(145,580),(190,580),(235,580),(280,580),(325,580),(370,580)))

        self.Alfabeto = 'QWERTYUIOPASDFGHJKLÑZXCVBNM'

        self.PintaEscenario()


    def BuscarPosicionTecla(self,Letra):
        IndiceLetra = divmod(self.Alfabeto.index(Letra), 10)
        Posicion = self.PosicionesTeclas[IndiceLetra[0]][IndiceLetra[1]]
        return Posicion

    def BuscarPosicionIntento(self):
        Posicion = self.PosicionesIntentos[self.Intento[0]][self.Intento[1]]
        return Posicion

    def PintaEscenario(self):
      for i in range (0,6):
          for Posicion in self.PosicionesIntentos[i]:
             self.Pintar_Tecla('',Posicion,'G')
      for Letra in self.Alfabeto:
          self.Pintar_Tecla(Letra, self.BuscarPosicionTecla(Letra), '')

    def Pintar_Tecla(self, Letra, Posicion, Estilo):
        if 'G' in Estilo:
            Size = (60,60)
            FuenteTecla = pygame.font.SysFont("segoeuiblack", 36)
        else:
            Size = (35,50)
            FuenteTecla = pygame.font.SysFont("arial", 24)
        ColorLetra = COLOR_LETRA_C
        if 'V' in Estilo:
            ColorFondo = COLOR_TECLA_V
        elif 'A' in Estilo:
            ColorFondo = COLOR_TECLA_A
        elif 'O' in Estilo:
            ColorFondo = COLOR_TECLA_O
        else:
            ColorLetra = COLOR_LETRA_O
            ColorFondo = COLOR_TECLA_C
        pygame.draw.rect(self.Pantalla, ColorFondo, (Posicion[0], Posicion[1], Size[0], Size[1]), 0, 2)
        texto = FuenteTecla.render(Letra, True, ColorLetra)
        PosicionTexto = texto.get_rect(center=(Posicion[0] + (Size[0] / 2), Posicion[1] + (Size[1] / 2)))
        self.Pantalla.blit(texto, PosicionTexto)

    def BorrarLetra(self):
        self.PalabraIntento = self.PalabraIntento[0:len(self.PalabraIntento)-1]
        self.Intento[1] = self.Intento[1] - 1
        self.Pintar_Tecla('', self.BuscarPosicionIntento(),'G')

    def PonerLetra(self, Letra):
        self.Pintar_Tecla(Letra, self.BuscarPosicionIntento(), 'G')
        self.PalabraIntento = self.PalabraIntento + Letra
        self.Intento[1] = self.Intento[1] + 1

    def Comparar(self):
        for i in range (0,5):
            if self.PalabraIntento[i] == self.PalabraSecreta[i]:
                self.Pintar_Tecla(self.PalabraIntento[i],self.PosicionesIntentos[self.Intento[0]][i],'GV')
                self.Pintar_Tecla(self.PalabraIntento[i], self.BuscarPosicionTecla(self.PalabraIntento[i]), 'V')
            elif self.PalabraIntento[i] in self.PalabraSecreta:
                self.Pintar_Tecla(self.PalabraIntento[i], self.PosicionesIntentos[self.Intento[0]][i],'GA')
                self.Pintar_Tecla(self.PalabraIntento[i], self.BuscarPosicionTecla(self.PalabraIntento[i]), 'A')
            else:
                self.Pintar_Tecla(self.PalabraIntento[i], self.PosicionesIntentos[self.Intento[0]][i],'G')
                self.Pintar_Tecla(self.PalabraIntento[i], self.BuscarPosicionTecla(self.PalabraIntento[i]), 'O  ')
        self.Intento[0] = self.Intento[0] + 1
        self.Intento[1] = 0


    def PulsaTecla(self, Tecla):
        if (Tecla.key == pygame.K_BACKSPACE) and (self.Intento[1] > 0):
            self.BorrarLetra()
        elif Tecla.key == pygame.K_RETURN:
            if (self.Intento[1] == 5) and (self.Intento[0] < 5):
                if self.PalabraIntento in self.Palabras:
                    if self.PalabraIntento == self.PalabraSecreta:
                        self.Comparar()
                        self.Estado = False
                    else:
                        #print(self.PalabraSecreta)
                        #print(self.PalabraIntento)
                        self.Comparar()
                        self.PalabraIntento = ''
                else:
                    for i in range (0,5):
                        self.BorrarLetra()
            elif (self.Intento[1] == 5) and (self.Intento[0] == 5):
                self.Estado = False
        elif (Tecla.unicode.upper() in ALFABETO) and (self.Intento[1] < 5) :
            self.PonerLetra(Tecla.unicode.upper())

    def PantallaFinal(self):
        if self.Estado == True:
            self.Pantalla.fill((0,0,0))
        else:
            self.Pantalla.fill((255,255,255))
        evento = pygame.event.get()
        return evento

