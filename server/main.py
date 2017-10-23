# -*- coding: utf-8 -*-

"服务器"

import sys
sys.path.append("..")
import queue
from net.udps import UDPS

if __name__ == "__main__":
	print("begin")
	queueRecv = queue.Queue()
	queueSend = queue.Queue()
	udps = UDPS(9999, queueRecv, queueSend)
	udps.start()
	udps.join()
	print("end")
