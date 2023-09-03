import pygame
from settings import *
#from tile import Tile
#from player import Player
#from debug import debug
#from support import import_csv_layout, import_folder
#from random import choice
#from weapon import Weapon
from ui import UI

class Level:
    def __init__(self):
        #get the display surface
        self.display_surface = pygame.display.get_surface()

        self.background = pygame.image.load("./graphics/mhf1-weapon-tree-prototype.png")
        self.background = pygame.transform.scale(self.background, (WIDTH, HEIGHT))
        
        # sprite group setup
        #self.visible_sprites = YSortCameraGroup()
        #self.obstacle_sprite = pygame.sprite.Group()

        # attack sprites
        #self.current_attack = None

        # sprite set up
        #self.create_map()
            # creates self.player

        # user interface
        self.ui = UI()

    def run(self):
        self.display_surface.blit(self.background, (0, 0))
        self.ui.display()

