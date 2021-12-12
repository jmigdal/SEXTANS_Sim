from PU import PU


class PE:
    def __init__(self):
        self.acc
    def pu_init(self):
        self.PU_0 = PU()
        self.PU_1 = PU()
        self.PU_2 = PU()
        self.PU_3 = PU()
        self.PU_4 = PU()
        self.PU_5 = PU()
        self.PU_6 = PU()
        self.PU_7 = PU()
    def rst_scratch(self):
        self.PU_0.rst()
        self.PU_1.rst()
        self.PU_2.rst()
        self.PU_3.rst()
        self.PU_4.rst()
        self.PU_5.rst()
        self.PU_6.rst()
        self.PU_7.rst()
    def pu_mult(self, a_val, a_row, a_col, B_ji):
        self.PU_0.cum_multiply(a_val, a_row, B_ji[a_col, 0])
        self.PU_1.cum_multiply(a_val, a_row, B_ji[a_col, 1])
        self.PU_2.cum_multiply(a_val, a_row, B_ji[a_col, 2])
        self.PU_3.cum_multiply(a_val, a_row, B_ji[a_col, 3])
        self.PU_4.cum_multiply(a_val, a_row, B_ji[a_col, 4])
        self.PU_5.cum_multiply(a_val, a_row, B_ji[a_col, 5])
        self.PU_6.cum_multiply(a_val, a_row, B_ji[a_col, 6])
        self.PU_7.cum_multiply(a_val, a_row, B_ji[a_col, 7])