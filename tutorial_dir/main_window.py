import pygame
import sys
import numpy as np

pygame.init()  # Initialise pygame
fps = 60  # frames per second (target)
window_w = 600  # window width
window_h = 600  # window height
window = pygame.display.set_mode((window_w, window_h))  # the game screen window
clock = pygame.time.Clock()  # time based function

running = True

class KeyMapper:
    def __init__(self):
        self.surf_w = 300
        self.surf_h = 200
        self.surf = pygame.surface.Surface((self.surf_w, self.surf_h), pygame.SRCALPHA)
        self.button = [self.surf_w / 3, self.surf_h / 2]
        self.rects = []
        self.rect = self.surf.get_rect()
        self.rect.bottomright = [window_w, window_h]


    def handle(self):

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            pygame.draw.rect(self.surf, (255, 0, 0), (self.button[0] * 2, self.button[1], self.button[0], self.button[1]))
            pygame.draw.rect(self.surf, (0, 0, 0), (self.button[0]*2, self.button[1], self.button[0], self.button[1]), 5)
        else:
            pygame.draw.rect(self.surf, (255, 255, 255),
                                     (self.button[0] * 2, self.button[1], self.button[0], self.button[1]))
            pygame.draw.rect(self.surf, (0, 0, 0),
                                     (self.button[0] * 2, self.button[1], self.button[0], self.button[1]), 5)
        if keys[pygame.K_LEFT]:
            pygame.draw.rect(self.surf, (255, 0, 0),
                             (0, self.button[1], self.button[0], self.button[1]))
            pygame.draw.rect(self.surf, (0, 0, 0), (0, self.button[1], self.button[0], self.button[1]),
                             5)
        else:
            pygame.draw.rect(self.surf, (255, 255, 255),
                             (0, self.button[1], self.button[0], self.button[1]))
            pygame.draw.rect(self.surf, (0, 0, 0),
                             (0, self.button[1], self.button[0], self.button[1]), 5)
        if keys[pygame.K_UP]:
            pygame.draw.rect(self.surf, (255, 0, 0),
                             (self.button[0],0,self.button[0], self.button[1]))
            pygame.draw.rect(self.surf, (0, 0, 0), (self.button[0],0,self.button[0], self.button[1]),
                             5)
        else:
            pygame.draw.rect(self.surf, (255, 255, 255),
                             (self.button[0],0,self.button[0], self.button[1]))
            pygame.draw.rect(self.surf, (0, 0, 0),
                             (self.button[0],0,self.button[0], self.button[1]), 5)
        if keys[pygame.K_DOWN]:
            pygame.draw.rect(self.surf, (255, 0, 0),
                             (self.button[0], self.button[1], self.button[0], self.button[1]))
            pygame.draw.rect(self.surf, (0, 0, 0), (self.button[0], self.button[1], self.button[0], self.button[1]),
                             5)
        else:
            pygame.draw.rect(self.surf, (255, 255, 255),
                             (self.button[0], self.button[1], self.button[0], self.button[1]))
            pygame.draw.rect(self.surf, (0, 0, 0),
                             (self.button[0], self.button[1], self.button[0], self.button[1]), 5)


        up = pygame.draw.rect(self.surf, (0,0,0), (self.button[0],0,self.button[0], self.button[1]), 5)
        down = pygame.draw.rect(self.surf, (0,0,0), (self.button[0], self.button[1], self.button[0], self.button[1]), 5)
        left = pygame.draw.rect(self.surf, (0,0,0), (0, self.button[1], self.button[0], self.button[1]), 5)
        right = pygame.draw.rect(self.surf, (0, 0, 0), (self.button[0]*2, self.button[1], self.button[0], self.button[1]), 5)








        self.draw()

    def draw(self):
        window.blit(self.surf, self.rect)


k = KeyMapper()

player = [100, 100]  # starting location
speed = 20
while running:  # shorthand while running == True:

    window.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        '''
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player[0] -= speed
            if event.key == pygame.K_RIGHT:
                player[0] += speed
            if event.key == pygame.K_UP:
                player[1] -= speed
            if event.key == pygame.K_DOWN:
                player[1] += speed
        '''
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        player[0] += speed
    if keys[pygame.K_LEFT]:
        player[0] -= speed
    if keys[pygame.K_UP]:
        player[1] -= speed
    if keys[pygame.K_DOWN]:
        player[1] += speed

    print(keys)

    pygame.draw.circle(surface=window, color=(0, 0, 0), center=player, radius=20)
    k.handle()
    pygame.display.flip()
    clock.tick(fps)
