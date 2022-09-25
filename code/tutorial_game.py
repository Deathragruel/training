import pygame, time
from sys import exit
from random import randint, choice

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        player_walk_1 = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
        player_walk_2 = pygame.image.load('graphics/player/player_walk_2.png').convert_alpha()
        self.walk = [player_walk_1, player_walk_2]
        self.index = 0
        self.jump = pygame.image.load('graphics/player/jump.png').convert_alpha()
        
        self.image = self.walk[self.index]
        self.rect = self.image.get_rect(midbottom = (80, 300))
        self.gravity = 1
        self.velocity = 0
        self.pos = pygame.math.Vector2(self.rect.midbottom)

        self.jump_sound = pygame.mixer.Sound('audio/audio_jump.mp3')
        # 0 to 1 for loudness
        self.jump_sound.set_volume(0.025)
    
    def apply_gravity(self, dt):
        self.velocity += self.gravity 
        self.rect.y += self.velocity * dt * 60
        if self.rect.bottom >= 300: 
            self.reset()

    def player_input(self, dt):
        # keys has a slight delay in contrast to event loop although it doesn't
        # matter too much.
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.velocity -= 20
            self.rect.y += self.velocity * dt * 60
            if self.rect.bottom >= 300:
                self.reset()
            if self.rect.bottom <= 90: 
                self.rect.bottom = 90
                self.rect.bottom += dt
                for i in range()
            self.jump_sound.play()

    def animate(self, dt):
        if self.rect.bottom < 300:
            self.image = self.jump
        else:
            self.index += 5 * dt
            if self.index >= len(self.walk): self.index = 0
            self.image = self.walk[int(self.index)]

    def update(self):
        if self.rect.bottom >= 300:
            self.reset()
        self.apply_gravity(dt)
        self.player_input(dt)
        self.animate(dt)
        if self.rect.bottom <= 90: self.rect.bottom = 90

    def reset(self):
        self.velocity = 0
        self.rect.bottom = 300

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()
        if type == 'fly':
            fly_1 = pygame.image.load('graphics/fly/fly1.png').convert_alpha()
            fly_2 = pygame.image.load('graphics/fly/fly2.png').convert_alpha()
            self.frames = [fly_1, fly_2]
            y_pos = randint(100, 210)
        else:
            snail_1 = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
            snail_2 = pygame.image.load('graphics/snail/snail2.png').convert_alpha()
            self.frames = [snail_1, snail_2]
            y_pos = 300

        self.index = 0
        self.image = self.frames[self.index]
        self.rect = self.image.get_rect(midbottom = (randint(900, 1100), y_pos))
        self.pos = pygame.math.Vector2(self.rect.topleft)
 
    def animate(self):
        self.index += 0.1
        if self.index >= len(self.frames): self.index = 0
        self.image = self.frames[int(self.index)]

    def update(self, dt):
        self.animate()
        self.pos.x -= 5 * dt * 60
        self.rect.x = round(self.pos.x)
        self.destroy()

    def destroy(self):
        if self.rect.right <= 0:
            self.kill()

def display_score(score):
    global current_time
    current_time = (pygame.time.get_ticks()//1000) - start_time
    score_surface = test_font.render(f'Score: {current_time}', False, (64, 64, 64))
    score_rect = score_surface.get_rect(center = (400, 50))
    if score >= 0:
        score_surface = test_font.render(f'Score: {score}', False, (0, 0, 0))
        score_rect = score_surface.get_rect(center = (400, 80))
    screen.blit(score_surface, score_rect)

def display_text(contents, rect_position_from_center):
    text_surface = test_font.render(contents, False, (0, 0, 0))
    text_rect = text_surface.get_rect(center=rect_position_from_center)
    screen.blit(text_surface, text_rect)

# def obstacle_movement(obstacle_list):
    # if obstacle_list:
        # for obstacle_rect in obstacle_list:
            # obstacle_rect.x -= 5

            # if obstacle_rect.bottom == 300:
                # screen.blit(snail_surface, obstacle_rect)
            # else:
                # screen.blit(fly_surface, obstacle_rect)
        
        # obstacle_list = [obstacle for obstacle in obstacle_list if
                # obstacle.right > 0]

        # return obstacle_list
    # else:
        # return []

# def collisions(player, obstacles):
    # if obstacles:
        # for obstacle_rect in obstacles:
            # if player.colliderect(obstacle_rect):
                # score = current_time
                # return False
    # return True

def collision_sprite():
    # The boolean indicates whether or not the sprite in the group that
    # collided with the player will be destroyed or not.
    if pygame.sprite.spritecollide(player.sprite, obstacle_group, False):
        obstacle_group.empty()
        return False
    else:
        return True

# def player_animation():
    # global player_surface, player_index
    # play walking animation if the player is on the floor
    # display the jump surface when player is on the floor
    # if player_rect.bottom < 300:
        # jump
        # player_surface = player_jump
    # else:
        # walk
        # player_index += 0.1
        # if player_index >= len(player_walk): player_index = 0
        # player_surface = player_walk[int(player_index)]

pygame.init()
bg_music = pygame.mixer.Sound('audio/music.wav')
bg_music.set_volume(0.025)
screen = pygame.display.set_mode((800, 400))
screen_rect = screen.get_rect()
pygame.display.set_caption('Runner')
# to check the framerate
clock = pygame.time.Clock()
# For getting the font type and size of text
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)
game_active = False
score = 0
start_time = 0

# Groups
# Group single so we can access the player at any time with .sprite
player = pygame.sprite.GroupSingle()
player.add(Player())

