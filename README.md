# Tello_drone   
   
## How to use   
- Open a new terminal and start stats_server: `python3 stats_server.py`   
- Open a new terminal and start video_server: `python3 video_server.py`   
- Power on Tello   
- Wait a few seconds for Tello to power on    
- Open a new terminal and run the script to send commands: `python3 control_client.py`
- After Tello has safely landed stop video_server (and stats_server)   
- Run frames parser script: `python3 frames_parser.py`   
