:'  Author:   Harsh Chaturvedi
    Usecase:  This file has been written to extract
              inter-frame time spacing and icmp response
              time and write it into a txt file. It couples
              with a python script (also present in this repo)
              that will calculate features on the two types of
              values that have been extracted.
    Requires: tshark and python to be installed
    Usage:    just run the script with pcaps and pythons script
              in the right folders.
              Read the python script to understand inputs to python
'

#!/bin/bash
tshark -r ../pcap/<pcap_name>.pcapng -Y "icmp.type==0" -T fields -e frame.time_delta > FrameTimeDelta.txt
python ../python/ipDeltaMod.py FrameTimeDelta.txt ../csv/FrameTimeDeltaOut.csv 99 A

tshark -r ../pcap/Linux_pcap/<pcap name>.pcapng -Y "icmp.type==0" -T fields -e icmp.resptime > RespTimeDelta.txt
python ../python/ipDeltaMod.py RespTimeDelta.txt ../csv/RespTimeDeltaOut.csv 99 A
