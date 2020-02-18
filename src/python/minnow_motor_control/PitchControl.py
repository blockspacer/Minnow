#!/usr/bin/env python
import time
import math
from .controlconfig import * 

class pitch_controller:
    def __init__(self, prev_pitch_error=0, pitch_error_integral=0):
        self.pitch_kp = config_pitch_kp
        self.pitch_ki = config_pitch_ki
        self.pitch_kd = config_pitch_kd
        self.max_pitch_error_integral=config_max_pitch_error_integral

        self.prev_pitch_error=prev_pitch_error
        self.pitch_error_integral=pitch_error_integral
        self.desired_pitch=0.0
        self.pitch_error=0.0

    def update(self,current_pitch,speed_thrust):
        # Calculating heading error
        # +ve errors turns nose up
        self.pitch_error = self.desired_pitch - current_pitch

        print('Current Pitch',current_pitch)
        print('Desired Pitch',self.desired_pitch)
        print('Pitch error',self.pitch_error)

        # Setting the integral of the error
        self.pitch_error_integral = self.pitch_error_integral + self.pitch_error
        if self.pitch_error_integral > self.max_pitch_error_integral:
            self.pitch_error_integral = self.max_pitch_error_integral
        if self.pitch_error_integral < -self.max_pitch_error_integral:
            self.pitch_error_integral = -self.max_pitch_error_integral

        pitch_p_value = self.pitch_kp * self.pitch_error
        pitch_i_value = self.pitch_ki * (self.pitch_error_integral)
        pitch_d_value = self.pitch_kd * (self.pitch_error - self.prev_pitch_error)
        pitch_differential_thrust = pitch_p_value + pitch_i_value + pitch_d_value
        print('Pitch differential thrust ',pitch_differential_thrust)

        # mixing speed thrust and pitch diff thrust
        upper_thrust = speed_thrust - 0.5 *pitch_differential_thrust
        lower_thrust = speed_thrust + 0.5 *pitch_differential_thrust
        if (speed_thrust + 0.5 * abs(pitch_differential_thrust)) > config_max_motor_thrust:
            pitch_differential_thrust_correction = (speed_thrust + 0.5 * abs(pitch_differential_thrust)) - config_max_motor_thrust
            upper_thrust = upper_thrust - pitch_differential_thrust_correction
            lower_thrust = lower_thrust - pitch_differential_thrust_correction

        # motor safelty limits
        if upper_thrust > config_max_motor_thrust:
            upper_thrust = config_max_motor_thrust
        if lower_thrust > config_max_motor_thrust:
            lower_thrust = config_max_motor_thrust
        if upper_thrust < config_min_motor_thrust:
            upper_thrust = config_min_motor_thrust
        if lower_thrust < config_min_motor_thrust:
            lower_thrust = config_min_motor_thrust

        # For error deravative
        self.prev_pitch_error = self.pitch_error

        return(lower_thrust,upper_thrust)

    def DesiredPitch(self,desired_pitch):
        self.desired_pitch = desired_pitch
        self.pitch_error_integral=0
        self.prev_pitch_error=0
