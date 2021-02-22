
import math
import random
import numpy as np
import io
from io import StringIO
import numpy as np

data = [[1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 3, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1]]
def distance(row1, row2):
    # replace the following by a function that returns the sum of differences between the
    # words in row1 and row2. this is the Manhattan distance.
    # you can assume that row1 and row2 are list with equal length, containing numeric values.
    dist1 = 0
    for i in range(len(row2)):
        dist1=dist1 + abs(row1[i]-row2[i])
    #print(dist1)
    return dist1

def find_nearest_pair(data):
    N = len(data)
    dist1 = [[distance(sent1, sent2) for sent1 in data] for sent2 in data]
    #print(dist1)
    #dist = np.empty((N, N), dtype=np.float)
    dist=np.array(dist1)
    #print(dist)
    row=-1
    for item in range(0,5):
        row=row+1
        column=-1
        for i in range(0,5):
            column = column+1
            if (row==column):
                dist[row,column]=1000000
    #dist[row,column]=1000000
    #print(dist)
    print(np.unravel_index(np.argmin(dist), dist.shape))

find_nearest_pair(data)

  