import numpy as np
import math

class SEXTANS:
    def __init__(self, P, K_0, N_0):
        self.P = P
        self.K_0 = K_0
        self.N_0 = N_0

    collect = None
    PEG_0 =
    PEG_1 =
    PEG_2 =
    PEG_3 =
    PEG_4 =
    PEG_5 =
    PEG_6 =
    PEG_7 =

    def dot_multiply(self, A, B):
        a_dims = np.shape(A)
        b_dims = np.shape(B)

        if a_dims[1] != b_dims[0]:
            print('Invalid dimensions for dot multiplication')
            return

        for j in range(math.ceil(a_dims[1]/self.K_0)):
            A_j = A[:, self.K_0*j:self.K_0*(j+1)]
            A_pjs = np.zeros((self.P, math.ceil(a_dims[0]/self.P), self.K_0))
            for p in range(math.ceil(a_dims[0]/self.P)):
                A_pjs[p % self.P, math.floor(p / self.P)] = A_j[p]

            for i in range(math.ceil(b_dims[1]/self.N_0)):
                B_ji = B[self.K_0*j:self.K_0*(j+1), self.N_0*i:self.N_0*(i+1)]
                PEG_0.multiply(self.schedule(A_pjs[0], 0, i), B_ji)
                PEG_1.multiply(self.schedule(A_pjs[1], 1, i), B_ji)
                PEG_2.multiply(self.schedule(A_pjs[2], 2, i), B_ji)
                PEG_3.multiply(self.schedule(A_pjs[3], 3, i), B_ji)
                PEG_4.multiply(self.schedule(A_pjs[4], 4, i), B_ji)
                PEG_5.multiply(self.schedule(A_pjs[5], 5, i), B_ji)
                PEG_6.multiply(self.schedule(A_pjs[6], 6, i), B_ji)
                PEG_7.multiply(self.schedule(A_pjs[7], 7, i), B_ji)

    def schedule(self, A_pj, p, i):
        dims = np.shape(A_pj)

        a_data = np.zeros((0,3))
        for row in range(dims[0]):
            for col in range(dims[1]):
                if A_pj[row,col] != 0:
                    a_val_row_col = np.array([[A_pj[row, col], row*self.P + p, col*(i+1)]]) #this is probably fucked up
                    a_data = np.append(a_data, a_val_row_col, axis=0)