# -*- coding: utf-8 -*-

"msg manager"

import threading
from net.udp.data import *

class MessageManager(object):
	
	"""message management"""

	def __init__(self, queueRecv, queueSend):
		self.__queueRecv = queueRecv
		self.__queueSend = queueSend
		self.__protocol = dict()

		# thread
		self.__threadRecv = threading.Thread(target=self.__recv)

	def start(self):
		self.__threadRecv.start()

	def join(self):
		self.__threadRecv.join()

	def regist(self, ptl, fun):
		self.__protocol[ptl]=fun

	def __recv(self):
		while True:
			addrData = self.__queueRecv.get()
			if addrData.ptl in self.__protocol:
				self.__protocol[addrData.ptl](addrData.addr, addrData.data)
			else:
				print("[ERROR]no ptl[%s]" % addrData.ptl)

	def send(self, ptl, msg, addr = ""):
		self.__queueSend.put(AddrData(addr, ptl, msg))
