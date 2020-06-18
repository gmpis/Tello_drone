import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # we need udp

UDP_IP = "192.168.10.1"  # this is tello's ip
UDP_PORT = 8889          # this is for tello
t_dst = ((UDP_IP, UDP_PORT))


def t_send_cmd(byte_cmd, d_dest, s_delay=2):
    # send command
    # msg=b"command"
    s.sendto(byte_cmd, d_dest)
    
    # parse responce
    data, addr = s.recvfrom(1024)  # buffer is 1024 BYTES
    print("Received:", data, "from:", addr)
    time.sleep(s_delay)  # 2 seconds
    
    
# put tello to SDK mode
msg = b"command"
t_send_cmd(msg, t_dst)


# start video streaming
msg = b"streamon"
t_send_cmd(msg, t_dst)


# take off
msg = b"takeoff"
t_send_cmd(msg, t_dst)


# add some delay here
time.sleep(20)  # seconds


# land
msg = b"land"
t_send_cmd(msg, t_dst)


# stop video streaming
msg = b"streamoff"
t_send_cmd(msg, t_dst)
