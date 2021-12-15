import numpy as np
import math

from PEG import PEG


class SEXTANS:
    def __init__(self, M, P, K_0, N_0, num_PE):
        self.M = M
        self.P = P
        self.K_0 = K_0
        self.N_0 = N_0
        self.num_PE = num_PE

        self.PEGs = [None] * self.P
        for i in range(self.P):
            self.PEGs[i] = PEG(self.M, self.N_0, self.num_PE)

        self.collect = None

    def dot_multiply(self, A, B):
        a_dims = np.shape(A)
        b_dims = np.shape(B)
        self.collect = np.zeros((a_dims[0], b_dims[1]))

        if a_dims[0] != self.M:
            print('Row dimension of Sparse matrix is not equal to M value')
            return

        if a_dims[1] != b_dims[0]:
            print('Invalid dimensions for dot multiplication')
            return

        for j in range(math.ceil(a_dims[1]/self.K_0)):                          #8 cols of result
            A_j = A[:, self.K_0*j:self.K_0*(j+1)]
            A_pjs = np.zeros((self.P, math.ceil(a_dims[0]/self.P), np.shape(A_j)[1]))
            for p in range(a_dims[0]):
                A_pjs[p % self.P, math.floor(p / self.P)] = A_j[p]

            #print(np.shape(A_j))
            #print(np.shape(A_pjs))
            #print(np.shape(A_j)[1])
            np.set_printoptions(suppress=True)
            #print(A_pjs)
            for i in range(math.ceil(b_dims[1]/self.N_0)):
                B_ji = B[self.K_0*j:self.K_0*(j+1), self.N_0*i:self.N_0*(i+1)] #self.N_0*i:self.N_0*(i+1)]
                #print(np.shape(B_ji))
                #print(B_ji)
                #print(A_pjs)
                for peg in range(self.P):
                    self.PEGs[peg].multiply(self.schedule(A_pjs[peg], peg, i), B_ji)

                self.collect[:, i*self.N_0:(i+1)*self.N_0] = self.collect[:, i*self.N_0:(i+1)*self.N_0] + self.accum(np.shape(B_ji)[1])
                self.rst()

        #result = self.accum()
        #print(result)
        return self.collect

    def schedule(self, A_pj, p, i):
        dims = np.shape(A_pj)

        a_data = np.zeros((0,3))
        for row in range(dims[0]):
            for col in range(dims[1]):
                if A_pj[row, col] != 0:
                    a_val_row_col = np.array([[A_pj[row, col], row*self.P + p, col]]) #this is probably fucked up
                    a_data = np.append(a_data, a_val_row_col, axis=0)

        return a_data

    def accum(self, cols):
        sum = np.zeros((self.M, cols))
        for i in range(self.P):
            for j in range(self.num_PE):
                addend = np.zeros((self.M, cols))
                for k in range(cols):
                    addend[:, k] = self.PEGs[i].PEs[j].PUs[k].scratch
                sum = sum + addend
        return sum

    def rst(self):
        for i in range(self.P):
            self.PEGs[i].rst()
