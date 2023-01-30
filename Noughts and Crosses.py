import pygame
import sys


pygame.init()
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
screen = pygame.display.set_mode((1000, 1000))
screen.fill(BLACK)
pygame.mouse.set_cursor(pygame.cursors.diamond)

pygame.draw.rect(screen, WHITE, (0, 0, 323, 323), 0)
pygame.draw.rect(screen, WHITE, (0, 333, 323, 323), 0)
pygame.draw.rect(screen, WHITE, (0, 666, 323, 333), 0)
pygame.draw.rect(screen, WHITE, (333, 0, 333, 323), 0)
pygame.draw.rect(screen, WHITE, (333, 333, 333, 323), 0)
pygame.draw.rect(screen, WHITE, (333, 666, 333, 333), 0)
pygame.draw.rect(screen, WHITE, (676, 0, 343, 323), 0)
pygame.draw.rect(screen, WHITE, (676, 333, 343, 323), 0)
pygame.draw.rect(screen, WHITE, (676, 666, 343, 333), 0)


def cross1(x, y, x2, y2, x3, y3, x4, y4):
    pygame.draw.line(screen, BLACK, (x, y), (x2, y2), 20)
    pygame.draw.line(screen, BLACK, (x3, y3), (x4, y4), 20)


#cross1(0, 0, 333, 333, 0, 333, 333, 0)
cross1(333, 0, 666, 333, 333, 333, 666, 0)
cross1(666, 0, 999, 333, 666, 333, 999, 0)

pygame.display.update()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
def t1():
    if pygame.MOUSEBUTTONDOWN:
        cross1(0, 0, 333, 333, 0, 333, 333, 0)
t1()

pygame.display.update()
