import itertools
import struct
import socket
import net

class ip6(net.ethernet, level=1):
	def __class_getitem__(cls, frame: net.ethernet) -> None | type:
		return cls if frame.proto == 0x86dd else None

	def __init__(self, data: bytes):
		self.version = data[0] >> 4
		self.proto, self.ttl, self.src, self.dst = struct.unpack("! 6x B B 16s 16s", data[:40])
		self.src = f"[{':'.join(map(lambda n: "{:02x}{:02x}".format(*n), itertools.batched(self.src, n=2)))}]"
		self.dst = f"[{':'.join(map(lambda n: "{:02x}{:02x}".format(*n), itertools.batched(self.dst, n=2)))}]"
		self.data = data[40:]
