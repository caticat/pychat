# -*- coding: utf-8 -*-

"客户端"

import sys
sys.path.append("..")
import queue
from net.udpc import UDPC

if __name__ == "__main__":
	print("begin")
	queueRecv = queue.Queue()
	queueSend = queue.Queue()
	udpc = UDPC("127.0.0.1", 9999, 10000, queueRecv, queueSend)
	udpc.start()

	queueSend.put("world")

	udpc.join()
	print("end")

