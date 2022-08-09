
## server code
# 导入所需的库
import socket
import datetime
import struct
import time

# 配置UDP
BUFSIZE = 16  # 缓冲池容量
ip_serverport = ('127.0.0.1', 8004)  # Server端ip地址及端口
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # 无需更改

print('开始UDP通讯_Server端')
server.bind(ip_serverport)
for i in range(1, 10):
    data, client_addr = server.recvfrom(BUFSIZE)  # 接收数据包
    receivedata1 = struct.unpack("d""d", data)[0]  # 解包
    receivedata2 = struct.unpack("d""d", data)[1]  # 解包
    print(receivedata1)  # 输出接收到的数据
    print(receivedata2)  # 输出接收到的数据