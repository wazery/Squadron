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

import random
import pygame
import loader

from projectile import Projectile
from players import Players
from enemy import Enemy
from particle import Particle
from pygame.locals import *

def main():

    # Game Constants..
    SCREEN_HEIGHT = 800
    SCREEN_WIDTH = 600

    HIGHST_SCORE = 60000
    BEATEN_HIGH_SCORE = False

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
    numberof_hits = 0
    numberof_kills = 0
    enemy_killed = 0
    player_score = 0
    player_lives = 7
    player_flash_timer = 0
    player_flash_on = False

    # Game control stuff..
    game_mode = 1
    title_menu_choice = 0
    title_lit_message = True

    # Init the game and creating the display surface..
    pygame.init()
    random.seed()
    screen = pygame.display.set_mode(SCREEN_HEIGHT, SCREEN_WIDTH)
    SCREEN_WIDTH, SCREEN_HEIGHT = sceen.get_size()
    pygame.display.set_caption('Squadron: Yet Another Arcade Game!')
    pygame.mouse.set_visible(False)

    # Creating a Font..
    pygame.font.init()
    game_font = pygame.font.Font(os.path.join('data', '04b_25__.ttf'), 18)

    # Loading game gfx..
    backgorund_image, background_rect = loader.load_image('Main_Hud.jpeg') #TODO creating the Main_Hud image!
    player_bullet_image = loader.load_image('bullet1.png')
    enemy_bullet_image = loader.load_image('bullet2.png')
    invader_image = loader.load_image('invader.png')
    shooter_image = loader.load_image('shooter_enemy.png')
    transient_image = loader.load_image('Transient.png')
    ufo_image = loader.load_image('ufo.png')

     # Loading all game sounds..
    damage_sound = loader.load_sound(damage)
    exit_sound = loader.load_sound(exit)
    expolde_sound = loader.load_sound(explode)
    lazer_sound = loader.load_sound(lazer)
    menu_mov_sound = loader.load_sound(menu_move)
    menu_select_sound = loader.load_sound(menu_select)
    new_wave_sound = loader.load_sound(newwave)
    player_dead_sound = loader.load_sound(player_dead)
    shoot2_sound = loader.load_sound(shoot2)
    start_sound = loader.load_sound(start)
    ufo_sound = loader.load_sound(ufo)
    win_sound = loader.load_sound(win)

    # Create some particle images..
    red_particle_image = pygame.Surface(8,8)
    red_particle_image.fill(176,0,0)

    green_particle_image = pygame.Surface(8,8)
    green_particle_image.fill(31,92,4)

    blue_particle_image = pygame.Surface(8,8)
    blue_particle_image.fill(46, 102, 187)

    yellow_particle_image = pygame.Surface(8,8)
    yellow_particle_image.fill(255, 206, 0)

    gray_particle_image = pygame.Surface(8,8)
    gray_particle_image.fill(88, 88, 88)
    
    # Player bullets..
    player_bullets = []
    for count in range(MAX_PLAYER_BULLETS):
	player_bullets[count].append(projectile(SCREEN_WIDTH, SCREEN_HEIGHT, player_bullet_image)
	player_bullets[count].active = False

    # Enemy bullets..
    enemy_bullets = []
    for count in range(MAX_ENEMY_BULLETS):
	enemy_bullets[count].append(projectile(SCREEN_WIDTH, SCREEN_HEIGHT, enemy_bullet_image))
	enemy_bullets[count].active = False

    # Create the game players..
    bottom_player = Players(SCREEN_WIDTH, SCREEN_HEIGHT, bottom=True)
    side_player = Players(SCREEN_WIDTH, SCREEN_HEIGHT, side=True)

    # Prepare enemies..
   invaders = []
   shooter_invaders = []
   transient_invaders = []

   for count in range (MAX_ENEMIES):
   	# invaders 
   	invaders[count].append(enemy(SCREEN_WIDTH, SCREEN_HEIGHT, invader_image))
   	invaders[count].rect.top = 0
      	invaders[count].rect.left = 0
   	invaders[count].rect.vector_x = 0
   	invaders[count].rect.vector_y = 0
   	invaders[count].rect.vector_y = 0
   	invaders[count].rect.active = False
   	invaders[count].rect.anim_max_frame = 3
   	invaders[count].rect.movement_type = 0

   	# shooter invaders 
   	shooter_invaders[count].append(enemy(SCREEN_WIDTH, SCREEN_HEIGHT, shooter_image))
   	shooter_invaders[count].rect.top = 0
   	shooter_invaders[count].rect.left = 0
   	shooter_invaders[count].rect.vector_x = 0
   	shooter_invaders[count].rect.vector_y = 0
   	shooter_invaders[count].rect.vector_y = 0
   	shooter_invaders[count].rect.active = False
   	shooter_invaders[count].rect.anim_max_frame = 3
   	shooter_invaders[count].rect.movement_type = 0

   	# transient invaders 
   	transient_invaders[count].append(enemy(SCREEN_WIDTH, SCREEN_HEIGHT, transient_image))
   	transient_invaders[count].rect.top = 0
   	transient_invaders[count].rect.left = 0
   	transient_invaders[count].rect.vector_x = 0
   	transient_invaders[count].rect.vector_y = 0
   	transient_invaders[count].rect.vector_y = 0
   	transient_invaders[count].rect.active = False
   	transient_invaders[count].rect.anim_max_frame = 3
   	transient_invaders[count].rect.movement_type = 0
    
    ufos[]
    for count in range MAX_UFOS:
	ufos[count].append(enemy(SCREEN_WIDTH, SCREEN_HEIGHT, ufo_image))
	ufos[count].anim_max_frame = 9

    particles[]
    for count in range MAX_PARTICLES:
	particles[count].append(particle(SCREEN_WIDTH, SCREEN_HEIGHT, ))
   
#<<<><><><><><>||MAIN LOOP||<><><><><><><><>>>#
#<<<><><><><><><><><><><><><><><><><><><><>>>>#

    main_loop = True

    while main_loop is True:

	# Check the game mode if TITLE_SCREEN_MODE
	if GAME_MODE == TITLE_SCREEN_MODE:

	    #-----------------------#
	    #----||TITLE SCREEN||---#
	    #-----------------------#
	    
	    # Render the game title..
	    screen.blit(game_font.render('Squadron', True, (255, 0, 0), (230, 100)))

	    title_lit_message_timer += 1
	    if title_lit_message_timer > 30:
	    	title_lit_message_timer = 0
		if title_lit_message == True:
		    title_lit_message = False
		else:
		    title_lit_message = True

	    if title_lit_message == True:
		screen.blit(game_font.render('Insert Coin'), True, (255, 0, 0), (280, 380))

	    if title_menu_choice == 0:
		screen.blit(game_font.render('Start'), True, (255, 0, 0), (300, 255))
	    else:
		screen.blit(game_font.render('Start'), True, (255, 255, 255), (300, 255))

	    if title_lit_message == 1:
		screen.blit(game_font.render('Exit'), True, (255, 0, 0))
	    else:
		screen.blit(game_font.render('Exit'), True, (255, 255, 255))

	    screen.blit(game_font.render(('Z and X to fire, cursor keys to move the battles'), True, (0, 255, 0), (120, 450)
	
	# Screen Events...
	for event in pygame.events.get():
	    if event.type == QUIT:
		main_loop = False

		if event.type == KEYDOWN:
		    if event.key == pygame.K_UP:
			title_menu_choice += 1
		    elif event.key == pygame.K_DOWN:
			title_menu_choice -= 1
		    elif event.key == pygame.K_ESCAPE:
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
		    title_lit_message_timer = 0
		    title_lit_message = False
		    title_menu_choice = 0
		    player_score = 0
		    player_lives = 7
		    player_flash_timer = 0
		    player_flash_on = False

		    # Deactivate all enemies, particles, bullets
		    for count in range(MAX_ENEMIES):
			invaders[count].active = False
			shooter_enemy[count].active = False
			transient_invaders[count].active = False

		    for count in range(MAX_PARTICLES):
			particles[count].active = False

		    for count in range(MAX_PLAYER_BULLETS):
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
	for event in pygame.events.get():
	    if event.type == QUIT:
		main_loop = False

		if event.type == KEYDOWN:
		    elif event.key == pygame.K_x: and player_fire_delay_left > player_fire_delay_time and game_over == False:
			for count in range(MAX_PLAYER_BULLETS):
			    player_bullets[count].active = True
			    player_bullets[count].vector_x = -9
			    player_bullets[count].vector_y = 0
			    player_bullets[count].
			    lazer_sound.play()
			    break

		    elif event.key == pygame.K_z and player_fire_delay_left > player_fire_delay_time and game_over == False:
			for count in range(MAX_PLAYER_BULLETS):
			    player_bullets[count].active = True
			    player_bullets[count].vector_x = 0
			    player_bullets[count].vector_y = -9
			    player_bullets[count].
			    lazer_sound.play()
			    break

		    elif event.key == pygame.K_ESCAPE:
			game_mode = TITLE_SCREEN_MODE # Switch back to the title screen

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
				    invaders[count].vector_x = 0
				    invaders[count].vector_y = max_enemy_speed
				    invaders[count].active = True
				    break
		    elif enemy_type == 1:
			for count in range(MAX_ENEMIES):
			    if shooter_invaders[count].active = False:
				if direction == 0: # if enemies come from left
				    shooter_invaders[count].rect.left = -32 # 32 is the icon size
				    shooter_invaders[count].rect.top = random.randint(0, (SCREEN_HEIGHT - 64) / 32) * 32
				    shooter_invaders[count].vector_x = max_enemy_speed
				    shooter_invaders[count].vector_y = 0
				    shooter_invaders[count].active = True
				    shooter_invaders[count].movement_type = 2
				    break
				else: # if enemies come from top
				    shooter_enemy[count].rect.left = random.randint(0, (SCREEN_WIDTH - 64) / 32) * 32
				    shooter_enemy[count].rect.top = -32
				    shooter_enemy[count].vector_x = 0
				    shooter_enemy[count].vector_y = max_enemy_speed
				    shooter_enemy[count].movement_type = 1
				    shooter_enemy[count].movement_type = 1
				    break
		    elif enemy_type == 2:
			for count in range(MAX_ENEMIES):
			    if shooter_invaders[count].active = False:
				if direction == 0: # if enemies come from left
				    transient_invaders[count].rect.left = -32
				    transient_invaders[count].rect.top = random.randint(0, (SCREEN_HEIGHT - 64) / 32) * 32
				    transient_invaders[count].vector_x = max_enemy_speed
				    transient_invaders[count].vector_y = 0
				    transient_invaders[count].active = True
				    break
				else: # if enemies come from top
				    transient_invaders[count].rect.left = random.randint(0, SCREEN_WIDTH - 64) / 32) * 32
				    transient_invaders[count].rect.top = -32
				    transient_invaders[count].vector_x = max_enemy_speed
				    transient_invaders[count].vector_y = 0
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
				ufos[count].vector_x = max_ufo_speed
				ufos[count].vector_y = 0
				ufos[count].active = True
			else: # Attacking the bottom player
			    if random.randint(0, 10) > 4:
				ufos[count].rect.left = SCREEN_WIDTH+ 32
				ufos[count].rect.top = SCREEN_HEIGHT - 32
				ufos[count].rect.vector_x = max_enemy_speed
				ufos[count].rect.vector_y = 0
				ufos[count].rect.active = True

		# Render the particles..
		for count in range(MAX_PARTICLES):
		    if particle[count].active == True:
			particle[count].update()
			screen.blit(particle[count].image, particle[count].rect)
		
		# Update the players due to their key events..
		player_bottom.update()
		player_side.update() 
		
		# If player recovers from damage..
		if player_flash_timer > 0:
		    player_flash_on -= 1
		    if player_flash_on = True:
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

		# Increase the delay for the players fire
		player_fire_delay_left += 1
		player_fire_delay_right += 1

		# Update the invaders (move and draw)
		for count in range(MAX_ENEMIES):
		    if invaders[count].active:
			invaders[count].update()
			screen.blit(invaders[count].image, invaders[count].rect, (32 * invaders[count].anim_frame, 0, 32, 32))
			# Check the invader collision with any player_bullets
			for collision_count in range(PLAYER_BULLETS):
			    if player_bullets[collision_count].active:
				if player_bullets[collision_count].rect.colliderect(invaders[count].rect, player_bullets[count].rect)
				    invaders[count].active = False
				    create_particles(15, invaders[count].rect.left + 8, invaders[count].rect.top + 8, green_particle_image
				    player_bullets[collision_count].active = False
				    enemy_killed += 1
				    expolde_sound.play()
				    player_score += 2000

		# Update the red invaders (move and draw)
		for count in range(MAX_ENEMIES):
		    if shooter_invaders[count].active:
			shooter_invaders[count].update()
			screen.blit(shooter_invaders[count].image, shooter_invaders[count].rect, player_bullets[count].rect)
			for collision_count in range(player_bullets):
			    if player_bullets[collision_count].rect.colliderect(shooter_invaders[count].rect, player_bullets[count]):
				shooter_invaders[count].active = False
				create_particles(15, shooter_invaders[count].rect.left + 8, shooter_invaders[count].rect.top + 8, red_particle_image)
				player_bullets[collision_count].active = False
				expolde_sound.play()
				player_score += 4750
				enemy_killed -= 1

		# Update the transient invaders (move and draw)
		for count in range(MAX_ENEMIES):
		    if transient_invaders[count].active:
			for count in range(player_bullets):
			    if player_bullets[collision_count].rect.colliderect(transient_invaders[count], player_bullets[count]):
				transient_invaders[count].active = False
				create_particles(15, transient_invaders[count].rect.left + 8, transient_invaders[count].top + 8)
				player_bullets[collision_count].active = False
				expolde_sound.play()
				player_score += 2500
				enemy_killed += 1

		# Update the ufos (move and draw)
		for count in range(MAX_UFOS):
		    if ufos[count].active:
			ufos[count].update()
			screen.blit(ufos[count].image, ufos[count].rect, (32 * ufos[count].anim_frame, 0, 32, 32))
			for count in range(player_bullets):
			    if player_bullets[collision_count].rect.colliderect(transient_invaders[count], player_bullets[count]):
				ufos[count].active = False
				create_particles(15, ufos[count].rect.left + 8, ufos[count].top + 8)
				player_bullets[collision_count].active = False
				expolde_sound.play()
				player_score += 3250
				enemy_killed += 1
		
		# How nmuch the shooter_invaders take to shoot?
		enemy_fire_timer += 1
		if enemy_fire_timer > enemy_fire_max and game_over == False:
		    enemy_fire_timer = 0
		    for count in range(MAX_ENEMIES):
			if shooter_enemy[count].active == True and shooter_enemy[count].rect.top < 
			    shoot2_sound.play()
			    bullets = 0
			    for bullet_count in range(MAX_ENEMY_BULLETS):
				if enemy_bullets[bullet_count]
				    bullets += 1

		#    # Game Hack..
                #    if event.key == pygame.K_t:
		#	player_flash_on = True
		#	player_flash_timer = 50000
    pygame.quit()
#<<<><><><><><><><><><><><><><><><><><><><>>>>#
