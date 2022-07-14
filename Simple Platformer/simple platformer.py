import pygame
from sys import exit

# The Player Class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        player_walk1 = pygame.image.load("png/Sprite/Walk (1).png").convert_alpha()
        player_walk2 = pygame.image.load("png/Sprite/Walk (2).png").convert_alpha()
        self.player_walk = [player_walk1,player_walk2]
        self.player_index = 0
        self.player_stand = pygame.image.load("png/Sprite/Idle (1).png").convert_alpha()
        self.player_jump = pygame.image.load("png/Sprite/Jump (4).png")

        self.image = self.player_walk[self.player_index]
        self.image_scaled = pygame.transform.scale(self.image, (25,25))
        self.rect = self.image_scaled.get_rect(midbottom = (80 , 300))
        self.gravity = 0 

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.gravity = -20
            # self.jump_sound.play()

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 300:
            self.rect.bottom = 300

    def animation_state(self):
        if self.rect.bottom < 300:
            self.image = self.player_jump
        else:
            self.image = self.player_stand
            # self.player_index += 0.1
            # if self.player_index >= len(self.player_walk):
            #     self.player_index = 0
            # self.image = self.player_walk[int(self.player_index)]

    def player_size(self):
        
        player_resized = pygame.transform.scale(self.image, (50, 100))
        player_stand_rectangle = player_stand.get_rect(center = (400,200))



    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animation_state()


# player sprite (single group)
# enemy sprite (single group)
# coin (single group)
# platforms (single group)
# audio(bgm, collision sound, etc)
# ending/starting screen
# 


pygame.init()
# screen
screen = pygame.display.set_mode((1900, 1200))
pygame.display.set_caption('Santa Jump')

# background and ground surface
background_surf = pygame.image.load('png/Background/background_surface.png').convert_alpha()
ground_surf = pygame.image.load('png/Background/ground_surface.png').convert_alpha()

game_active = True

player = pygame.sprite.GroupSingle()
player.add(Player())

# while game is running
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    

    if game_active:
        screen.blit(background_surf, (0,0))
        screen.blit(ground_surf, (0,0))
        
        player.draw(screen)
        player.update()

    pygame.display.update()