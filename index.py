import pygame, sys
from game import Game
from colors import Colors

pygame.init()

background_image = pygame.image.load("unsplash_upscayl.png")
screen = pygame.display.set_mode((500, 620))
pygame.display.set_caption("Druna_s Tetris")