obstacle_group = pygame.sprite.Group()

sky_surface = pygame.image.load('graphics/sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()
# To make text from a specific font with or without antialiasing and a certain
# color
# text_surface = test_font.render('My game', False, (64, 64, 64))
# text_rect = text_surface.get_rect(center = (400, 50))

# Obstacles
# snail_frame_1 = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
# snail_frame_2 = pygame.image.load('graphics/snail/snail2.png').convert_alpha()
# snail_frames = [snail_frame_1, snail_frame_2]
# snail_frame_index = 0
# snail_surface = snail_frames[snail_frame_index]

# fly_frame_1 = pygame.image.load('graphics/fly/fly1.png').convert_alpha()
# fly_frame_2 = pygame.image.load('graphics/fly/fly2.png').convert_alpha()
# fly_frames = [fly_frame_1, fly_frame_2]
# fly_frame_index = 0
# fly_surface = fly_frames[fly_frame_index]

# obstacle_rect_list = []

# player_walk_1 = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
# player_walk_2 = pygame.image.load('graphics/player/player_walk_2.png').convert_alpha()
# player_walk = [player_walk_1, player_walk_2]
# player_index = 0
# player_jump = pygame.image.load('graphics/player/jump.png').convert_alpha()

# player_surface = player_walk[player_index]
# player_rect = player_surface.get_rect(midbottom=(80, 300))
# player_gravity = 0

# Intro screen
player_stand = pygame.image.load('graphics/player/player_stand.png').convert_alpha()
# rotates, filters and resizes surface
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rect = player_stand.get_rect(center = (400, 200))

# timer (every 1500 milliseconds)
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)

# snail_animation_timer = pygame.USEREVENT + 2
# pygame.time.set_timer(snail_animation_timer, 500)

# fly_animation_timer = pygame.USEREVENT + 3
# pygame.time.set_timer(fly_animation_timer, 200)
previous_time = time.time()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # documentation suggests that pygame.quit() is unnecessary to call
            # before exiting.
            exit()
        if game_active:
            # if event.type == pygame.MOUSEBUTTONDOWN:
                # if player_rect.collidepoint(event.pos) and player_rect.bottom >= 300:
                    # player_gravity = -20
            # if event.type == pygame.KEYDOWN:
                # if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                    # player_gravity = -20
            if event.type == obstacle_timer:
                # This if statement triggers if 1 and does not trigger if 0
                obstacle_group.add(Obstacle(choice(['fly', 'snail',
                'snail', 'snail'])))
                # if randint(0, 2):
                    # obstacle_rect_list.append(snail_surface.get_rect(midbottom=(randint(900, 1100), 300)))
                # else:
                    # obstacle_rect_list.append(fly_surface.get_rect(midbottom=(randint(900,
                        # 1100), randint(100, 210)))) 
            # if event.type == snail_animation_timer:
                # if snail_frame_index == 0: snail_frame_index = 1
                # else: snail_frame_index = 0
                # snail_surface = snail_frames[snail_frame_index]
            # if event.type == fly_animation_timer:
                # if fly_frame_index == 0: fly_frame_index = 1
                # else: fly_frame_index = 0
                # fly_surface = fly_frames[fly_frame_index]

        else:    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    game_active = True
                    start_time = pygame.time.get_ticks()//1000
    
    if game_active:
        bg_music.play(-1)
        
        now = time.time()
        dt = now - previous_time
        previous_time = now
        # draw all elements
        # blit == block image transfer
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))
        # Drawing twice so the color is retained and the borders are larger.
        # pygame.draw.rect(screen, '#c0e8ec', text_rect)
        # pygame.draw.rect(screen, '#c0e8ec', text_rect, 10)
        # screen.blit(text_surface, text_rect)
        display_score(-1)
        
        # snail_rect.x -= 4
        # So, apparently you do not need indentation for one line of if statement.
        # if snail_rect.right <= 0: snail_rect.left = 800
        # screen.blit(snail_surface, snail_rect)
    
        # Player
        # player_gravity += 1
        # player_rect.y += player_gravity
        # if player_rect.bottom >= 300: player_rect.bottom = 300
        # player_animation()
        # screen.blit(player_surface, player_rect)
        
        player.draw(screen)
        player.sprite.update()

        obstacle_group.draw(screen)
        obstacle_group.update(dt)

        # Obstacle movement
        # obstacle_rect_list = obstacle_movement(obstacle_rect_list)

        # collisions
        # game_active = collisions(player_rect, obstacle_rect_list)
        game_active = collision_sprite()
    
        # keys = pygame.key.get_pressed()
        # if keys[pygame.K_SPACE]:
            # print("jump")
    
        # if player_rect.colliderect(snail_rect):
            # print("collision")
    
        # mouse_pos = pygame.mouse.get_pos()
        # if player_rect.collidepoint(mouse_pos):
            # print(pygame.mouse.get_pressed())
    
        # collisions
        # if snail_rect.colliderect(player_rect):
            # score = current_time
            # game_active = False
    
    else:
        bg_music.stop()
        screen.fill((94, 129, 162))
        screen.blit(player_stand, player_stand_rect)
        # obstacle_rect_list.clear()
        # player_rect.midbottom = (80, 300)
        # player_gravity = 0
        player.sprite.reset()
        display_text('Runner', (400, 30))
        display_text('Press "e" to start the game', (400, 350))
        display_score(score)
    
    # update everything
    pygame.display.update()
    # to set the framerate 'ceiling' to 60fps
    clock.tick(1)
