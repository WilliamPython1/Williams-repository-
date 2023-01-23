import pygame
import time
pygame.init()
SCREENWIDTH = 1000
SCREENHEIGHT = 1000
WHITE = (255,255,255)
BLACK = (0,0,0)
screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))

screen.fill(WHITE)
pygame.draw.rect(screen, BLACK, (0, 333, 1000, 20), 0)
pygame.draw.rect(screen, BLACK, (0, 666, 1000, 20), 0)
pygame.draw.rect(screen, BLACK, (333, 0, 20, 1000), 0)
pygame.draw.rect(screen, BLACK, (666, 0, 20, 1000),0)
pygame.display.update()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
time.sleep(10)
pygame.quit()
