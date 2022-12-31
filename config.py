import os
import pygame
from random import randrange
pygame.init()
sounds = []
for i in os.listdir("sounds"):
    sounds.append(pygame.mixer.Sound(f"sounds/{i}"))
width, height = 800, 300
fps = 60
sc = pygame.display.set_mode([width, height])
clock = pygame.time.Clock()
image = pygame.image.load("img/putin.jpg")
pygame.display.set_caption("Putin Simulator")
color_passive, color_hover, color_active = (255, 64, 64), (255, 128, 128), (255, 0, 0)
color = color_passive
color1 = color_passive
color2 = color_passive
countries = 0
text = pygame.font.SysFont("Arial", 20, bold=True).render("Destroy World", False, (255, 255, 255))
text1 = pygame.font.SysFont("Arial", 20, bold=True).render("Say a phrase", False, (255, 255, 255))
text2 = pygame.font.SysFont("Arial", 40, bold=True).render("QUIT", False, (255, 255, 255))


def say_a_phrase():
    a = randrange(0, len(sounds))
    pygame.mixer.Sound.play(sounds[a])
