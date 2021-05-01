import pygame

WIDTH = 800
HEIGHT = 800

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('BomberPy')

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        
