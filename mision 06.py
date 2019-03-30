#Sara Delgado
#Mision 6

import pygame
import math


ANCHO = 640
ALTO = 480

BLANCO = (255, 255, 255)
VERDE_BANDERA = (27, 94, 32)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)



def dibujar(r ,R ,l):

    pygame.init()

    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        ventana.fill(BLANCO)


    periodo = int( r//math.gcd(r, R))

    for angulo in range(0, 360+1, 1):
            k = r/ R
            a = math.radians(a)
            x = int(R * ((1 - k) * math.cos(a) + (l * k) * math.cos(a * ((1 - k) / k))))
            y = int(R * ((1 - k) * math.sin(a) - (l * k) * math.sin(a * ((1 - k) / k))))
            pygame.draw.circle(ventana, ROJO, (x + ANCHO // 2, ALTO // 2 - y), 1)

            pygame.display.flip()
            reloj.tick(40)

    pygame.quit()


def main():
    r = int(input("Inserte el valor r:"))
    R = int(input("Inserte el valor R:"))
    l = int(input("Inserte el valor l:"))
    dibujar(r, R, l)


main()
