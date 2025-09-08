'''
Maak het plaatje dat in dit mapje staat na.

Slides: 
https://docs.google.com/presentation/d/1YwoUdeWABUYJkSfNzzZzDbCKvCVmWoo9Z5Uu7f_Y_K4/edit?usp=sharing
'''
import os
os.environ['SDL_AUDIODRIVER'] = 'dsp'

import pygame

pygame.init()

screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Eerste game!')
clock = pygame.time.Clock()
running = True

surface = pygame.Surface((800, 400))
surface.fill("blue")

pijp = pygame.Surface((50, 300))
pijp.fill("green")

flappybird = pygame.Surface((25, 25))
flappybird.fill("yellow")

while running:

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  screen.blit(surface, (0, 0))
  screen.blit(pijp, (175,-100))
  screen.blit(pijp, (400,-200))
  screen.blit(pijp, (625,-50))
  screen.blit(pijp, (175,300))
  screen.blit(pijp, (400,200))
  screen.blit(pijp, (625,350))
  screen.blit(flappybird, (50, 175))

  pygame.display.update()
  clock.tick(60)
