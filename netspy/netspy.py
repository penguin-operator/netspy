import socket
import net
import ui

class netspy:
	__instance__ = None
	__socket__ = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))

	def __new__(cls, *args, **kwargs):
		if not cls.__instance__:
			cls.__instance__ = object.__new__(cls, *args, **kwargs)
		return cls.__instance__

	def __call__(self, buffsize=65336) -> list[net.ethernet]:
		raw = self.__socket__.recv(buffsize)
		frames = [net.ethernet(raw)]
		while True:
			for proto in net.ethernet.__protocols__(frames[-1].__class__.__level__):
				if proto[frames[-1]]:
					frames += [proto[frames[-1]](frames[-1].data)]
					break
			else: return frames

	def __del__(self):
		self.__socket__.close()
