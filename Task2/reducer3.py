#!/usr/bin/env python3


import sys


# c06 9 r236 support/ticket 0 500 1000 500
# c01 1/3 500
# c0053 300 0 200
prevClient = ""
valid = 0
total = 0
cost = 0

for line in sys.stdin:
    line = line.split()
    client = line[0]
    amt = int(line[1])
    check = line[3]
    rtype = line[2]
    if prevClient != client and prevClient != "":
        print(f"{prevClient} {valid}/{total} {cost}")
        if check == "1":
            valid = 1
            total = 1
            if rtype == "200":
                cost = amt
            else:
                cost = 0
        else:
            valid = 0
            total = 1
            if rtype == "200":
                cost = amt
            else:
                cost = 0
    else:
        if check == "1":
            valid += 1
            total += 1
            if rtype == "200":
                cost += amt
        else:
            total += 1
            if rtype == "200":
                cost += amt
    prevClient = client
print(f"{prevClient} {valid}/{total} {cost}")
