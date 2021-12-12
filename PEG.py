import numpy as np

from PE import PE


class PEG:
    def __init__(self, K_0):
        self.K_0 = K_0

        self.PE_0 = PE(self.K_0)
        self.PE_1 = PE(self.K_0)
        self.PE_2 = PE(self.K_0)
        self.PE_3 = PE(self.K_0)
        self.PE_4 = PE(self.K_0)
        self.PE_5 = PE(self.K_0)
        self.PE_6 = PE(self.K_0)
        self.PE_7 = PE(self.K_0)
        self.PEs = [self.PE_0, self.PE_1, self.PE_2, self.PE_3, self.PE_4, self.PE_5, self.PE_6, self.PE_7]

        self.collect = None

    def accum(self):
        p_sum = np.zeros((64, 8))
        for i in range(8):
            p_sum = p_sum + self.PEs[i].acc

        #print(p_sum)
        return p_sum

    def multiply(self, A_pj_data, B_ji):
        a_dims = np.shape(A_pj_data)
        a_data = A_pj_data

        for i in range(a_dims[0]):
            self.PEs[i % 8].pu_mult(a_data[i, 0], a_data[i, 1], a_data[i, 2], B_ji)

        self.accum()
