import pygame

from settings import *

class UI:
    def __init__(self):
        
        # general
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(UI_FONT, UI_FONT_SIZE)

        self.tiles = []
        for y in range(0, HEIGHT, TILESIZE):
            for x in range(0, WIDTH, TILESIZE):
                tile_rect = pygame.Rect(x, y, TILESIZE, TILESIZE)
                self.tiles.append(tile_rect)
        

    def selection_box(self,left,top,is_selected) -> pygame.Rect:
        bg_rect = pygame.Rect(left,top,ITEM_BOX_SIZE,ITEM_BOX_SIZE)
        #pygame.draw.rect(self.display_surface, UI_BG_COLOR,bg_rect)
        if is_selected:
            pygame.draw.rect(self.display_surface, UI_BORDER_COLOR_ACTIVE,bg_rect,3)
        #else:
            #pygame.draw.rect(self.display_surface, UI_BORDER_COLOR,bg_rect,3)
        return bg_rect

    def display(self):
        # prototipo estatico
        tiles = []
        tiles.append(self.selection_box(64,64,False))
        tiles.append(self.selection_box(2*64,2*64,False))
        tiles.append(self.selection_box(3*64,3*64,False))
        tiles.append(self.selection_box(2*64,4*64,False))

        # mouse hover
        mouse_x, mouse_y = pygame.mouse.get_pos()
        for tile in tiles:
            if tile.collidepoint(mouse_x, mouse_y):
                self.selection = self.selection_box(tile.left,tile.top,True)

        '''for tile in self.tiles:
            if tile.collidepoint(mouse_x, mouse_y):
                self.selection_box.move
            else:
                pygame.draw.rect(self.display_surface, TILE_COLOR, tile)'''