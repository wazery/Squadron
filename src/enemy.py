# file: enemy.py	--> The enemy module
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

import pygame
from pygame.locals import *

class Enemy(pygame.sprite.Sprite):
    
    def init(self, screen_width, screen_width, sprite_image):
	pygame.sprite.Sprite.__init__(self)
	self.screen_width = screen_width
	self.screen_height screen_height
	self.image = sprite_image
	self.rect = self.image.get_rect(topleft= (0, 0))
	self.image.set_colorkey((255,0,255))

	self.active = False
	self.vector_x = 0
	self.vector_y = 0

	self.anim_frame = 0
	self.anim_delay = 0
	self.anim_max_frame = 0
	self.movement_type = 0
	self.movement_timer = 0

    def update(self):
	if (self.active):
	    # Move the enemy to its dest..
	    self.rect.move_ip(self.vector_x, self.vector_y)

	    # Do the enemy animation..
	    self.anim_delay += 1
	    if self.anim_delay > 6:
		self.anim_frame += 1
		self.anim_delay = 0
		if self.anim_frame > self.anim_max_frame:
		    self.anim_frame = 0
	    
	    # Now handle the movement_type 
	    if self.movement_type == 1:
		self.movement_timer += 1
		# What is the time to change enemy direction
		if self.movement_timer > 35:
		    self.movement_timer = 0
		    # In which direction the enemy will go
		    if self.rect.left < (self.screen_width / 4):
			self.vector_x = random.randint(1, 2)
		    elif self.rect.left > (self.screen_width - (self.screen_width / 4)):
			self.vector_x = random.randint(1, 2)
			else:
			    self.vector_x = random.randint(0, 1) - random.randint(1, 2)

	    if self.movement_type == 1:
		self.movement_timer += 1
		# What is the time to change enemy direction
		if self.movement_timer > 35:
		    self.movement_timer = 0
		    # In which direction the enemy will go
		    if self.rect.top < (self.screen_height / 4):
			self.vector_y = random.randint(1, 2)
		    elif self.rect.top > (self.screen_height - (self.screen_height / 4)):
			self.vector_y = random.randint(1, 2)
			else:
			    self.vector_x = random.randint(0, 1) - random.randint(1, 2)

	    # Is enemy go out of the screen?
	    if self.vector_x < 0 and self.rect.left < -50:
		self.active = False

	    if self.vector_x > 0 and self.rect.left > self.screen_width + 50:
		self.active = False

	    if self.vector_y < 0 and self.rect.top < -50:
		self.active = False

	    if self.vector_y > 0 and self.rect.left > self.screen_height + 50:
		self.active = False
