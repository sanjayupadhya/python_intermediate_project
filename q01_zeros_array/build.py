# %load q01_zeros_array/build.py
# Default Imports
import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir),  '..'  ))
import numpy as np

def array_zeros() :
    return np.zeros((3,4,2))

print array_zeros()
# Your solution




