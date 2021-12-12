import numpy as np
import math

from PEG import PEG


class SEXTANS:
    def __init__(self, P, K_0, N_0):
        self.P = P
        self.K_0 = K_0
        self.N_0 = N_0

        self.PEG_0 = PEG(self.K_0)
        self.PEG_1 = PEG(self.K_0)
        self.PEG_2 = PEG(self.K_0)
        self.PEG_3 = PEG(self.K_0)
        self.PEG_4 = PEG(self.K_0)
        self.PEG_5 = PEG(self.K_0)
        self.PEG_6 = PEG(self.K_0)
        self.PEG_7 = PEG(self.K_0)
        self.PEGs = [self.PEG_0, self.PEG_1, self.PEG_2, self.PEG_3, self.PEG_4, self.PEG_5, self.PEG_6, self.PEG_7]

        self.collect = None

    def dot_multiply(self, A, B):
        a_dims = np.shape(A)
        b_dims = np.shape(B)
        self.collect = np.zeros((a_dims[0], b_dims[1]))

        if a_dims[1] != b_dims[0]:
            print('Invalid dimensions for dot multiplication')
            return

        for j in range(math.ceil(a_dims[1]/self.K_0)):                          #8 cols of result
            #print(j)
            A_j = A[:, self.K_0*j:self.K_0*(j+1)]
            A_pjs = np.zeros((self.P, math.ceil(a_dims[0]/self.P), self.K_0))
            for p in range(a_dims[0]):
                A_pjs[p % self.P, math.floor(p / self.P)] = A_j[p]

            #print(np.shape(A_j))
            #print(np.shape(A_pjs))
            np.set_printoptions(suppress=True)
            #print(A_pjs)
            for i in range(math.ceil(b_dims[1]/self.N_0)):
                B_ji = B[self.K_0*j:self.K_0*(j+1), self.N_0*i:self.N_0*(i+1)] #self.N_0*i:self.N_0*(i+1)]
                #print(np.shape(B_ji))
                #print(B_ji)
                self.PEG_0.multiply(self.schedule(A_pjs[0], 0, i), B_ji)
                self.PEG_1.multiply(self.schedule(A_pjs[1], 1, i), B_ji)
                self.PEG_2.multiply(self.schedule(A_pjs[2], 2, i), B_ji)
                self.PEG_3.multiply(self.schedule(A_pjs[3], 3, i), B_ji)
                self.PEG_4.multiply(self.schedule(A_pjs[4], 4, i), B_ji)
                self.PEG_5.multiply(self.schedule(A_pjs[5], 5, i), B_ji)
                self.PEG_6.multiply(self.schedule(A_pjs[6], 6, i), B_ji)
                self.PEG_7.multiply(self.schedule(A_pjs[7], 7, i), B_ji)

        result = self.accum()
        #print(result)
        return result

    def schedule(self, A_pj, p, i):
        dims = np.shape(A_pj)

        a_data = np.zeros((0,3))
        for row in range(dims[0]):
            for col in range(dims[1]):
                if A_pj[row,col] != 0:
                    a_val_row_col = np.array([[A_pj[row, col], row*self.P + p, col*(i+1)]]) #this is probably fucked up
                    a_data = np.append(a_data, a_val_row_col, axis=0)

        return a_data

    def accum(self):
        sum = np.zeros((64, 8))
        for i in range(8):
            for j in range(8):
                addend = np.zeros((64, 8))
                for k in range(8):
                    addend[:, k] = self.PEGs[i].PEs[j].PUs[k].scratch
                sum = sum + addend
        return sum