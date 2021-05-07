import socket
import time
import math

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # we need udp

UDP_IP = "192.168.10.1"  # this is tello's ip
UDP_PORT = 8889          # this is for tello
t_dst = ((UDP_IP, UDP_PORT))

# edit flight params here
# 100cm == 1m
UP_ELEVATION = 21  # x value in cm, valid x: 20 - 500
NUM_OF_STEPS = 18  # number of steps to make a full 360 degree rotation
DELAY_PER_STEP = 2 # in seconds
# end of flight params, DONT EDIT AFTER here

# auto calculated values, DONT EDIT
degrees_per_step = 360 / NUM_OF_STEPS  # number of degrees to turn at each step
degrees_per_step = math.ceil(degrees_per_step)  # convert 16.36363 to 17
rotation_duration = DELAY_PER_STEP * NUM_OF_STEPS  # rotation duration in seconds

def t_send_cmd(byte_cmd, d_dest, s_delay=2):
    # send command
    # msg=b"command"
    s.sendto(byte_cmd, d_dest)
    
    # parse responce
    data, addr = s.recvfrom(1024)  # buffer is 1024 BYTES
    data = data.decode("utf-8")
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


# go up
msg_str = "up " + str(UP_ELEVATION)
msg = msg_str.encode("utf-8")
t_send_cmd(msg, t_dst)


# add some delay here
# time.sleep(20)  # seconds


# do the rotations here
curr_rotation = 0
print("Starting " + str(NUM_OF_STEPS) + " steps rotation for: " + str(rotation_duration) + " seconds.")
for tmp_rot_indx in range(NUM_OF_STEPS):
    # send rotate cmd
    # msg_str = "ccw " + str(degrees_per_step)  # rotate x degrees counter-clockwise, valid x: 1 - 360
    msg_str = "cw " + str(degrees_per_step)  # rotate x degrees clockwise, valid x: 1 - 360
    msg = msg_str.encode("utf-8")
    t_send_cmd(msg, t_dst, DELAY_PER_STEP)
    
    # update vars
    curr_rotation += degrees_per_step
    print("Rotated " + str(degrees_per_step) + " degrees. Total rotation: " + str(curr_rotation) + ".")
    

# go down
msg_str = "down " + str(UP_ELEVATION)
msg = msg_str.encode("utf-8")
t_send_cmd(msg, t_dst)


# land
msg = b"land"
t_send_cmd(msg, t_dst)


# stop video streaming
msg = b"streamoff"
t_send_cmd(msg, t_dst)
