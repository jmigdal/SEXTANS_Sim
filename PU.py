import numpy as np

class PU:
    def __init__(self, K_0):
        self.K_0 = K_0
        self.scratch = np.zeros((1, K_0))

    def cum_multliply(self, a_val, a_row, b_val):
        self.scratch[a_row] = self.scratch[a_row] + a_val * b_val

    def rst(self):
        self.scratch = np.zeros((1, self.K_0))
