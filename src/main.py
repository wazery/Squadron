# file: main.py	--> The main module
# ###################################################
# Copyright (C) 2011 Squadron by Islam Wazery
# al.wazery@gmail.com
# This file is part of Squadron.
#
# Squadron is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the
# Free Software Foundation, Inc.,
# 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
# ###################################################

import pygame, random, os, pygame.mixer
import loader

from projectile import Projectile
from player import PlayerBottom
from player import PlayerSide
from enemy import Enemy
from particle import Particle
from pygame.locals import *

def main():
    
    def create_particles(number, x, y, image):
	for count in range(number):
	    for particle_count in range(MAX_PARTICLES):
		if particles[particle_count].active == False:
		    particles[particle_count].active = True
		    particles[particle_count].rect.left = x
		    particles[particle_count].rect.top = y
		    particles[particle_count].image = image
		    if number > 15:
			particles[particle_count].move_count = random.randint(20, 30)
		    else:
			particles[particle_count].move_count = random.randint(10, 17)
		    if random.randint(0, 10) > 5:
			particles[particle_count].vector_x = 0 - random.randint(0, 4)
			particles[particle_count].vector_y = 0 - random.randint(0, 4)
		    else:
			particles[particle_count].vector_x = random.randint(0, 4)
			particles[particle_count].vector_y = random.randint(0, 4)
		    break

    # Game Constants..
    SCREEN_HEIGHT = 468
    SCREEN_WIDTH = 640

    high_score = 750000

    TITLE_SCREEN_MODE = 1
    GAME_MODE = 2
    FPS = 60

    NUMBER_OF_LIVES = 6
    MAX_ENEMIES = 15
    PLAYER_BULLETS = 40
    MAX_ENEMY_BULLETS = 30
    MAX_UFOS = 1
    MAX_PARTICLES = 200

    # Counters..
    attack_timer = 0
    attack_max = 70
    ufo_attack_timer = 0
    ufo_attack_max = 500
    max_enemy_speed = 2
    max_ufo_speed = 2

    game_wave = 1
    enemy_killed = 0
    wave_break = 100
    wave_target_kills = 50
    game_over = False
    game_over_timer = 500
    game_victory = False
    game_victory_particle_timer = 0

    player_score = 0
    player_lives = 7
    player_flash_timer = 0
    player_flash_on = False

    # Game control stuff..
    game_mode = TITLE_SCREEN_MODE
    title_menu_choice = 0
    title_lit_message = True

    beaten_high_score = False

    enemy_fire_timer = 0
    enemy_fire_max = 50

    title_freeplay_timer = 0
    title_freeplay_on = False

    # Init the game and creating the display surface..
    pygame.init()
    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    #SCREEN_WIDTH, SCREEN_HEIGHT = screen.get_size()
    pygame.display.set_caption("Squadron: Yet Another Arcade Game!")
    clock = pygame.time.Clock()

    # Creating game fonts..
    pygame.font.init()
    game_font = pygame.font.Font(os.path.join("gfx", "04b_25__.ttf"), 18)
    game_font_large = pygame.font.Font(os.path.join("gfx", "04b_25__.ttf"), 36)
    game_font_xl = pygame.font.Font(os.path.join("gfx", "04b_25__.ttf"), 46)

    # Show loading message...
    screen.fill((0,0,0))
    screen.blit(game_font.render("Loading....", 0, ((176, 0, 0))), (270, SCREEN_HEIGHT / 2 - 36))
    pygame.display.flip()

    # Loading game gfx..
    player_bullet_image = pygame.image.load(os.path.join("gfx", "bullet1.png")).convert()
    enemy_bullet_image = pygame.image.load(os.path.join("gfx", "bullet2.png")).convert()
    invader_image = pygame.image.load(os.path.join("gfx", "invader.png")).convert()
    shooter_image = pygame.image.load(os.path.join("gfx", "shooter_invaders.png")).convert()
    transient_image = pygame.image.load(os.path.join("gfx", "Transient.png")).convert()
    ufo_image = pygame.image.load(os.path.join("gfx", "ufo.png")).convert()
    player_health_image = pygame.Surface((8, 16))
    player_health_image.fill((176, 0, 0))

    # Sort the sound driver
    pygame.mixer.quit()
    sound = pygame.mixer.init()

    # Loading all game sounds..
    damage_sound = pygame.mixer.Sound(os.path.join("sound", "damage.wav"))
    exit_sound = pygame.mixer.Sound(os.path.join("sound", "exit.wav"))
    expolde_sound = pygame.mixer.Sound(os.path.join("sound", "explode1.wav"))
    lazer_sound = pygame.mixer.Sound(os.path.join("sound", "lazer.wav"))
    menu_mov_sound = pygame.mixer.Sound(os.path.join("sound", "menu_move.wav"))
    menu_select_sound = pygame.mixer.Sound(os.path.join("sound", "menu_select.wav"))
    wave_sound = pygame.mixer.Sound(os.path.join("sound", "newwave.wav"))
    player_dead_sound = pygame.mixer.Sound(os.path.join("sound", "player_dead.wav"))
    shoot2_sound = pygame.mixer.Sound(os.path.join("sound", "shoot2.wav"))
    start_sound = pygame.mixer.Sound(os.path.join("sound", "start.wav"))
    ufo_sound = pygame.mixer.Sound(os.path.join("sound", "ufo.wav"))
    ufo_sound.set_volume(0.35)
    win_sound = pygame.mixer.Sound(os.path.join("sound", "win.wav"))

    # Create some particle images..
    red_particle_image = pygame.Surface((8, 8))
    red_particle_image.fill((176, 0, 0))

    green_particle_image = pygame.Surface((8, 8))
    green_particle_image.fill((31, 92, 14))

    blue_particle_image = pygame.Surface((8, 8))
    blue_particle_image.fill((46, 102, 187))

    yellow_particle_image = pygame.Surface((8, 8))
    yellow_particle_image.fill((255, 206, 0))

    gray_particle_image = pygame.Surface((8, 8))
    gray_particle_image.fill((88, 88, 88))
   
    # Create the players... TODO: Clean this!
    #player_side = Player(SCREEN_WIDTH, SCREEN_HEIGHT, side= True)
    #player_bottom = Player(SCREEN_WIDTH, SCREEN_HEIGHT, bottom= True)
    player_bottom = PlayerBottom(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_WIDTH / 2, SCREEN_HEIGHT - 35)
    player_side = PlayerSide(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_WIDTH -35, SCREEN_HEIGHT / 2)

    player_score = 0
    player_fire_rate = 5
    player_fire_delay_right = 0
    player_fire_delay_left = 0
    player_shield = 9
    player_lives = 10
    player_flash_on = False
    player_flash_timer = 0

    # Prepare the player pointed projectiles!
    player_bullets = []
    for count in range(PLAYER_BULLETS):
        player_bullets.append(Projectile(SCREEN_WIDTH, SCREEN_HEIGHT, player_bullet_image))
        player_bullets[count].active = False

    # Enemy bullets..
    enemy_bullets = []
    for count in range(MAX_ENEMY_BULLETS):
	enemy_bullets.append(Projectile(SCREEN_WIDTH, SCREEN_HEIGHT, enemy_bullet_image))
	enemy_bullets[count].active = False

    # Prepare enemies..
    invaders = []
    shooter_invaders = []
    transient_invaders = []

    for count in range (MAX_ENEMIES):
   	# invaders 
   	invaders.append(Enemy(SCREEN_WIDTH, SCREEN_HEIGHT, invader_image))
   	invaders[count].rect.top = 0
      	invaders[count].rect.left = 0
   	invaders[count].vector_x = 0
   	invaders[count].vector_y = 0
   	invaders[count].active = False
   	invaders[count].anim_max_frame = 3
   	invaders[count].movement_type = 0

   	# shooter invaders 
   	shooter_invaders.append(Enemy(SCREEN_WIDTH, SCREEN_HEIGHT, shooter_image))
   	shooter_invaders[count].rect.top = 0
   	shooter_invaders[count].rect.left = 0
   	shooter_invaders[count].vector_x = 0
   	shooter_invaders[count].vector_y = 0
   	shooter_invaders[count].active = False
   	shooter_invaders[count].anim_max_frame = 3
   	shooter_invaders[count].movement_type = 0

   	# transient invaders 
   	transient_invaders.append(Enemy(SCREEN_WIDTH, SCREEN_HEIGHT, transient_image))
   	transient_invaders[count].rect.top = 0
   	transient_invaders[count].rect.left = 0
   	transient_invaders[count].vector_x = 0
   	transient_invaders[count].vector_y = 0
   	transient_invaders[count].active = False
   	transient_invaders[count].anim_max_frame = 3
   	transient_invaders[count].movement_type = 1
    
    ufos = []
    for count in range(MAX_UFOS):
	ufos.append(Enemy(SCREEN_WIDTH, SCREEN_HEIGHT, ufo_image))
	ufos[count].anim_max_frame = 9

    particles = []
    for count in range(MAX_PARTICLES):
        particles.append(Particle(SCREEN_WIDTH, SCREEN_HEIGHT, red_particle_image))
        particles[count].active = False   

