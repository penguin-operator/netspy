import struct
import socket
import net

class udp(net.ethernet, level=2):
	def __class_getitem__(cls, frame: net.ethernet) -> None | type:
		try:
			return cls if frame.proto == 17 else None
		except AttributeError:
			return None

	def __init__(self, data: bytes):
		self.src, self.dst, self.len, _ = struct.unpack("! H H H H", data[:8])
		self.data = data[8:]
