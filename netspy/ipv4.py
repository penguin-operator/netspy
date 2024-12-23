import socket
import ethernet

class ipv4(ethernet.ethernet):
	def __class_getitem__(cls, frame: ethernet.ethernet) -> None | type:
		return cls if frame.proto == 0x0800 else None

	def __init__(self, data: bytes):
		...
