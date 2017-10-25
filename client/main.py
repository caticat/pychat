# -*- coding: utf-8 -*-

"客户端"

import sys
sys.path.append("..")
import queue
from net.udp.client import UDPC
from net.udp.message import MessageManager
import time

def hello(sock, data):
	print("[hello]%s" % data)

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
	time.sleep(1)
	msgMgr.send(1, "pan")
	time.sleep(1)
	msgMgr.send(1, "aaa")

	udpc.join()
	print("end")
