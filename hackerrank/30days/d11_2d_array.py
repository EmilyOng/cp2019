#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    total=0
    mtotal=-65
    for k in range(6):
        for i in range(6):
            total=0
            if i<=3 and k<=3:
                for j in range(i,i+3):
                    total+=arr[k][j]
                    total+=arr[k+2][j]
                total+=arr[k+1][i+1]
                mtotal=max(mtotal,total)

    print(mtotal)
