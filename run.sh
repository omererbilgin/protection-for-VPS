#!/bin/bash

clear
printf "Run in background? [Y]/[n] "
read answer

if [ "$answer" == "Y" ] || [ "$answer" == "y" ]
then
sudo -b python3 vps-prot.py
else
sudo python3 vps-prot.py
fi

clear
