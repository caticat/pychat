# -*- coding: utf-8 -*-

"服务器"

import sys
sys.path.append("..")
import queue
from net.udps import UDPS
from net.msg import MessageManager

def hello(sock, data):
	print("hello!")
	msgMgr.send(1, ("hello, %s" % data).encode("utf-8"), sock)

if __name__ == "__main__":
	print("begin")

	# 参数
	queueRecv = queue.Queue()
	queueSend = queue.Queue()

	# 网络
	udps = UDPS(9999, queueRecv, queueSend)
	udps.start()

	# 消息
	msgMgr = MessageManager(queueRecv, queueSend)
	msgMgr.regist(1, hello)
	msgMgr.start()

	# 逻辑
	pass

	# 结束
	msgMgr.join()
	udps.join()
	print("end")
