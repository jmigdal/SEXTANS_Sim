import numpy as np
from PU import PU


class PE:
    def __init__(self, K_0):
        self.K_0 = K_0
        self.acc = np.zeros((64, 8))
        self.PU_0 = PU(self.K_0)
        self.PU_1 = PU(self.K_0)
        self.PU_2 = PU(self.K_0)
        self.PU_3 = PU(self.K_0)
        self.PU_4 = PU(self.K_0)
        self.PU_5 = PU(self.K_0)
        self.PU_6 = PU(self.K_0)
        self.PU_7 = PU(self.K_0)
        self.PUs = [self.PU_0, self.PU_1, self.PU_2, self.PU_3, self.PU_4, self.PU_5, self.PU_6, self.PU_7]

    def rst_scratch(self):
        for i in range(8):
            self.PUs[i].rst()

    def pu_mult(self, a_val, a_row, a_col, B_ji):
        a_col = int(a_col)
        self.PU_0.cum_multiply(a_val, a_row, B_ji[a_col, 0])
        self.PU_1.cum_multiply(a_val, a_row, B_ji[a_col, 1])
        self.PU_2.cum_multiply(a_val, a_row, B_ji[a_col, 2])
        self.PU_3.cum_multiply(a_val, a_row, B_ji[a_col, 3])
        self.PU_4.cum_multiply(a_val, a_row, B_ji[a_col, 4])
        self.PU_5.cum_multiply(a_val, a_row, B_ji[a_col, 5])
        self.PU_6.cum_multiply(a_val, a_row, B_ji[a_col, 6])
        self.PU_7.cum_multiply(a_val, a_row, B_ji[a_col, 7])

        self.accum()


    def accum(self):
        p_sum = np.zeros((64, 8))
        for i in range(8):
            p_sum[:, 1] = self.PUs[i].scratch

        self.acc = self.acc + p_sum