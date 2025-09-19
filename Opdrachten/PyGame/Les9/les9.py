# Het lopen van de speler is al geanimeerd!

# Voeg comments aan de code die uitleggen wat de code doet.

# Voeg hierna de jump animatie toe. Op dit moment gaat dezelfde animatie verder als de speler springt.
# Zorg ervoor dat de speler een jump animatie krijgt als de speler springt.
import os
os.environ['SDL_AUDIODRIVER'] = 'dsp'

import pygame, sys
from pygame.locals import QUIT  

pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Animaties')
clock = pygame.time.Clock()

background_surface = pygame.Surface((400, 300))
background_surface.fill("white")


speler_stil1_surface = pygame.image.load("Opdrachten/PyGame/Les9/graphics/speler_stil1.png").convert_alpha()
speler_stil2_surface = pygame.image.load("Opdrachten/PyGame/Les9/graphics/speler_stil2.png").convert_alpha()
animaties = [speler_stil1_surface, speler_stil2_surface]

speler_stil1_surface_links = pygame.transform.flip(speler_stil1_surface, True, False)
speler_stil2_surface_links = pygame.transform.flip(speler_stil2_surface, True, False)
animaties_links = [speler_stil1_surface_links, speler_stil2_surface_links]

index = 0
speler_jump_surface = pygame.image.load("Opdrachten/PyGame/Les9/graphics/speler_jump.png").convert_alpha()
speler_jump_surface_links = pygame.transform.flip(speler_jump_surface, True, False)
speler_rect = speler_stil1_surface.get_rect(midbottom = (200, 300))

zwaartekracht = 0

while True:
  
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit() 

    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_UP and speler_rect.bottom >= 300:
        zwaartekracht = -18
        screen.blit(speler_jump_surface, speler_rect)

  keys = pygame.key.get_pressed()
  if keys[pygame.K_LEFT] and speler_rect.left > 0:
    speler_rect.x -= 5
  if keys[pygame.K_RIGHT] and speler_rect.right < 400:
    speler_rect.x += 5


  screen.blit(background_surface, (0, 0))

  zwaartekracht += 1
  speler_rect.y += zwaartekracht
  
  if speler_rect.bottom >= 300:
    speler_rect.bottom = 300

  index += 0.05
  
  if index > len(animaties):
    index = 0

  if speler_rect.bottom < 300:
    screen.blit(speler_jump_surface, speler_rect)
  elif keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]:
    if keys[pygame.K_LEFT]:
      screen.blit(animaties_links[int(index)], speler_rect)
    else:
      screen.blit(animaties[int(index)], speler_rect)
  else:
    screen.blit(speler_stil1_surface, speler_rect)

  pygame.display.update()
  clock.tick(60)