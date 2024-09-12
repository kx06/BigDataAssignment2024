#!/usr/bin/env python3


import sys
import json

for line in sys.stdin:
    line = line.strip()
    if line.startswith("]") or line.startswith("["):
        continue
    if not line:
        continue
    if line[-1] == ",":
        line = line[:-1]
    data = json.loads(line)
    if len(data["categories"]) == 0:
        continue
    temp = [val for val in data["categories"] if val in data["sales_data"].keys()]
    len_temp = len(temp)
    if len_temp == 0:
        continue
    cost = 0
    state = False
    for y in temp:
        x = data["sales_data"][y]
        if "revenue" not in list(x.keys()) or "cogs" not in list(x.keys()):
            continue
        state = True
        cost += x["revenue"] - x["cogs"]
    if state == False:
        continue
    print(data["city"] + "," + str(cost))
