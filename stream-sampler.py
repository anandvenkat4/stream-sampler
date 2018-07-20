import numpy as np
import sys

def reservoir_sampling(size):
    i, sample = 0, []
    while True:
        item = yield i, sample
        
        i += 1
        k = np.random.randint(0, i)
        if len(sample) < size:
            sample.append(item)
        elif k < size:
            sample[k] = item

reservoir = reservoir_sampling(5)
next(reservoir)

while True:
    line = sys.stdin.read(1)
    if line == "\n":
        break    
    k, sample = reservoir.send(line)
    print(k, sample)
