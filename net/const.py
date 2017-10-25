# -*- coding: utf-8 -*-

"const define"

# 长度
MSG_SIZE_LEN = 32 # 消息长度
MSG_PROTOCOL_LEN = 32 # 协议号长度

# 起始位置
MSG_SIZE_POS = 0
MSG_PROTOCOL_POS = MSG_SIZE_LEN
MSG_DATA_POS = MSG_PROTOCOL_POS + MSG_PROTOCOL_LEN
