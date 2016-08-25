"""	Purpose
	Provides platform to control Sabertooth motor driver through Raspberry Pi 
	serial port.
	forward, reverse, left, right - speed passed to these methods only needs to
	be positive.
	motorLeft and motorRight is for manual driving and must be a value between
	-2047 to 2047.
"""

"""	Prerequisites
	Disable Raspberry Pi OS access to the UART (serial) port using raspi-config.
"""

import serial

class MotorControl():
	port = serial.Serial("/dev/ttyS0", baudrate = 9600, timeout = 1)
	RTN = "\r\n"
	
	def forward(self, speed):
		self.port.write("M1: " + str(speed) + self.RTN + "M2: " + str(speed) + self.RTN)
	
	def reverse(self, speed):
		self.port.write("M1: " + "-" + str(speed) + self.RTN + "M2: " + "-" + str(speed) + self.RTN)
	
	def coast(self):
		self.port.write("M1: 0" + self.RTN + "M2: 0" + self.RTN)
	
	def left(self, speed):
		self.port.write("M1: " + "-" + str(speed) + self.RTN + "M2: " + str(speed) + self.RTN)
	
	def right(self, speed):
		self.port.write("M1: " + str(speed) + self.RTN + "M2: " + "-" + str(speed) + self.RTN)
	
	def motorLeft(self, speed):
		self.port.write("M1: " + str(speed) + self.RTN)
	
	def motorRight(self, speed):
		self.port.write("M2: " + str(speed) + self.RTN)
