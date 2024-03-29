from os import kill
import pygame
from sys import exit
from random import randint, choice

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # CHANGES

        # PROBLEMS

        # Idle 2 & 13 
        player_idle_2 = pygame.image.load('collabprojects/Simple Platformer/png/Sprite/Idle (2).png').convert_alpha()
        player_idle_2 = pygame.transform.scale(player_idle_2, (100,158))

        player_idle_13 = pygame.image.load('collabprojects/Simple Platformer/png/Sprite/Idle (13).png').convert_alpha()
        player_idle_13 = pygame.transform.scale(player_idle_13, (100,158))

        # animation index
        self.player_idle = [player_idle_2, player_idle_13]
        self.player_idle_index = 0

        # player walk
        player_walk_1 = pygame.image.load('collabprojects/Simple Platformer/png/Sprite/Walk (1).png').convert_alpha()
        player_walk_1 = pygame.transform.scale(player_walk_1, (100,158))

        player_walk_4 = pygame.image.load('collabprojects/Simple Platformer/png/Sprite/Walk (4).png').convert_alpha()
        player_walk_4 = pygame.transform.scale(player_walk_4, (100,158))

        # player walk index
        self.player_walk = [player_walk_1, player_walk_4]
        self.player_walk_index = 0

        # resized player jump
        self.player_jump = pygame.image.load("collabprojects/Simple Platformer/png/Sprite/Jump (4).png").convert_alpha()
        self.player_jump = pygame.transform.scale(self.player_jump, (100,158))

        self.image = self.player_idle[self.player_idle_index]
        self.image = pygame.image.load('collabprojects/Simple Platformer/png/Sprite/Idle (2).png').convert_alpha() or pygame.image.load('collabprojects/Simple Platformer/png/Sprite/Idle (2)l.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (100,158))
        self.rect = self.image.get_rect(midbottom = (120,800))
        self.gravity = 0
        self.flip = False

        # jump sound
        self.jump_sound = pygame.mixer.Sound('collabprojects/Simple Platformer/png/music/JumpSound.mp3')
        self.jump_sound.set_volume(0.05)

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 800:
            self.gravity = -20
            self.jump_sound.play()

            # left and right arrow to move left and right
        if keys[pygame.K_RIGHT]:
            self.rect.x += 4
            self.player_walk_index += 0.1
            if self.player_walk_index >= len(self.player_walk): self.player_walk_index = 0
            self.image = self.player_walk[int(self.player_walk_index)]
            self.flip = False
        if keys[pygame.K_LEFT]:
            self.rect.x -= 4
            self.player_walk_index += 0.1
            if self.player_walk_index >= len(self.player_walk): self.player_walk_index = 0
            self.image = self.player_walk[int(self.player_walk_index)]
            self.flip = True

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

    def draw(self):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), (self.rect.x - 7, self.rect.y - 5))

    def update(self):
        self.animation_state()
        self.apply_gravity()
        self.player_input()
        self.draw()

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

