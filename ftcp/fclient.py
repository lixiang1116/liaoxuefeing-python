# -*- coding:utf-8 -*-
import socket
host='127.0.0.1'
port=80
#创建socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#建立连接
s.connect((host,port))
#发送数据和接受数据
while True:
    psendData = input('Client:')
    sendData='Client：'+psendData
    s.send(sendData.encode())
    receiveData = s.recv(1024)
    print(receiveData.decode())