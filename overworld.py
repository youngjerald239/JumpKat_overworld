import pygame
from game_data import levels

class Node(pygame.sprite.Sprite):
    def __init__(self,pos,status):
        super().__init__()
        self.image = pygame.Surface((100,80))
        if status == 'available':
            self.image.fill('red')
        else:
            self.image.fill('grey')
        self.rect = self.image.get_rect(center = pos)

class Overworld:
    def __init__(self,start_level,max_level,surface):

        #setup
        self.display_surface = surface
        self.max_level = max_level
        self.current_level = start_level

        # sprites
        self.setup_nodes()

    def setup_nodes(self):
        self.nodes = pygame.sprite.Group()

        for index, node_data in enumerate(levels.values()):
            if index <= self.max_level:
                node_sprite = Node(node_data['node_pos'],'available')
                self.nodes.add(node_sprite)
            else:
                node_sprite = Node(node_data['node_pos'],'locked')
            self.nodes.add(node_sprite)

    def draw_paths(self):
        points = [node['node_pos'] for node in levels.values()]
        pygame.draw.lines(self.display_surface,'red',False,points,6)

    def run(self):
        self.nodes.draw(self.display_surface)
        self.draw_paths()