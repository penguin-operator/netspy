import struct
import socket
import net

class arp(net.ethernet, level=1):
	def __class_getitem__(cls, frame: net.ethernet) -> None | type:
		return cls if frame.proto == 0x0806 else None

	def __init__(self, data: bytes):
		 ...
