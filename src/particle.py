# file: particle.py	--> The particle module
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

class Particle(pygame.sprite.Sprite):
    
    def __init__(slef, screen_width, screen_height, sprite_image)
	self.screen_width = screen_width
	self.screen_height = screen_height
	self.image = sprite_image
	self.image.set_colorkey((255, 0, 255))
	self.rect = self.image.get_rect(topleft= (0, 0))
	self.active = False
	self.vector_x = 0
	self.vector_y = 0
	self.move_count = 0

    def update(self):
	if (self.active):
	    self.rect.move_ip(self.vector_x, self.vector_y)
	    self.move_count -= 1
	    if self.move_count == 0
		self.active = False

	if (self.rect.left < -12 or self.rect.top < -12 or slef.rect.left > self.screen_width + 12 or self.rect.top > self.screen_height + 12):
	    self.active = False
