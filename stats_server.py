import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # we need udp

UDP_IP = ""
UDP_PORT = 8890          # this is for tello

s.bind((UDP_IP, UDP_PORT))

while True:
    # parse responce
    data, addr = s.recvfrom(1024)  # buffer is 1024 BYTES
    print("Received:", data, "from:", addr)
    
