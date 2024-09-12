#!/usr/bin/env python3


import sys


for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    line = line.split()
    if len(line) != 2:
        time = line[3]
        time = time.split(":")
        time = int(time[0]) * 60 * 60 + int(time[1]) * 60 + int(time[2])
        line[3] = str(time)
        if len(line) != 4:
            line[4] = str(3 - int(float(line[4])))
        else:
            line.append("3")
        print(" ".join(line))
    else:
        print(" ".join(line))
