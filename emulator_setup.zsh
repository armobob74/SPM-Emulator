#!/bin/zsh
SOCAT_LOGFILE="logfile.txt" # can't be changed as python script depends on it
echo $SOCAT_LOGFILE
# clear logfile for easy parsing
echo '' > $SOCAT_LOGFILE
# Get pseudo-terminals using socat
socat -lf $SOCAT_LOGFILE -d -d pty,raw,echo=0 pty,raw,echo=0
