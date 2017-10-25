# -*- coding: utf-8 -*-

"客户端"

import sys
sys.path.append("..")
import queue
from net.udpc import UDPC
from net.msg import MessageManager

def hello(sock, data):
	print("hello:%s,%s" % (sock, data))

if __name__ == "__main__":
	print("begin")
	queueRecv = queue.Queue()
	queueSend = queue.Queue()
	udpc = UDPC("127.0.0.1", 9999, queueRecv, queueSend)
	udpc.start()

	# 消息
	msgMgr = MessageManager(queueRecv, queueSend)
	msgMgr.regist(1, hello)
	msgMgr.start()

	# 逻辑
	msgMgr.send(1, "world")
	msgMgr.send(1, "pan")
	msgMgr.send(1, "aaa")

	udpc.join()
	print("end")
