import numpy as np


class PU:
    def __init__(self, M):
        self.M = M
        self.scratch = np.zeros(self.M)

    def cum_multiply(self, a_val, a_row, b_val):
        self.scratch[int(a_row)] = self.scratch[int(a_row)] + a_val * b_val

    def rst(self):
        self.scratch = np.zeros(self.M)
