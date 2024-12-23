import socket

class ethernet:
	def __init__(self, data: bytes):
		self.dst = ':'.join(map("{:02x}".format, data[0:6]))
		self.src = ':'.join(map("{:02x}".format, data[6:12]))
		self.proto = socket.htons((data[13] << 8) | data[12])
		self.data = data[14:]

	def __repr__(self) -> str:
		vars = map(
			lambda x: f"{x}={repr(getattr(self, x))}",
			filter(
				lambda x: not x.startswith("__"),
				self.__dict__.keys()
			)
		)
		return f"{self.__class__.__name__}({', '.join(vars)})"
