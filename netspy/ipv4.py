import socket
import ethernet

class ipv4(ethernet.ethernet):
	def __class_getitem__(cls, frame: ethernet.ethernet) -> None | type:
		return cls if frame.proto == 0x0800 else None

	def __init__(self, data: bytes):
		self.version = data[0] >> 4
		self.headerlen = (data[0] & 15) * 4
		self.ttl = data[8]
		self.proto = data[9]
		self.sender = '.'.join(map(str, data[12:16]))
		self.target = '.'.join(map(str, data[16:20]))
		self.data = data[self.headerlen:]
