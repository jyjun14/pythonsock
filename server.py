from socket import *
import os
import threading

port = 8081

sock = socket(AF_INET, SOCK_STREAM)

sock.bind(('', port))
sock.listen(1)
print("4444 포트로 접속 대기 중")
connectionSock, addr = sock.accept()
print("'{0}' 에서 접속 확인").format(addr)
input()