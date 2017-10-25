# -*- coding: utf-8 -*-

"udp data"

class AddrData(object):
	def __init__(self, addr, ptl, data):
		self.addr = addr
		self.ptl = ptl
		self.data = data

def int_to_bytes(x):
    return x.to_bytes((x.bit_length() + 7) // 8, 'big')

def int_from_bytes(xbytes):
    return int.from_bytes(xbytes, 'big')
