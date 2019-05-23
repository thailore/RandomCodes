#!/usr/bin/env python
# -*- coding: utf-8 -*-


from enum import Enum

all_rover_coordinates = []
'''all_rover_coordinates array holds current location of all rovers when they
are initialized. Coordinates of currently active rover are last element in array.

When changing coordinates, elements are popped and reset. 
Array allows for collision prevention
'''


class Direction(Enum):
	'''Enumeration for Directions
	'''
	N = 1
	E = 2
	S = 3
	W = 4

class Movements(Enum):
	'''Enumeration for Movements (instructions) to help with
	reading from instructions text and executing
	'''
	L = 0
	R = 1
	M = 2


class Plateau(object):

	def __init__(self, x, y):
		'''Initialize the Plateau
		'''
		self.plateau_x = x
		self.plateau_y = y


class Rover(object):

	def __init__(self, x, y, direction, plateau):
		'''Initialize Rover object
		'''
		#Don't initialize rover unless starting coordinates are within plateau borders
		if x not in range(plateau.plateau_x+1) or y not in range(plateau.plateau_y+1):
			raise ValueError("Please make sure rovers are initialized inside the plateau. Check starting coordinates")

		self.x = x
		self.y = y
		self.direction = direction
		self.plateau = plateau

		#Add rover to all rover coordinates
		all_rover_coordinates.append([self.x, self.y])

	def validate_rover_movement_on_plateau(self, x, y):
		'''Make sure rover does not move out of plateau

		In the case of an attempted movement out of plateau, will not move and instead turn right
		'''

		#check that desired coordinates are within Plateau borders
		if 0 <= x <= self.plateau.plateau_x and 0 <= y <= self.plateau.plateau_y: 
			return True
		else:
			print("Preventing rover from leaving plateau and progressing to {0},{1}....Turned Right".format(x, y))
			return False
		

	def validate_no_collision(self, x, y): 
		'''Make sure that movement does not result in collision with another rover
		'''
		c = [x,y] #Create coordinate set for desired movement

		#Check if new coords are already in all_rover_coordinates which signifies rover occupies desired position
		if c not in all_rover_coordinates:  
			all_rover_coordinates.pop() #Last element of the array is current position of current rover. Remove
			all_rover_coordinates.append(c) #Add new coordinates for current rover 
			return True
		else: #Coords already exist, meaning rover occupies position
			print("Preventing Collision at {0},{1}....Turned Right".format(x,y) )
			return False
	

	def coordinates(self):
		'''Returns coordinates of current rover
		'''
		return (self.x, self.y)


	def _R(self):
		'''Function to turn right
		'''
		direction_value = self.direction.value + 1 
		if direction_value > Direction.W.value:
			direction_value = Direction.N.value

		self.direction = Direction(direction_value)


	def _L(self):
		'''Function to turn left
		'''
		direction_value = self.direction.value - 1 

		if direction_value < Direction.N.value:
			direction_value = Direction.W.value

		self.direction = Direction(direction_value)


	def _M(self):
		'''Function to move forward one space
		'''

		'''Checks what direction rover is facing and simulates desired movement in correct x or y direction.
		If simulated movement is not allowed due to boundaries or collision, message is printed, rover is
		turned to the right, and continues to next instruction

		If allowed, executes movement
		'''
		if self.direction is Direction.N: 
			if self.validate_rover_movement_on_plateau(self.x, self.y + 1) and self.validate_no_collision(self.x, self.y+1):
				self.y += 1 #validated desired movement results in executed movement
			else:
				self._R() #Turn Right

		elif self.direction is Direction.E:
			if self.validate_rover_movement_on_plateau(self.x + 1, self.y) and self.validate_no_collision(self.x + 1, self.y):
				self.x += 1 #validated desired movement results in executed movement
			else:
				self._R() #Turn Right

		elif self.direction is Direction.S:
			if self.validate_rover_movement_on_plateau(self.x, self.y - 1) and self.validate_no_collision(self.x, self.y - 1):
				self.y -= 1 #validated desired movement results in executed movement
			else:
				self._R() #Turn Right

		elif self.direction is Direction.W:
			if self.validate_rover_movement_on_plateau(self.x - 1, self.y) and self.validate_no_collision(self.x - 1, self.y):
				self.x -= 1 #validated desired movement results in executed movement
			else:
				self._R() #Turn Right

	def exe(self, command):
		if not isinstance(command, Movements):
			raise ValueError("Nonexistent command entered....Please check mission instructions has only L,R, or M")

		if command is Movements.L: 
			self._L() 
		if command is Movements.R:
			self._R()
		if command is Movements.M:
			self._M() 








