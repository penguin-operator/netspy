import struct
import socket
import net

class ip4(net.ethernet, level=1):
	def __class_getitem__(cls, frame: net.ethernet) -> None | type:
		return cls if frame.proto == 0x0800 else None

	def __init__(self, data: bytes):
		self.version = data[0] >> 4
		self.headerlen = (data[0] & 15) * 4
		self.ttl, self.proto, self.src, self.dst = struct.unpack("! 8x B B 2x 4s 4s", data[:20])
		self.src = '.'.join(map(str, self.src))
		self.dst = '.'.join(map(str, self.dst))
		self.data = data[self.headerlen:]
