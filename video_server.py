import socket
import time  # for timestamp

c_timestamp = int(time.time())  # float: time in seconds since epoch
fl_name = "vStream_" + str(c_timestamp) + ".h264"  # for unique filenames
f = open(fl_name, "wb")

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # we need udp

UDP_IP = ""
UDP_PORT = 11111          # this is for tello
s.bind((UDP_IP, UDP_PORT))

m_buff_size = 65535  # max udp

while True:
    # parse responce
    data, addr = s.recvfrom(m_buff_size)  # buffer is 1024 BYTES
    print("Received:", data, "from:", addr)
    # print(data)
    f.write(data)
    f.flush()
    
