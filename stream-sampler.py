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

reservoir = reservoir_sampling(int(sys.argv[1]))
next(reservoir)

while True:
    char = sys.stdin.read(1)

    if char == '' or char == "\n":
        print(''.join(sample))
        break    
    k, sample = reservoir.send(char)
   
