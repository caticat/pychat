# -*- coding: utf-8 -*-

"a network framework by udp(client)"

import socket
import threading
from net.udpd import *

class UDPC(object):
	
	"""UDP Client"""

	def __init__(self, ip, port, queueRecv, queueSend, portBind = 10000, recvBuffLen=1024):
		# param
		self.__addr = (ip, port)
		self.__addrBind = [ip, portBind]
		self.__queueRecv = queueRecv
		self.__queueSend = queueSend
		self.__recvBuffLen = recvBuffLen

		# net
		self.__socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

		# thread
		self.__threadRecv = threading.Thread(target=self.__recv)
		self.__threadSend = threading.Thread(target=self.__send)

	def start(self):
		for port in range(self.__addrBind[1], 65535):
			if port == self.__addr[1]:
				continue
			if self.__port_is_free(port):
				self.__addrBind[1] = port
				break
		self.__socket.bind(tuple(self.__addrBind))
		self.__threadRecv.start()
		self.__threadSend.start()

	def join(self):
		self.__threadRecv.join()
		self.__threadSend.join()

	def __recv(self): 
		print("begin revcing msg")
		while True:
			# 拆包问题
			data, addr = self.__socket.recvfrom(self.__recvBuffLen)
			data = data.decode("utf-8")
			ptl = 0
			if data.find(":") > 0:
				ptl, data = data.split(":", 1)
			else:
				ptl = 1
				print("data invalid")
			print("[recv]%s,%s" % (data, addr))
			self.__queueRecv.put(AddrData(addr, int(ptl),data))
		print("finish revcing msg")

	def __send(self):
		print("begin sending msg")
		while True:
			addrData = self.__queueSend.get()
			data = "%s:%s" % (addrData.ptl, addrData.data)
			print("[send][%s:%s]%s" % (*self.__addr, data))
			self.__socket.sendto(data.encode("utf-8"), self.__addr)
		print("finish sending msg")

	def __port_is_free(self, port):
		# logger.debug('check port %d is free', port)
		print('check port %d is free' % port)
		s = socket.socket()
		s.settimeout(0.5)
		try:
			#s.connect_ex return 0 means port is open
			return s.connect_ex(('localhost', port)) != 0
		finally:
			s.close()

