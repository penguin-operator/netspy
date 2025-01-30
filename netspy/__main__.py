#!/usr/bin/python3.13
import netspy

try:
	app = netspy.netspy()
	while True:
		print(app())
except KeyboardInterrupt:
	print(end="\r")
