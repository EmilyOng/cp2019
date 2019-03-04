#!/bin/python3

import math
import os
import random
import re
import sys

def binary(n):
    s=""
    while n!=0:
        s+=str((int(n)%2))
        n=int(n)
        n/=2
        n=int(n)
    return s

if __name__ == '__main__':
    n = int(input())
    count=0
    res=0
    for i in binary(n):
        if i=='1':
            count+=1
            res=max(count,res)
        else:
            count=0
    print(res)
