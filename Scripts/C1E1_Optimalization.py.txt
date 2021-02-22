
import math
import random
import numpy as np
import io
from io import StringIO
portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]
 
def permutation(start, end=[]):
    if len(start) == 0:
        if end[0] == 0:
            print(' '.join([portnames[i] for i in end]))
    else:
        for i in range(len(start)):
            permutation(start[:i] + start[i+1:], end + start[i:i+1])

def permutations(route, ports):

    routes = route + ports
    permutation(routes)

        # write the recursive function here
        # remember to print out the route as the recursion ends

# this will start the recursion with 0 as the first stop
permutations([0], list(range(1, len(portnames))))
