import struct
import socket

class ethernet:
	__level__: int = 0

	def __init_subclass__(cls, *, level: int):
		cls.__level__ = level

	@classmethod
	def __protocols__(cls, level: int) -> list[type]:
		return [sub for sub in cls.__subclasses__() if sub.__level__ == level + 1]

	def __init__(self, data: bytes):
		self.dst, self.src, self.proto = struct.unpack("! 6s 6s H", data[:14])
		self.dst = ':'.join(map("{:02x}".format, self.dst))
		self.src = ':'.join(map("{:02x}".format, self.src))
		self.data = data[14:]

	def __str__(self) -> str:
		return f"{self.__class__.__name__}(...)"

	def __repr__(self) -> str:
		vars = map(
			lambda x: f"{x}={repr(getattr(self, x))}",
			filter(
				lambda x: not x.startswith("__"),
				self.__dict__.keys()
			)
		)
		return f"{self.__class__.__name__}({', '.join(vars)})"
