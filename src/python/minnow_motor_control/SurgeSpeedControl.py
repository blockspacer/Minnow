#!/usr/bin/env python
import time
import math
import numpy as np
from .controlconfig import * 

class speed_controller:

	def __init__(self):

		self.max_thrust = config_max_motor_thrust
		self.min_thrust = config_min_motor_thrust
		self.speed_thrust_map = np.poly1d(np.polyfit(config_map_speed,config_map_thrust,2))

	def update(self,desired_speed):
		# Thrust output
		self.speed_thrust = self.speed_thrust_map(desired_speed)

		# Motor safety limits
		if self.speed_thrust > self.max_thrust:
			self.speed_thrust = self.max_thrust
		if self.speed_thrust < self.min_thrust:
			self.speed_thrust = self.min_thrust

		return(self.speed_thrust)
