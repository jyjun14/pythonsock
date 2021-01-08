import socket
import os
import threading

port = 8080

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('211.108.167.150', port))

print("접속 성공")
input()