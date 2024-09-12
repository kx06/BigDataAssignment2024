#!/usr/bin/env python3


import sys

prev_line = ["lsp is dumb or me is dumb"]

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    line = line.split()
    if line[0] == prev_line[0]:
        print(" ".join(line + [prev_line[1]]))
    else:
        prev_line = line
