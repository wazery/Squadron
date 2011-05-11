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


	

