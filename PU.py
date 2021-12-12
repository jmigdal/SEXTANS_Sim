import numpy as np


class PU:
    def __init__(self, K_0):
        self.K_0 = K_0
        self.scratch = np.zeros(64)

    def cum_multiply(self, a_val, a_row, b_val):
        #print(a_val, b_val, a_val * b_val, int(a_row))
        self.scratch[int(a_row)] = self.scratch[int(a_row)] + a_val * b_val

    def rst(self):
        self.scratch = np.zeros(self.K_0)
