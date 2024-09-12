#!/usr/bin/env python3


import sys

#  c0053 500 300 200

prevTime = 99999999999
for line in sys.stdin:
    line = line.strip()
    line = line.split()
    if line[1] == line[3]:
        print(" ".join(line[0:1] + line[2:] + ["1"]))
    else:
        print(" ".join(line[0:1] + line[2:] + ["0"]))
