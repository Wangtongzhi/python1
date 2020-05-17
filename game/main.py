import pygame
import sys
pygame.display.set_mode([600,400])
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()