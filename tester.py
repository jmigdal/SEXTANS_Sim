import numpy as np

from SEXTANS import SEXTANS


s = SEXTANS(64, 8, 8, 8, 8)

A = np.arange(64*64).reshape((64, 64))/100
B = np.arange(64*9).reshape((64, 9))/100

test = s.dot_multiply(A, B)
true = np.dot(A, B)

if np.array_equal(np.around(test, decimals=4), np.around(true, decimals=4)):
    print("Hell yeah baybee")