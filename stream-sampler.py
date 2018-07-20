#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 23:35 2018
@author: Venkateshwaran Loganathan
"""

#import the necessary modules
import numpy as np
import sys

#This implementation is based on reservoir sampling algorithm. 
def reservoir_sampling(size):
    "This generator function takes input of the length of the sampling string needed and yields a string sample"
    i, sample = 0, []

    while True:
        item = yield i, sample
        
        i += 1
        k = np.random.randint(0, i)
        if len(sample) < size:
            sample.append(item)
        elif k < size:
            sample[k] = item

#Get the sample size from user as input
reservoir = reservoir_sampling(int(sys.argv[1]))
next(reservoir)

def main():
    while True:
        #Read the characters one by one from the input stream sys.stdin 
        char = sys.stdin.read(1)

        if char == '' or char == "\n":
            return ''.join(sample)
            break    
        k, sample = reservoir.send(char)
   
if __name__== "__main__":
    print(main())
