'''
Gegeven zijn: een horror font dat "voetbal game" op het scherm zet en een plaatje van een bal.

We gaan de game aanpassen zodat het er beter uit ziet.

Doe het volgende:

  - Download een toepasselijk font en maak hiermee een scoreboard
  - Download 2 plaatjes van voetballers en zet deze tegenover elkaar op het scherm
  - Zet de bal in het midden van de scherm

Extra tijd:

  - Voeg 2 goals toe (links en rechts)
  - Voeg een toepasselijke achtergrond toe
  - Schrijf de namen van de spelers ergens op het scherm

Slides: https://docs.google.com/presentation/d/1c4C94q8OcMGCIFefVo18Xac4WIFJacq5Eutj1gY6rCg/edit?usp=sharing
'''
import os
os.environ['SDL_AUDIODRIVER'] = 'dsp'

import pygame

pygame.init()

screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Voetbal game!')
clock = pygame.time.Clock()
running = True
test_font = pygame.font.Font("/workspaces/pygame-oefeningen-TylerBrandt0/Opdrachten/PyGame/Les2/fonts/Soccer.ttf", 50)

surface = pygame.Surface((800, 400))
surface.fill("blue")
grass = pygame.Surface((800, 100))
grass.fill("dark green")
voetbal_surface = pygame.image.load("Opdrachten/PyGame/Les2/graphics/voetbal.png")
speler = pygame.image.load("/workspaces/pygame-oefeningen-TylerBrandt0/Opdrachten/PyGame/Les2/graphics/speler.png")
tekst_surface = test_font.render("Score", False, "white")
tekst_surface2 = test_font.render("0 - 0", False, "dark red")
goal = pygame.image.load("/workspaces/pygame-oefeningen-TylerBrandt0/Opdrachten/PyGame/Les2/graphics/goal.svg")

speler = pygame.transform.scale(speler, (150, 150))
speler2 = pygame.transform.flip(speler, True, False)
voetbal_surface = pygame.transform.scale(voetbal_surface, (35, 35))
goal = pygame.transform.scale(goal, (200, 200))
goal2 = pygame.transform.flip(goal, True, False)

while running:

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  screen.blit(surface, (0, 0))
  screen.blit(grass, (0, 300))
  screen.blit(goal, (700, 150))
  screen.blit(goal2, (-100, 150))
  screen.blit(tekst_surface, (0, 0))
  screen.blit(tekst_surface2, (35, 50))
  screen.blit(voetbal_surface, (365, 300))
  screen.blit(speler, (550, 200))
  screen.blit(speler2, (100, 200))

  pygame.display.update()
  clock.tick(60)
