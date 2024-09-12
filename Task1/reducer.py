#!/usr/bin/env python3

import sys

prevStore = ""
proft_stores = 0
loss_stores = 0
for line in sys.stdin:
    data = line.split(",")
    cost = int(data[1])
    store = data[0]
    if store == prevStore or not prevStore:
        if cost > 0:
            proft_stores += 1
        else:
            loss_stores += 1
    else:
        print(
            f'{{"city": "{prevStore}", "profit_stores": {proft_stores}, "loss_stores": {loss_stores}}}'
        )
        if cost > 0:
            proft_stores = 1
            loss_stores = 0
        else:
            loss_stores = 1
            proft_stores = 0
    prevStore = store
print(
    f'{{"city": "{prevStore}", "profit_stores": {proft_stores}, "loss_stores": {loss_stores}}}'
)
