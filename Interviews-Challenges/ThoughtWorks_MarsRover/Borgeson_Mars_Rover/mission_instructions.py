#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mars_rover import *

if __name__ == '__main__':
	mission_instructions = open('mission_instructions.txt', 'r')

	#Get borders of plateau, and initializes
	borders = mission_instructions.readline().split()
	x, y = map(int, borders)
	plateau = Plateau(x,y)
	rover_count = 0
	#Go through instructions
	for instructions in mission_instructions:
		#Initialize rover direction and location
		x, y, direction = instructions.split()
		rover = Rover(int(x), int(y), getattr(Direction, direction), plateau)
		rover_count+=1
		#Get line of commands
		commands = mission_instructions.readline().strip()
		for command in commands:
			#Go through commands and find mapped function, execute
			move = getattr(Movements, command, None)
			rover.exe(move)

		#Print end result of rover commands
		print("Rover #{0} final position : {1}, {2} {3}".format(rover_count,rover.coordinates()[0],
			rover.coordinates()[1] , str(rover.direction)[-1]))