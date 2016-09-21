#! usr/bin/env python
# -*- coding: utf-8 -*-
from simulator import *
import unittest

class RadioSystemTests(unittest.TestCase):
	def setUp(self):
		self.radio = RadioEmulation()

	def test_power_button(self):
		'''Turn on
		'''
		self.radio.power()
		self.assertEqual(self.radio.status, "on")
		'''Turn off
		'''
		self.radio.power()
		self.assertEqual(self.radio.status, "off")
	
	def test_get_set_station(self):
		self.radio.power() '''sets station to DW1 first'''
		self.assertEqual(self.radio.get_station(), "DW1")	
		
		'''Test set real station name and fake name'''
		self.radio.set_station("DW2")
		self.assertEqual(self.radio.get_station(), "DW2")
		with self.assertRaises(Exception):
			self.radio.set_station("DW4")

	def test_mute(self): 
		self.radio.set_volume(5)
		'''Test mute on
		'''
		self.radio.mute_on()
		self.assertEqual(self.radio.current_volume, 0)
		
		'''Test mute off, mute on 'pushed' above
		'''
		self.radio.mute_off()
		self.assertEqual(self.radio.current_volume, 5) '''volume should go back to 5 as it was before mute'''


	def test_volume_level(self):
		'''Test that volume sets correctly
		''' 
		self.radio.set_volume(5)
		self.assertEqual(self.radio.get_volume(), 5)
		
		'''Test that volume can't be set out of range
		'''
		with self.assertRaises(Exception):
			self.radio.set_volume(-1)
		with self.assertRaises(Exception):
			self.radio.set_volume(11)
					
	def test_setting_favorite_station(self):
		'''Set station to DW2 for favorite station
		'''
		self.radio.set_station("DW2")
		self.radio.favorite_station()
		self.assertEqual(self.radio.favorite, "DW2")

		'''Test that favorite station was stored correctly
		'''
		self.assertEqual(self.radio.restore_station(),"DW2")
		
	def test_setting_DW3_changes_volume(self):
		'''Test volume raises by 3
		'''
		self.radio.set_volume(5)
		self.radio.set_station("DW3")
		self.assertEqual(self.radio.current_volume, 8)
		
		'''Test if volume raises every time DW3 button is pushed
		'''
		self.radio.set_station("DW3")
		self.assertEqual(self.radio.current_volume, 8)


unittest.main()


