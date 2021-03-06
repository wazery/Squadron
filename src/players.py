# file: players.py	--> The players class
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

import loader
import pygame
from pygame.locals import *

class Players(pygame.sprite.Sprite):
	"""This class is for the game players"""
    def init(slef, screen_width, screen_height, bottom=False, side= False):
	pygame.sprite.Sprite.__init__(self) #call sprite initializer
	self.screen_width = screen_width
	self.screen_height = screen_height

	if bottom is True:
	    self.bottom = True 
	    self.image, self.rect = loader.load_iamge('player_bottom.png', -1)
	    self.rect = self.image.get_rect(topleft = (start_x, start_y))

	if side is True:
	    self.side = True
	    self.image, self.rect = loader.load_iamge('player_side.png', -1)
	    self.rect = self.image.get_rect(topleft = (start_x, start_y))

    def update(self):
	#Get the current keyboard pressed button (state)
        keystate = pygame.key.get_pressed() 

	if self.bottom is True: #If player is bottom corner player, and it reaches te lower bound, reset the location
	    if slef.rect.left < 0: #Check if the player is out of boundary
		self.rect.left = 0
	    elif slef.rect.right > 800:
		self.rect.right = 800

	    if keystate == [pygame.K_LEFT]:
		self.rect.move_ip(-7,0)
	    if keystate == [pygame.K_RIGHT]:
		self.rect.move_ip(7,0)

	if self.side is True:
	    if slef.rect.bottom < 0:
		self.rect.bottom = 0
	    elif slef.rect.top > 600:
		self.rect.top = 600

	    if keystate == [pygame.K_UP]:
		self.rect.move_ip(0,-7)
	    if keystate == [pygame.K_DOWN]:
		self.rect.move_ip(7,0)
	
    screen_rect = Rect(0, 0, self.screen_width, self.screen_height)
    self.rect.clamp_ip(SCREENRECT)
