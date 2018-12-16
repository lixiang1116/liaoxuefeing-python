# -*- coding:utf-8 -*-

import socket

#参数
host='127.0.0.1'
port=80
buffersize=2048
ADDR=(host,port)

#创建socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)  #socket.AF_INET	用于服务器与服务器之间的网络通信,socket.SOCK_STREAM	基于TCP的流式socket通信
#绑定监听地址和端口
s.bind(ADDR)
#调用listen方法监听端口
s.listen(5)

#print('Server start at:%s:%s')%(host,port)
print('waiting for connection')

while True:
    conn,addr=s.accept()
    print('conneciton from ',addr)

    while True:
        receiveData=conn.recv(buffersize)
        print(receiveData.decode())
        psendData=input('Server:')
        sendData='Server：'+psendData
        #print(sendData)
        conn.send(sendData.encode())




