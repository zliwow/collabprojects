from platform import platform
import pygame
from sys import exit
from random import randint, choice

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # CHANGES
        # resized display screen and background to be compatible with my monitor

        # resized and updated the player surface variable. resize to (100, 158), or something else if you find something better
        # if you wanna use new sprites, you have to resize them in paint 3d tool.
        # go to canvas, go to crop, and crop out the blank spaces.
        # you can see the pixel width and height on the right. try to set it as close to 350, 550 as possible to keep things similar
        
        # added idle animation
        # added left and right movement
        # inverted sprites to make left movement look more natural. (added an "l" at the end for left invert)

        # PROBLEMS
        # When character jumps, it uses walking animation instead of jumping one. applies to both left and right
        # Idle animation is fixed to look right. even after you move left, as soon as you let go of left arrow, character will look right.

        # Idle 2 & 13 
        player_idle_2 = pygame.image.load('collabprojects/Simple Platformer/png/Sprite/Idle (2).png').convert_alpha()
        player_idle_2 = pygame.transform.scale(player_idle_2, (100,158))
        player_idle_2l = pygame.image.load('collabprojects/Simple Platformer/png/Sprite/Idle (2)l.png').convert_alpha()
        player_idle_2l = pygame.transform.scale(player_idle_2l, (100,158))

        player_idle_13 = pygame.image.load('collabprojects/Simple Platformer/png/Sprite/Idle (13).png').convert_alpha()
        player_idle_13 = pygame.transform.scale(player_idle_13, (100,158))
        player_idle_13l = pygame.image.load('collabprojects/Simple Platformer/png/Sprite/Idle (13)l.png').convert_alpha()
        player_idle_13l = pygame.transform.scale(player_idle_13l, (100,158))

        # animation index
        self.player_idle = [player_idle_2, player_idle_13]
        self.player_idle_index = 0
        self.player_idlel = [player_idle_2l, player_idle_13l]
        self.player_idle_indexl = 0

        # player walk
        player_walk_1 = pygame.image.load('collabprojects/Simple Platformer/png/Sprite/Walk (1).png').convert_alpha()
        player_walk_1 = pygame.transform.scale(player_walk_1, (100,158))
        player_walk_1l = pygame.image.load('collabprojects/Simple Platformer/png/Sprite/Walk (1)l.png').convert_alpha()
        player_walk_1l = pygame.transform.scale(player_walk_1l, (100,158))

        player_walk_4 = pygame.image.load('collabprojects/Simple Platformer/png/Sprite/Walk (4).png').convert_alpha()
        player_walk_4 = pygame.transform.scale(player_walk_4, (100,158))
        player_walk_4l = pygame.image.load('collabprojects/Simple Platformer/png/Sprite/Walk (4)l.png').convert_alpha()
        player_walk_4l = pygame.transform.scale(player_walk_4l, (100,158))

        # player walk index
        self.player_walk = [player_walk_1, player_walk_4]
        self.player_walk_index = 0
        self.player_walkl = [player_walk_1l, player_walk_4l]
        self.player_walk_indexl = 0

        # resized player jump
        self.player_jump = pygame.image.load("collabprojects/Simple Platformer/png/Sprite/Jump (4).png").convert_alpha()
        self.player_jump = pygame.transform.scale(self.player_jump, (100,158))
        self.player_jumpl = pygame.image.load("collabprojects/Simple Platformer/png/Sprite/Jump (4)l.png").convert_alpha()
        self.player_jumpl = pygame.transform.scale(self.player_jumpl, (100,158))

        self.image = self.player_idle[self.player_idle_index] or self.player_idlel[self.player_idle_indexl]
        self.image = pygame.image.load('collabprojects/Simple Platformer/png/Sprite/Idle (2).png').convert_alpha() or pygame.image.load('collabprojects/Simple Platformer/png/Sprite/Idle (2)l.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (100,158))
        self.rect = self.image.get_rect(midbottom = (120,800))
        self.gravity = 0

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 800:
            self.gravity = -20
            # self.jump_sound.play()

            # left and right arrow to move left and right
        if keys[pygame.K_RIGHT]:
            self.rect.x += 4
            self.player_walk_index += 0.1
            if self.player_walk_index >= len(self.player_walk): self.player_walk_index = 0
            self.image = self.player_walk[int(self.player_walk_index)]
        if keys[pygame.K_LEFT]:
            self.rect.x -= 4
            self.player_walk_indexl += 0.1
            if self.player_walk_indexl >= len(self.player_walkl): self.player_walk_indexl = 0
            self.image = self.player_walkl[int(self.player_walk_indexl)]

            # updated ground to 800
    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 800:
            self.rect.bottom = 800

    def animation_state(self):
        if self.rect.bottom < 800:
            self.image = self.player_jump
        else:
            self.player_idle_index += 0.1
            if self.player_idle_index >= len(self.player_idle): self.player_idle_index = 0
            self.image = self.player_idle[int(self.player_idle_index)]

    def update(self):
        self.animation_state()
        self.apply_gravity()
        self.player_input()

class Platform(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
    
        self.image = pygame.image.load("collabprojects/Simple Platformer/png/Background/ground_surface.png").convert_alpha()
        # rect size unsure
        self.rect = self.image.get_rect(midbottom = (120,800))



class Goldcoin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        goldcoin_1 = pygame.image.load("collabprojects/Simple Platformer/png/GoldCoinSprite/Coin1.png").convert_alpha()
        goldcoin_2 = pygame.image.load("collabprojects/Simple Platformer/png/GoldCoinSprite/Coin2.png").convert_alpha()
        goldcoin_3 = pygame.image.load("collabprojects/Simple Platformer/png/GoldCoinSprite/Coin3.png").convert_alpha()
        goldcoin_4 = pygame.image.load("collabprojects/Simple Platformer/png/GoldCoinSprite/Coin4.png").convert_alpha()
        goldcoin_5 = pygame.image.load("collabprojects/Simple Platformer/png/GoldCoinSprite/Coin5.png").convert_alpha()
        goldcoin_6 = pygame.image.load("collabprojects/Simple Platformer/png/GoldCoinSprite/Coin6.png").convert_alpha()

        self.coin_spin = [goldcoin_1, goldcoin_2, goldcoin_3, goldcoin_4, goldcoin_5, goldcoin_6]
        self.image = pygame.image.load("collabprojects/Simple Platformer/png/GoldCoinSprite/Coin1.png").convert_alpha()
        self.rect = self.image.get_rect(midbottom = (1200,800))
        self.coin_spin_index = 0


    def coin_animation(self):
        self.coin_spin_index += 0.1
        if self.coin_spin_index >= len(self.coin_spin): self.coin_spin_index = 0
        self.image = self.coin_spin[int(self.coin_spin_index)]


    def update(self):
        self.coin_animation()








        

pygame.init()

screen = pygame.display.set_mode((1406,900))
pygame.display.set_caption('Santa Jump')
clock = pygame.time.Clock()
game_active = True

background_surf = pygame.image.load('collabprojects/Simple Platformer/png/Background/background_surface.png').convert_alpha()
ground_surf = pygame.image.load('collabprojects/Simple Platformer/png/Background/ground_surface.png').convert_alpha()

player = pygame.sprite.GroupSingle()
player.add(Player())

ice_platform = pygame.sprite.GroupSingle()
ice_platform.add(Platform())

coin = pygame.sprite.GroupSingle()
coin.add(Goldcoin())

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    if game_active:
            screen.blit(background_surf, (0,0))
            # screen.blit(ground_surf, (0,700))
            # screen.blit(ground_surf, (300,700))
            # screen.blit(ground_surf, (600,700))
            # screen.blit(ground_surf, (900,700))
            # screen.blit(ground_surf, (1200,700))
            # screen.blit(ground_surf, (1500,700))
            # screen.blit(ground_surf, (1800,700))

            player.draw(screen)
            player.update()
            ice_platform.draw(screen)
            coin.draw(screen)
            coin.update()

            



    mouse_pos = pygame.mouse.get_pos()
    print(mouse_pos)

    pygame.display.update()
    clock.tick(60)