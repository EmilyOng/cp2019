#!/bin/python3

import sys

S = input().strip()
try:
    S=int(S)
except ValueError:
    print("Bad String")
    sys.exit()
print(S)