#<<<><><><><><>||MAIN LOOP||<><><><><><><><>>>#
#<<<><><><><><><><><><><><><><><><><><><><>>>>#

    main_loop = True
    enemies_onscreen = False

    while main_loop:

        # Clear the screen (NOTE: This is not particularly efficient, but deadline is looming!)
        screen.fill((0,0,0)) 

	# Check the game mode if TITLE_SCREEN_MODE
	if game_mode == TITLE_SCREEN_MODE:

	    #-----------------------#
	    #----||TITLE SCREEN||---#
	    #-----------------------#
	    
	    # Render the game title..
	    screen.blit(game_font_xl.render("Squadron",  0, ((255, 206, 0))), (230, 100))

	    title_freeplay_timer += 1
	    if title_freeplay_timer > 30:
	    	title_freeplay_timer = 0
		if title_freeplay_on == True:
		    title_freeplay_on = False
		else:
		    title_freeplay_on = True

	    if title_freeplay_on == True:
                screen.blit(game_font.render("Insert Coin", 0, ((175, 175, 175))), (280, 380))

	    if title_menu_choice == 1:
                screen.blit(game_font.render("Start", 0, ((255, 206, 0))), (300, 225))
	    else:
                screen.blit(game_font.render("Start", 0, ((176, 0, 0))), (300, 225))           

	    if title_menu_choice == 0:
                screen.blit(game_font.render("Exit", 0, ((255, 206, 0))), (308, 250))
	    else:
                screen.blit(game_font.render("Exit", 0, ((176, 0, 0))), (308, 250))

            screen.blit(game_font.render("Z and X to fire, cursor keys control both ships", 0, ((176, 0, 0))), (120, 450))

	   # Screen Events...
	    for event in pygame.event.get():
		if event.type == pygame.QUIT:
		    main_loop = False

		elif event.type == pygame.KEYDOWN:
		    if event.key == pygame.K_UP:
			menu_mov_sound.play()
			title_menu_choice -= 1
			if title_menu_choice < 0:
                            title_menu_choice = 0

		    if event.key == pygame.K_DOWN:
			title_menu_choice += 1
			menu_mov_sound.play()
			if title_menu_choice > 1:
                            title_menu_choice = 1

		    if event.key == pygame.K_ESCAPE:
			main_loop = False 

		    if event.key == pygame.K_z or event.key == pygame.K_x or event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
			if title_menu_choice == 0:
			    # Start the games
			    start_sound.play()
			    game_mode = GAME_MODE # Switch to the game play mode
			    attack_timer = 0
			    attack_max = 70
			    ufo_attack_timer = 0
			    ufo_attack_max = 500
			    max_enemy_speed = 2
			    max_ufo_speed = 2
			    beaten_high_score = False
			    game_wave = 1
			    enemy_killed = 0
			    wave_break = 100
			    wave_target_kills = 50
			    game_over = False
			    game_over_timer = 500
			    game_victory = False
			    game_victory_particle_timer = 0
			    enemy_fire_timer = 0
			    enemy_fire_max = 50 
			    player_fire_delay_left = 0
                            player_fire_delay_right = 0
			    player_score = 0
			    player_shield = 9
			    player_lives = 7
			    player_flash_timer = 0
			    player_flash_on = False

			    # Deactivate all enemies, particles, bullets
			    for count in range(MAX_ENEMIES):
				invaders[count].active = False
				shooter_invaders[count].active = False
				transient_invaders[count].active = False

			    for count in range(MAX_PARTICLES):
				particles[count].active = False

			    for count in range(PLAYER_BULLETS):
				player_bullets[count].active = False

			    for count in range(MAX_ENEMY_BULLETS):
				enemy_bullets[count].active = False

			    for count in range(MAX_UFOS):
				ufos[count].active = False

			if title_menu_choice == 1:
			    exit_sound.play()
			    main_loop = False
        else:

	    #-----------------------#
	    #-----||GAME MODE||-----#
	    #-----------------------#

	    # Game Events...
            for event in pygame.event.get():
		if event.type == pygame.QUIT:
		    main_loop = False

		elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game_mode = TITLE_SCREEN_MODE # Switch back to the title screen
                    if event.key == pygame.K_z and player_fire_delay_left > player_fire_rate and game_over == False:
                        # Pop off a few projectiles...                    
                        for count in range(PLAYER_BULLETS):
                            if (player_bullets[count].active == False): # Find a 'free' bullet for the bottom ship
                                player_bullets[count].active = True
                                player_bullets[count].rect.top = player_bottom.rect.top
                                player_bullets[count].rect.left = player_bottom.rect.left + 12
                                player_bullets[count].vector_x = 0
                                player_bullets[count].vector_y = -9
                                player_fire_delay_left = 0
                                lazer_sound.play()                                
                                break
                    # Has side player fired
                    if event.key == pygame.K_x and player_fire_delay_left > player_fire_rate and game_over == False:
                        for count in range(PLAYER_BULLETS):
                            if (player_bullets[count].active == False):
                                player_bullets[count].active = True
                                player_bullets[count].rect.top = player_side.rect.top + 12
                                player_bullets[count].rect.left = player_side.rect.left
                                player_bullets[count].vector_x = -9
                                player_bullets[count].vector_y = 0
                                player_fire_delay_right = 0
                                lazer_sound.play()                            
                                break


		attack_timer += 1
		ufo_attack_timer += 1

		if attack_timer > attack_max and wave_break < 1 and enemy_killed < wave_target_kills and game_over == False:	
		    attack_timer = 0
		    
		    if game_wave > 2:
			enemy_type = random.randint(0, 2)
		    else:
			enemy_type = random.randint(0, 1)

		    direction = random.randint(0, 1)
		    if enemy_type == 0:
			for count in range(MAX_ENEMIES):
			    if invaders[count].active == False:
				if direction == 0: # if enemies come from left
				    invaders[count].rect.left = -32
				    invaders[count].rect.top = random.randint(0, (SCREEN_HEIGHT - 64) / 32) * 32
				    invaders[count].vector_x = max_enemy_speed
				    invaders[count].vector_y = 0
				    invaders[count].active = True
				    break
				else: # if enemies come from top
				    invaders[count].rect.left = random.randint(0, (SCREEN_WIDTH - 64) / 32) * 32
				    invaders[count].rect.top = -32
				    invaders[count].vector_x = 0
				    invaders[count].vector_y = max_enemy_speed
				    invaders[count].active = True
				    break
		    elif enemy_type == 1:
			for count in range(MAX_ENEMIES):
			    if shooter_invaders[count].active == False:
				if direction == 0: # if enemies come from left
				    shooter_invaders[count].rect.left = -32 # 32 is the icon size
				    shooter_invaders[count].rect.top = random.randint(0, (SCREEN_HEIGHT - 64) / 32) * 32
				    shooter_invaders[count].vector_x = max_enemy_speed
				    shooter_invaders[count].vector_y = 0
				    shooter_invaders[count].active = True
				    shooter_invaders[count].movement_type = 2
				    break
				else: # if enemies come from top
				    shooter_invaders[count].rect.left = random.randint(0, (SCREEN_WIDTH - 64) / 32) * 32
				    shooter_invaders[count].rect.top = -32
				    shooter_invaders[count].vector_x = 0
				    shooter_invaders[count].vector_y = max_enemy_speed
				    shooter_invaders[count].active = True
				    shooter_invaders[count].movement_type = 1
				    break
		    elif enemy_type == 2:
			for count in range(MAX_ENEMIES):
			    if shooter_invaders[count].active == False:
				if direction == 0: # if enemies come from left
				    transient_invaders[count].rect.left = -32
				    transient_invaders[count].rect.top = random.randint(0, (SCREEN_HEIGHT - 64) / 32) * 32
				    transient_invaders[count].vector_x = max_enemy_speed
				    transient_invaders[count].vector_y = random.randint(0, 1) - random.randint(0, 1)
				    transient_invaders[count].active = True
				    break
				else: # if enemies come from top
				    transient_invaders[count].rect.left = random.randint(0, (SCREEN_WIDTH - 64) / 32) * 32
				    transient_invaders[count].rect.top = -32
				    transient_invaders[count].vector_x = random.randint(0, 1) - random.randint(0, 1)
				    transient_invaders[count].vector_y = max_enemy_speed
				    transient_invaders[count].active = True
				    break

		# ufo attacks..
		for count in range(MAX_UFOS):
		    if ufos[count].active == False and ufo_attack_timer > ufo_attack_max and wave_break < 1 and game_over == False:
			ufo_attack_timer = 0
			ufo_sound.play()
			if random.randint(0, 10) > 4: # Attacking the side player
			    if random.randint(0, 10) > 4:
				ufos[count].rect.left = SCREEN_WIDTH - 32
				ufos[count].rect.top = -32
				ufos[count].vector_x = 0
				ufos[count].vector_y = max_ufo_speed
				ufos[count].active = True
			    else:
				ufos[count].rect.left = SCREEN_WIDTH -32
				ufos[count].rect.top = SCREEN_HEIGHT + 32
				ufos[count].vector_x = - max_ufo_speed
				ufos[count].vector_y = 0
				ufos[count].active = True
			else: # Attacking the bottom player
			    if random.randint(0, 10) > 4:
				ufos[count].rect.left = 32
				ufos[count].rect.top = SCREEN_HEIGHT - 32
				ufos[count].rect.vector_x = max_ufo_speed
				ufos[count].rect.vector_y = 0
				ufos[count].rect.active = True
			    else:
				ufos[count].rect.top = SCREEN_HEIGHT -32
                                ufos[count].rect.left = SCREEN_WIDTH + 32                        
                                ufos[count].vector_x = 0 - max_ufo_speed
                                ufos[count].vector_y = 0
                                ufos[count].active = True  

		# Render the particles..
		for count in range(MAX_PARTICLES):
		    if particles[count].active == True:
			particles[count].update()
			screen.blit(particles[count].image, particles[count].rect)
		
		# Update the players due to their key events..
		player_bottom.update()
		player_side.update() 
		
		# If player recovers from damage..
		if player_flash_timer > 0:
		    player_flash_on -= 1
		    if player_flash_on == True:
			player_flash_on = False
		    else:
			player_flash_on = True
		else:
		    player_flash_on = False
		
		# Render all the player projectiles..
		for count in range(PLAYER_BULLETS):
		    if (player_bullets[count].active):
			player_bullets[count].update()
			screen.blit(player_bullets[count].image, player_bullets[count].rect)

		# Render all the enemies projectiles..
		for count in range(MAX_ENEMY_BULLETS):
		    if (enemy_bullets[count].active):
			enemy_bullets[count].update
			screen.blit(enemy_bullets[count].image, enemy_bullets[count].rect)

		# Increase the delay for the players fire..
		player_fire_delay_left += 1
		player_fire_delay_right += 1

		# Update the invaders (move and draw)..
		for count in range(MAX_ENEMIES):
		    if invaders[count].active:
			invaders[count].update()
			screen.blit(invaders[count].image, invaders[count].rect, (32 * invaders[count].anim_frame, 0, 32, 32))
			# Check the invader collision with any player_bullets
			for collision_count in range(PLAYER_BULLETS):
			    if player_bullets[collision_count].active:
				if player_bullets[collision_count].rect.colliderect((invaders[count].rect.left, invaders[count].rect.top, 32, 32)):        
				    invaders[count].active = False
				    player_bullets[collision_count].active = False
				    enemy_killed += 1
				    expolde_sound.play()
				    player_score += 2000
				    create_particles(15, invaders[count].rect.left + 8, invaders[count].rect.top + 8, green_particle_image)

		# Update the shooter_invaders (move and draw)..
		for count in range(MAX_ENEMIES):
		    if shooter_invaders[count].active:
			shooter_invaders[count].update()
			screen.blit(shooter_invaders[count].image, shooter_invaders[count].rect, (32* shooter_invaders[count].anim_frame, 0, 32, 32))
			for collision_count in range(PLAYER_BULLETS):
			    if player_bullets[collision_count].active == True:
				if player_bullets[collision_count].rect.colliderect((shooter_invaders[count].rect.left, shooter_invaders[count].rect.top, 32, 32)):        
				    shooter_invaders[count].active = False
				    player_bullets[collision_count].active = False
				    expolde_sound.play()
				    player_score += 4750
				    enemy_killed += 1
				    create_particles(15, shooter_invaders[count].rect.left + 8, shooter_invaders[count].rect.top + 8, red_particle_image)

		# How nmuch the shooter_invaders take to shoot?
		enemy_fire_timer += 1
		if enemy_fire_timer > enemy_fire_max and game_over == False:
		    enemy_fire_timer = 0
		    for count in range(MAX_ENEMIES):
			if shooter_invaders[count].active == True and shooter_invaders[count].rect.top < SCREEN_HEIGHT - 50 and shooter_invaders[count].rect.top > 50:
			    shoot2_sound.play()
			    bullets = 0
			    for bullet_count in range(MAX_ENEMY_BULLETS):
				if enemy_bullets[bullet_count].active == False:
				    if random.randint(0, 10) > 4:
					enemy_bullets[bullet_count].active = True
					enemy_bullets[bullet_count].vector_x = 7
					enemy_bullets[bullet_count].vector_y = 0
					enemy_bullets[bullet_count].rect.top = shooter_invaders[count].rect.top + 8
					enemy_bullets[bullet_count].rect.left = shooter_invaders[count].rect.left + 12
					break
				    else:
					enemy_bullets[bullet_count].active = True
					enemy_bullets[bullet_count].vector_x = 0
					enemy_bullets[bullet_count].vector_y = 7
					enemy_bullets[bullet_count].rect.top = shooter_invaders[count].rect.top + 16
					enemy_bullets[bullet_count].rect.left = shooter_invaders[count].rect.left + 8
					break

		# Update the ufos (move and draw)..
		for count in range(MAX_UFOS):
		    if ufos[count].active:
			ufos[count].update()
			screen.blit(ufos[count].image, ufos[count].rect, (32 * ufos[count].anim_frame, 0, 32, 32))
			for collision_count in range(PLAYER_BULLETS):
                            if player_bullets[collision_count].rect.colliderect((ufos[count].rect.left, ufos[count].rect.top, 32, 32)):        
				ufos[count].active = False
				create_particles
				player_bullets[collision_count].active = False
				expolde_sound.play()
				player_score += 3250
                                create_particles(15, ufos[count].rect.left + 8, ufos[count].rect.top + 8, gray_particle_image)

		# Update the transient invaders (move and draw)..
		for count in range(MAX_ENEMIES):
		    if transient_invaders[count].active:
			transient_invaders[count].update()
			screen.blit(transient_invaders[count].image, transient_invaders[count].rect, (32* transient_invaders[count].anim_frame, 0, 32, 32))
			for collision_count in range(PLAYER_BULLETS):
			    if player_bullets[collision_count].active == True:
				if player_bullets[collision_count].rect.colliderect(transient_invaders[count], player_bullets[count]):
				    transient_invaders[count].active = False
				    player_bullets[collision_count].active = False
				    expolde_sound.play()
				    player_score += 2500
				    enemy_killed += 1
				    create_particles(15, transient_invaders[count].rect.left + 8, transient_invaders[count].top + 8, blue_particle_image)

	    # Check for player and invaders collisions..
            if player_flash_timer < 1 and game_over == False:
                player_hit = False
                for collision_count in range(MAX_ENEMIES):
                    # Have any invaders collided with player?
                    if invaders[collision_count].active == True:
                        if player_side.rect.colliderect((invaders[collision_count].rect.left + 5, invaders[collision_count].rect.top + 5, 24, 24)):        
                            invaders[collision_count].active = False
                            create_particles(15, invaders[collision_count].rect.left + 8, invaders[collision_count].rect.top + 8, green_particle_image)
                            player_hit = True
                        if player_bottom.rect.colliderect((invaders[collision_count].rect.left + 5, invaders[collision_count].rect.top + 5, 24, 24)):        
                            invaders[collision_count].active = False
                            create_particles(15, invaders[collision_count].rect.left + 8, invaders[collision_count].rect.top + 8, green_particle_image)
                            player_hit = True
                            
                    # Have any transient_invaders collided with player?
                    if shooter_invaders[collision_count].active == True:
                        if player_side.rect.colliderect((shooter_invaders[collision_count].rect.left + 5, shooter_invaders[collision_count].rect.top + 5, 24, 24)):        
                            shooter_invaders[collision_count].active = False
                            create_particles(15, shooter_invaders[collision_count].rect.left + 8, shooter_invaders[collision_count].rect.top + 8, red_particle_image)
                            player_hit = True
                        if player_bottom.rect.colliderect((shooter_invaders[collision_count].rect.left + 5, shooter_invaders[collision_count].rect.top + 5, 24, 24)):        
                            shooter_invaders[collision_count].active = False
                            create_particles(15, shooter_invaders[collision_count].rect.left + 8, shooter_invaders[collision_count].rect.top + 8, red_particle_image)
                            player_hit = True
                            
                    # Have any transient_invaders collided with player?
                    if transient_invaders[collision_count].active == True:
                        if player_side.rect.colliderect((transient_invaders[collision_count].rect.left + 5, transient_invaders[collision_count].rect.top + 5, 24, 24)):        
                            transient_invaders[collision_count].active = False                    
                            create_particles(15, transient_invaders[collision_count].rect.left + 8, transient_invaders[collision_count].rect.top + 8, blue_particle_image)
                            player_hit = True
                        if player_bottom.rect.colliderect((transient_invaders[collision_count].rect.left + 5, transient_invaders[collision_count].rect.top + 5, 24, 24)):        
                            transient_invaders[collision_count].active = False
                            create_particles(15, transient_invaders[collision_count].rect.left + 8, transient_invaders[collision_count].rect.top + 8, blue_particle_image)
                            player_hit = True

                # Have any ufos collided with player?
                for collision_count in range (MAX_UFOS):
                    if ufos[collision_count].active == True:
                        if player_side.rect.colliderect((ufos[collision_count].rect.left + 5, ufos[collision_count].rect.top + 5, 24, 24)):        
                            ufos[collision_count].active = 0
                            create_particles(15, ufos[collision_count].rect.left + 8, ufos[collision_count].rect.top + 8, gray_particle_image)
                            player_hit = True
                        if player_bottom.rect.colliderect((ufos[collision_count].rect.left + 5, ufos[collision_count].rect.top + 5, 24, 24)):        
                            ufos[collision_count].active = 0
                            create_particles(15, ufos[collision_count].rect.left + 8, ufos[collision_count].rect.top + 8, gray_particle_image)
                            player_hit = True

                # Have any enemy bullets collided with player?
                for collision_count in range (MAX_ENEMY_BULLETS):
                    if player_bullets[collision_count].active == True:
                        if player_side.rect.colliderect((player_bullets[collision_count].rect.left, player_bullets[collision_count].rect.top, 8, 8)):        
                            player_bullets[collision_count].active = 0
                            player_hit = True
                        if player_bottom.rect.colliderect((player_bullets[collision_count].rect.left, player_bullets[collision_count].rect.top, 8, 8)):        
                            player_bullets[collision_count].active = 0
                            player_hit = True

                # Has player been hit by anything nasty?
                if player_hit == True and game_over == False:          
                    player_shield -= 1
                    create_particles(5, 85 + ((player_shield) * 11), 32, red_particle_image)                    
                    player_flash_timer = 50
                    damage_sound.play()                
                        
                    if player_shield == 0:
                        player_dead_sound.play()
                        create_particles(20, player_bottom.rect.left + 8, player_bottom.rect.top + 8, red_particle_image)
                        create_particles(20, player_bottom.rect.left + 8, player_bottom.rect.top + 8, yellow_particle_image)
                        create_particles(20, player_side.rect.left + 8, player_side.rect.top + 8, red_particle_image)
                        create_particles(20, player_side.rect.left + 8, player_side.rect.top + 8, yellow_particle_image)
                        game_over = True

            # Display hud stuff
            screen.blit(game_font.render("Score: " + str(player_score), 0, ((255, 206, 0))), (10, 10))
            screen.blit(game_font.render("High Score: " + str(high_score), 0, ((255, 206, 0))), (460, 10))

	    #NOTE: BOOKMARK HERE!
            # Beaten high score?
            if player_score > high_score:
                high_score = player_score
                # Make a little fuss of the player :)
                if BEATEN_HIGH_SCORE == False:
                    BEATEN_HIGH_SCORE = True
                    for count in range(5):
                        create_particles(5, 460 + (count * 15), 15, yellow_particle_image)                        
                
            if wave_break > 0:
                wave_break -= 1
                if game_over == False:
                    screen.blit(game_font_large.render("Wave " + str(game_wave) + " of 9", 0, ((255, 206, 0))), (240, SCREEN_HEIGHT / 2 - 36))        

	    for count in range(player_shield):
		screen.blit(game_font.render("Shields:", 0, ((255, 206, 0))), (10, 30))
		screen.blit(player_health_image, (85 + (count * 11), 32))

            if game_over == True:
                # Loss or victory?
                if game_victory == False:
                    screen.blit(game_font_large.render("GAME OVER", 0, ((176, 0, 0))), (260, SCREEN_HEIGHT / 2 - 36))
                else:
                    screen.blit(game_font_large.render("YOU ARE AWESOME!!!", 0, ((255, 206, 0))), (160, SCREEN_HEIGHT / 2 - 36))
                    game_victory_particle_timer += 1
                    if game_victory_particle_timer > 10:
                        create_particles(30, random.randint(160, 450), random.randint(160, 300), red_particle_image)                       
                        
                game_over_timer -= 1
                if game_over_timer == 0:
                    game_mode = TITLE_SCREEN_MODE
                    
            # Time for a new wave? Only start new wave display when all enemies are dead
            enemies_onscreen = False
            for count in range(MAX_ENEMIES):
                if invaders[count].active == True:
                    enemies_onscreen = True
                    break
                if shooter_invaders[count].active == True:
                    enemies_onscreen = True
                    break
                if transient_invaders[count].active == True:
                    enemies_onscreen = True
                    break
                
            for count in range(MAX_UFOS):
                if ufos[count].active == True:
                    enemies_onscreen = True

            if enemy_killed > wave_target_kills and enemies_onscreen == False and game_over == False:
                wave_break = 300
                wave_target_kills += 10
                game_wave += 1
                if game_wave == 10:
                    game_over = True
                    game_victory = True
                    game_over_timer = 700
                    win_sound.play()
                    
                enemy_killed = 0
               
                # Make the next round a bit harder :)
                if attack_max > 30:
                    attack_max -= 10
                if ufo_attack_max > 0:
                    ufo_attack_max -= 50
                if game_wave > 6:
                    player_fire_rate = 10
                wave_sound.play()

        pygame.display.flip()

        clock.tick(FPS)

		#    # Game Hack..
                #    if event.key == pygame.K_t:
		#	player_flash_on = True
		#	player_flash_timer = 50000

    pygame.quit()
#<<<><><><><><><><><><><><><><><><><><><><>>>>#
