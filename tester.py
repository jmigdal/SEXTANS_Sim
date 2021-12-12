import numpy as np
import time

from SEXTANS import SEXTANS


s = SEXTANS(8, 8, 8)

A = np.arange(64*64).reshape((64, 64))/100
B = np.arange(64*8).reshape((64, 8))/100

test = s.dot_multiply(A, B)
print(test)
true = np.dot(A, B)
print("help me")
print(true)

np.savetxt("test.csv", test, delimiter=",")
if np.array_equal(np.around(test, decimals=4), np.around(true, decimals=4)):
    print("Hell yeah baybee")

# sum = np.zeros((64, 8))
# for i in range(8):
#     for j in range(8):
#         addend = np.zeros((64, 8))
#         for k in range(8):
#             addend[:, k] = s.PEGs[i].PEs[j].PUs[k].scratch
#         sum = sum + addend
# print(sum)
