#!/usr/bin/env python3

import sys


# r299 c10 support/ticket 73 2 500


costs = {
    "user/profile": 100,
    "user/settings": 200,
    "order/history": 300,
    "order/checkout": 400,
    "product/details": 500,
    "product/search": 600,
    "cart/add": 700,
    "cart/remove": 800,
    "payment/submit": 900,
    "support/ticket": 1000,
}

for line in sys.stdin:
    line = line.strip()
    line = line.split()
    cost = str(costs[line[2]])
    print(
        " ".join(
            line[3:4]
            + line[0:1]
            + line[1:2]
            + line[2:3]
            + line[4:5]
            + line[5:6]
            + [cost]
        )
    )