class IntroPlayer(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        player_idle_2 = pygame.image.load('collabprojects/Simple Platformer/png/Sprite/Idle (2).png').convert_alpha()
        player_idle_2 = pygame.transform.scale(player_idle_2, (220,346))
        player_idle_13 = pygame.image.load('collabprojects/Simple Platformer/png/Sprite/Idle (13).png').convert_alpha()
        player_idle_13 = pygame.transform.scale(player_idle_13, (220,346))

        self.player_idle = [player_idle_2, player_idle_13]
        self.player_idle_index = 0

        self.image = self.player_idle[self.player_idle_index]
        self.image = pygame.image.load('collabprojects/Simple Platformer/png/Sprite/Idle (2).png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (220,346 ))
        self.rect = self.image.get_rect(midbottom = (703,630))

    def animation_state(self):
        self.player_idle_index += 0.1
        if self.player_idle_index >= len(self.player_idle): self.player_idle_index = 0
        self.image = self.player_idle[int(self.player_idle_index)]


    def update(self):
        self.animation_state()

pygame.init()

screen = pygame.display.set_mode((1406,900))
pygame.display.set_caption('Santa Jump')
clock = pygame.time.Clock()
test_font = pygame.font.Font('collabprojects/Simple Platformer/png/font/Frostbite.ttf', 50)
game_active = False

background_surf = pygame.image.load('collabprojects/Simple Platformer/png/Background/background_surface.png').convert_alpha()
ground_surf = pygame.image.load('collabprojects/Simple Platformer/png/Background/ground_surface.png').convert_alpha()

intro_music = pygame.mixer.Sound('collabprojects/Simple Platformer/png/music/FadeIntoWhite.mp3')

# Groups
player = pygame.sprite.GroupSingle()
player.add(Player())

ice_platform = pygame.sprite.GroupSingle() 
ice_platform.add(Platform())

coin = pygame.sprite.GroupSingle()
coin.add(Goldcoin())

introplayer = pygame.sprite.GroupSingle()
introplayer.add(IntroPlayer())

# Sound buttons
sound_on = pygame.image.load('collabprojects/Simple Platformer/png/Sprite/volume.png').convert_alpha()
sound_on = pygame.transform.scale(sound_on, (50,50))
sound_on_rect = sound_on.get_rect(topleft = (25,25))
sound_off = pygame.image.load('collabprojects/Simple Platformer/png/Sprite/mute.png').convert_alpha()
sound_off = pygame.transform.scale(sound_off, (50,50))
sound_off_rect = sound_off.get_rect(topleft = (25,25))

# Intro Screen
intro_text = test_font.render('" Press Space to Start "', False, (100,115,150))
intro_text_rect = intro_text.get_rect(center = (703,750))

game_title = test_font.render('Jump Santa', False, (0,50,130))
game_title = pygame.transform.rotozoom(game_title, 0, 2)
game_title_rect = game_title.get_rect(center = (703,100))

# Intro walk animation
intro_animation = pygame.USEREVENT + 1
pygame.time.set_timer(intro_animation, 1000)

# Intro music
intro_music = pygame.mixer.Sound('collabprojects/Simple Platformer/png/music/FadeIntoWhite.mp3')
intro_music.set_volume(0.05)

# Game music
game_music1 = pygame.mixer.Sound('collabprojects/Simple Platformer/png/music/HappyFlight.mp3')
game_music1.set_volume(0.05)
# game_music2 = pygame.mixer.music.load('collabprojects/Simple Platformer/png/music/Snowscape.mp3')
# game_music2.set_volume(0.1)
# game_music3 = pygame.mixer.music.load('collabprojects/Simple Platformer/png/music/CrystalWaver.mp3')
# game_music3.set_volume(0.1)

def pause_track():
    pygame.mixer.pause()

def resume_track():
    pygame.mixer.unpause()

# Taking the coin
def takeCoin():
    pygame.sprite.spritecollide(player.sprite, coin, True)
    # coin_taking_sound = pygame.mixer.Sound('collabprojects/Simple Platformer/png/music/TakeCoin.mp3')
    # coin_taking_sound.play()


# Intro fade
def fade(): 
    fade = pygame.Surface((1406,900))
    fade.blit(background_surf, (0,0))
    for alpha in range(0, 100):
        fade.set_alpha(alpha)
        screen.blit(fade, (0,0))
        pygame.display.update()
        pygame.time.delay(10)

# Winning/Ending
# player_down = pygame.image.load('collabprojects/Simple Platformer/png/Sprite/Dead (17).png').convert_alpha()
# player_down_rect = player_down.get_rect(center = (700 , 450))

# finish_message = test_font.render('Santa sold his soul to capitalism', False, (0, 50, 130))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active == False:
            intro_music.play(loops = -1)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                pygame.mixer.fadeout(1000)
                fade()
                game_active = True


    if game_active:
        screen.blit(background_surf, (0,0))
        # screen.blit(ground_surf, (0,700))
        # screen.blit(ground_surf, (300,700))
        # screen.blit(ground_surf, (600,700))
        # screen.blit(ground_surf, (900,700))
        # screen.blit(ground_surf, (1200,700))
        # screen.blit(ground_surf, (1500,700))
        # screen.blit(ground_surf, (1800,700))

        # player.draw(screen)
        player.update()
        ice_platform.draw(screen)
        coin.draw(screen)
        coin.update()
        takeCoin()

    else:
        screen.fill((176,217,247))
        screen.blit(intro_text, intro_text_rect)
        screen.blit(game_title, game_title_rect)
        introplayer.draw(screen)
        introplayer.update()
        
    # mouse_pos = pygame.mouse.get_pos()
    # print(mouse_pos)
    

    pygame.display.update()
    clock.tick(60)