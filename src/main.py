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

from players import Players
from enemy import enemy
from pygame.locals import *

def main():

    # Game Constants..
    SCREEN_HEIGHT = 800
    SCREEN_WIDTH = 600
    HIGHST_SCORE = 60000
    BEATEN_HIGH_SCORE = False

    FPS = 60

    NUMBER_OF_LIVES = 6
    MAX_ENEMIES = 7
    MAX_PLAYER_BULLETS = 3
    MAX_ENEMY_BULLETS = 3
    MAX_UFOS = 4

    # Counters..
    numberof_hits = 0
    numberof_kills = 0
    enemy_killed = 0

    # Game control stuff..
    GAME_MODE = 1
    TITLE_SCREEN_MODE = 1
    GAME_LOOP_MODE = 1

    title_menu_choice = 0
    TITLE_LIT_MESSAGE = True

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
    for count in range (MAX_PLAYER_BULLETS):
	player_bullet[count].append(projectile(SCREEN_WIDTH, SCREEN_HEIGHT, player_bullet_image)

    # Enemy bullets..
    enemy_bullets = []
    for count in range (MAX_ENEMY_BULLETS):
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

	    #***********************#
	    #****||TITLE SCREEN||***#
	    #***********************#
	    
	    # Render the game title..
	    screen.blit(game_font.render('Squadron', True, (255, 0, 0), (230, 100)))

	    title_lit_message_timer += 1
	    if title_lit_message_timer > 30:
	    	title_lit_message_timer = 0
		if TITLE_LIT_MESSAGE == True:
		    TITLE_LIT_MESSAGE = False
		else:
		    TITLE_LIT_MESSAGE = True

	    if TITLE_LIT_MESSAGE == True:
		screen.blit(game_font.render('Insert Coin'), True, (255, 0, 0), (280, 380))

	    if title_menu_choice == 0:
		screen.blit(game_font.render('Start'), True, (255, 0, 0), (300, 255))
	    else:
		screen.blit(game_font.render('Start'), True, (255, 255, 255), (300, 255))

	    if TITLE_LIT_MESSAGE == 1:
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
		    GAME_LOOP_MODE = True
		    # Start the game


    	# Game Events...
	for event in pygame.events.get():
	    if event.type == QUIT:
		main_loop = False

		if event.type == KEYDOWN:
		    if event.key == pygame.K_UP:
			side_player.update()
		    elif event.key == pygame.K_DOWN:
			side_player.update()
		    elif event.key == pygame.K_LEFT:
			bottom_player.update()
		    elif event.key == pygame.K_RIGHT:
			bottom_player.update()
		    elif event.key == pygame.K_x:
			player_bullet.shoot(side=True)
		    elif event.key == pygame.K_z:
			player_bullet.shoot(bottom=True)
		    elif event.key == pygame.K_ESCAPE:
			game_menu = True
#		if event.type == K_UP:
#			if event.key == K_DOWN:
#			elif event.key == K_LEFT:
#			elif event.key == K_x:
#			elif event.key == K_z:
#			elif event.key == K_ESCAPE:
#<<<><><><><><><><><><><><><><><><><><><><>>>>#
