#!/usr/bin/python3.13
import socket
import ethernet
import ipv4

connection = socket.socket(
	socket.AF_PACKET,
	socket.SOCK_RAW,
	socket.ntohs(3),
)

try:
	while True:
		raw = connection.recv(65536)
		frame = ethernet.ethernet(raw)
		while frame:
			print(frame)
			if frame.__class__.__subclasses__() == []:
				break
			for proto in frame.__class__.__subclasses__():
				if proto[frame]:
					frame = proto[frame](frame.data)
					break
except KeyboardInterrupt:
	print(end="\r")
finally:
	connection.close()
