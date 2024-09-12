#!/usr/bin/env python3


# 1169 r0172266 c0446 cart/add 1 200 700

import sys

seen = []
prev = []
tracker = {}

for line in sys.stdin:
    line = line.strip()
    line = line.split()
    if prev == []:
        seen = []
        servers = int(line[4])
        if servers == 0:
            print(" ".join(line[2:3] + line[5:] + ["500"]))
            prev = line
            seen.append(line[2])
            continue
        else:
            tracker.setdefault(line[3], servers - 1)
            print(" ".join(line[2:3] + line[5:] + ["200"]))
            prev = line
            seen.append(line[2])
            continue
    if line[0] == prev[0]:
        if line[2] in seen:
            continue
        if line[3] in tracker:
            servers = tracker[line[3]]
            if servers == 0:
                print(" ".join(line[2:3] + line[5:] + ["500"]))
            else:
                tracker[line[3]] -= 1
                print(" ".join(line[2:3] + line[5:] + ["200"]))
        else:
            servers = int(line[4])
            if servers == 0:
                print(" ".join(line[2:3] + line[5:] + ["500"]))
                tracker.setdefault(line[3], 0)
            else:
                tracker.setdefault(line[3], servers - 1)
                print(" ".join(line[2:3] + line[5:] + ["200"]))
        seen.append(line[2])

    else:
        seen = []
        tracker = {}
        servers = int(line[4])
        if servers == 0:
            tracker.setdefault(line[3], 0)
            print(" ".join(line[2:3] + line[5:] + ["500"]))
        else:
            tracker.setdefault(line[3], servers - 1)
            print(" ".join(line[2:3] + line[5:] + ["200"]))
        seen.append(line[2])
    prev = line
