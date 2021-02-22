
import math
import random
import numpy as np
import io
from io import StringIO
import numpy as np

def generate(p1):
    # change this so that it generates 10000 random zeros and ones
    # where the probability of one is p1
    seq = np.random.choice([0,1], p=[1-p1, p1], size=10000)
    return seq

def count(seq):
    # insert code to return the number of occurrences of 11111 in the sequence
    i = 0
    count11s = 0
    for i in range(len(seq)-4):
        if (seq[i] == 1):
            if(seq[i + 1] == 1):
                if(seq[i + 1 + 1] == 1):
                    if(seq[i + 1 + 1 + 1] == 1):
                        if(seq[i + 1 + 1 + 1 + 1] == 1):
                            count11s = count11s + 1
           

    return count11s

def main(p1):
    seq = generate(p1)
    return count(seq)

print(main(2/3))

  