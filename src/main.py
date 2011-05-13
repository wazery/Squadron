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

import random, os
import pygame

from players import Players
from pygame.locals import *

if __name__ == '__main__' : main()

def load_image(filename, colorkey=None):
	filename = os.path.join('data', filename)
	
	try:
		image = pygame.image.load(filename)
	except pygame.error, message:
		print 'Cannot load the image: ', filename
		raise SystemExit, message
	
	image = image.convert()

	if colorkey is not None:
		if colorkey is -1:
			colorkey = image.get_at((0,0))
		image.set_colorkey(colorkey, RLEACCEL)
	
	return image, image.get_rect()

def load_sound(name):
	class No_Sound:
		def play(self) : pass
	
	if not pygame.mixer or not pygame.mixer.get_init():
		return No_Sound()
	
	fullname = os.path.join('data', name)
	if os.path.exists(fullname) == False:
		sound = pygame.mixer.Sound(fullname)
	else:
		print 'File %s does not exist!', filename
		return No_Sound()
	
	return sound

def main():
	random.seed()
	pygame.init()

	#Creating the display surface..
	screen = pygame.display.set_mode(800,600)
	pygame.display.set_caption('Squadron: Yet Another Arcade Game!')
	pygame.mouse.set_visible(False)

	#Loading game images..
	backgorund_image, background_rect = load_image('Main_Hud.jpeg') #TODO creating the Main_Hud image!
	
	#Loading all game sounds..
	damage_sound = load_sound(damage)
	exit_sound = load_sound(exit)
	expolde_sound = load_sound(explode)
	lazer_sound = load_sound(lazer)
	menu_mov_sound = load_sound(menu_move)
	menu_select_sound = load_sound(menu_select)
	new_wave_sound = load_sound(newwave)
	player_dead_sound = load_sound(player_dead)
	shoot2_sound = load_sound(shoot2)
	start_sound = load_sound(start)
	ufo_sound = load_sound(ufo)
	win_sound = load_sound(win)


	#Counters..
	numberof_hits = 0
	numberof_kills = 0
	enemy_killed = 0
	
	#Create the game players..

