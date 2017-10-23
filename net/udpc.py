# -*- coding: utf-8 -*-

"a network framework by udp(client)"

import socket
import threading

class UDPC(object):
	
	"""UDP Client"""

	def __init__(self, ip, port, portBind, queueRecv, queueSend, recvBuffLen=1024):
		# param
		self.__addr = (ip, port)
		self.__addrBind = (ip, portBind)
		self.__queueRecv = queueRecv
		self.__queueSend = queueSend
		self.__recvBuffLen = recvBuffLen

		# net
		self.__socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

		# thread
		self.__threadRecv = threading.Thread(target=self.__recv)
		self.__threadSend = threading.Thread(target=self.__send)

	def start(self):
		self.__socket.bind(self.__addrBind)
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
			print("[recv]%s,%s" % (data, addr))
			self.__queueRecv.put(data)
		print("finish revcing msg")

	def __send(self):
		print("begin sending msg")
		while True:
			data = self.__queueSend.get()
			print("[send][%s:%s]%s" % (*self.__addr, data))
			self.__socket.sendto(data.encode("utf-8"), self.__addr)
		print("finish sending msg")

