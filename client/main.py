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

def test(sock, data):
	print("[test]%s" % data)

if __name__ == "__main__":
	print("begin")
	queueRecv = queue.Queue()
	queueSend = queue.Queue()
	udpc = UDPC("127.0.0.1", 9999, queueRecv, queueSend)
	udpc.start()

	# 消息
	msgMgr = MessageManager(queueRecv, queueSend)
	msgMgr.regist(1, hello)
	msgMgr.regist(2, test)
	msgMgr.start()

	# 逻辑
	msgMgr.send(1, "world")
	time.sleep(0.1)
	msgMgr.send(1, "pan")
	time.sleep(0.1)
	msgMgr.send(1, "aaa")
	time.sleep(0.1)
	msgMgr.send(2, "222")
	time.sleep(0.1)

	msgMgr.stop()
	udpc.stop()

	msgMgr.join()
	udpc.join()
	print("end")
