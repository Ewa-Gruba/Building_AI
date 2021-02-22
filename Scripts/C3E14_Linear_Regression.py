
import math
import random
import numpy as np
import io
from io import StringIO
import numpy as np

from io import StringIO


train_string = '''
25 2 50 1 500 127900
39 3 10 1 1000 222100
13 2 13 1 1000 143750
82 5 20 2 120 268000
130 6 10 2 600 460700
115 6 10 1 550 407000
'''

test_string = '''
36 3 15 1 850 196000
75 5 18 2 540 290000
'''


def main():


    np.set_printoptions(precision=1)    # this just changes the output settings for easier reading

    # read in the training data and separate it to x_train and y_train
    x_train = np.genfromtxt(StringIO(train_string), skip_header=1)
    # read the data in and fit it. the values below are placeholder values
    c = np.linalg.lstsq(x_train[:,:-1] , x_train[:,-1])[0]  # coefficients of the linear regression

    # read in the test data and separate x_test from it
    x_test = np.genfromtxt(StringIO(test_string), skip_header=1)
    x_test = x_test[:,:-1]

    # print out the linear regression coefficients
    print(c)
    print(x_test @ c)

#train_s = StringIO(train_string)
#test_s = StringIO(test_string)

main()

  