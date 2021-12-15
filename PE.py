import numpy as np
from PU import PU


class PE:
    def __init__(self, M, N_0):
        self.M = M
        self.N_0 = N_0
        self.acc = np.zeros((self.M, self.N_0))

        self.PUs = [None] * self.N_0
        for i in range(self.N_0):
            self.PUs[i] = PU(self.M)

    def rst_scratch(self):
        for i in range(self.N_0):
            self.PUs[i].rst()

    def pu_mult(self, a_val, a_row, a_col, B_ji):
        a_col = int(a_col)
        #print(np.shape(B_ji))
        #print(a_row, a_col, a_val)
        for i in range(np.shape(B_ji)[1]):
            self.PUs[i].cum_multiply(a_val, a_row, B_ji[a_col, i])

        self.accum()

    def accum(self):
        p_sum = np.zeros((self.M, self.N_0))
        for i in range(self.N_0):
            p_sum[:, i] = self.PUs[i].scratch

        self.acc = self.acc + p_sum
