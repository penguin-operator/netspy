import struct
import socket
import net

class icmp(net.ethernet, level=2):
	def __class_getitem__(cls, frame: net.ethernet) -> None | type:
		try:
			return cls if frame.proto == 1 else None
		except AttributeError:
			return None

	def __init__(self, data: bytes):
		self.type, self.code, _, self.rest = struct.unpack("! B B H I", data[:8])
