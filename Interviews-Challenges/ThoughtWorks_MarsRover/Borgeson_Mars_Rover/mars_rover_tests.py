#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Tests for Mars Rover Program
"""

from mars_rover import *
import unittest, logging, sys


class TestRover(unittest.TestCase):

	def setUp(self):
		'''Instantiate Plateau
		'''
		self.plateau = Plateau(5,5)
		'''Set Rover to starting location facing North
		'''
		self.rover = Rover(1, 2, Direction.N, self.plateau) 


	def tearDown(self):
		'''Reset array of all rover coordinates after each test
		'''
		del all_rover_coordinates [:] 


	def test_rover_in_plateau(self):
		'''Test that rover instance is validated in plateau
		'''
		with self.assertRaises(ValueError):
			rover = Rover(6,5, Direction.N, self.plateau)


	def test_turn_left(self):
		'''Test turn left command 
		- expected to change direction of rover by 90 degrees
		'''

		'''Turn once - North to West
		'''
		self.rover._L()
		self.assertEqual(self.rover.direction, Direction.W)

		'''Turn once - West to South
		'''
		self.rover._L()
		self.assertEqual(self.rover.direction, Direction.S)

		'''Turn once - South to East
		'''
		self.rover._L()
		self.assertEqual(self.rover.direction, Direction.E)

		'''Turn once - East to North
		'''
		self.rover._L()
		self.assertEqual(self.rover.direction, Direction.N)


	def test_turn_right(self):
		'''Test turn right command
		- expected to change direction of rover by 90 degrees
		'''

		'''Turn once - North to East
		'''
		self.rover._R()
		self.assertEqual(self.rover.direction, Direction.E)

		'''Turn once - East to South
		'''
		self.rover._R()
		self.assertEqual(self.rover.direction, Direction.S)

		'''Turn once - South to West
		'''
		self.rover._R()
		self.assertEqual(self.rover.direction, Direction.W)

		'''Turn once - West to North
		'''
		self.rover._R()
		self.assertEqual(self.rover.direction, Direction.N)


	def test_move_forward(self):
		'''Test move command
		- expected to move rover forward one grid space in the direction it's facing
		Rover instantiated at coordinates 1,2, facing North
		'''

		'''Move forward one space north, Y value should increase
		'''
		self.rover._M()
		self.assertEqual(self.rover.coordinates(), (1,3))

		'''Turn East, move forward one space, X value should increase
		'''
		self.rover._R()
		self.rover._M()
		self.assertEqual(self.rover.coordinates(), (2,3))

		'''Turn South, move forward one space, Y value should decrease
		'''
		self.rover._R()
		self.rover._M()
		self.assertEqual(self.rover.coordinates(), (2,2))

		'''Turn West, move forward one space, X value should decrease
		'''
		self.rover._R()
		self.rover._M()
		self.assertEqual(self.rover.coordinates(), (1,2))

		'''Turn North, move forward two spaces, Y value increase by 2
		'''
		self.rover._R()
		self.rover._M()
		self.rover._M()
		self.assertEqual(self.rover.coordinates(), (1,4))


	def test_cant_go_past_borders(self):
		'''Test Rover ability to breach borders 
		'''

		'''Set rover to top right corner of plateau facing north
		and try to move forward one

		Expect no movement, followed by a right turn to stay in borders
		'''
		rover = Rover(5, 5, Direction.N, self.plateau)

		rover._M()
		self.assertEqual(rover.coordinates(), (5,5)) #No forward movment
		self.assertEqual(rover.direction, Direction.E) #Right turn


		'''Now facing East at top right

		Expect no movement, followed by another right turn to stay in borders
		'''
		rover._M()
		self.assertEqual(rover.coordinates(), (5,5)) #No forward movement
		self.assertEqual(rover.direction, Direction.S) #Right turn


	def test_prevent_colliding_rovers(self):
		'''Test rover traveling to space occupied by another rover
		'''

		'''Set rover to one location, set second rover next to it and move
		to space occupied by first rover

		Expect no movement, followed by a right turn to avoid
		'''

		rover1 = Rover(3,4, Direction.N, self.plateau)
		rover2 = Rover(4,4, Direction.W, self.plateau)

		rover2._M()
		self.assertEqual(rover2.coordinates(), (4,4)) #Assert rover2 hasnt moved
		self.assertEqual(rover2.direction, Direction.N) #Assert rover2 has turned


	def test_false_command_entered(self):
		'''Test entry of false command
		'''
		with self.assertRaises(ValueError):
			self.rover.exe('U')

		with self.assertRaises(ValueError):
			self.rover.exe('r')

			


logging.basicConfig( stream=sys.stderr )	

#Was using logger to help debug the tests
#logging.getLogger( "TestRover.test_turn_left" ).setLevel( logging.DEBUG )
#logging.getLogger( "TestRover.test_turn_right" ).setLevel( logging.DEBUG )
#logging.getLogger( "TestRover.test_prevent_colliding_rovers" ).setLevel( logging.DEBUG )
#logging.getLogger( "TestRover.test_cant_go_past_borders" ).setLevel( logging.DEBUG )
#logging.getLogger( "TestRover.test_move_forward" ).setLevel( logging.DEBUG )
#logging.getLogger( "TestRover.test_rover_in_plateau" ).setLevel( logging.DEBUG )
unittest.main()















