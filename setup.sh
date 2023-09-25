#!/bin/bash

#updating and upgrading
sudo apt update && apt upgrade -y

#clear the screen
clear

#installing requirements.txt
pip install -r requirements.txt

#clear the screen
clear

#run the python file
#example: "python3 ip_tracker.py <ip-address/domain>"

python3 ip_tracker.py $1
