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

class Players:
	"""This class is for the game players"""
	def init(slef, down=False, side= False):
		pygame.spirite.Spirite.__init__(self) #call spirit initializer
		if down:
			self.image, self.rect = load_iamge('player_down.png', -1)
			self.rect.center = (400,577)
			self.x_velocity = 0
			self.y_velocity = 0
		if side:
			self.image, self.rect = load_iamge('player_side.png', -1)
			self.rect.center = (777,300)
			self.x_velocity = 0
			self.y_velocity = 0

	def update(self, down=False, side=False):
		self.rect.move_ip(self.x_velocity, slef.y_velocity)
		
		if down is True: #if player is down corner player, and it reaches te lower bound, reset the location
			if slef.rect.left < 0:
				self.rect.left = 0
			elif slef.rect.right > 800:
				self.rect.right = 800
				
		if side is True:
			if slef.rect.left < 0:
				self.rect.left = 0
			elif slef.rect.right > 600:
				self.rect.right = 600
