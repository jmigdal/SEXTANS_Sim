import numpy as np

from SEXTANS import SEXTANS


def arr_equal(arr1, arr2):
    if np.array_equal(np.around(arr1, decimals=4), np.around(arr2, decimals=4)):
        return True
    else:
        return False


def rand_sparse_arr(dims, percentNonZero, maxMin):
    sparse = np.random.rand(dims[0], dims[1])
    sparse = (np.random.rand(dims[0], dims[1]) * (maxMin[1] - maxMin[0]) + maxMin[0]) * (sparse < percentNonZero)
    return sparse


for M in range(64, 1000, 51):
    for K in range(64, 1000, 51):
        for N in range(8, 16, 3):
            s = SEXTANS(M, 8, 8, 8, 8)
            A = rand_sparse_arr([M, K], 0.1, [-50, 50])
            B = rand_sparse_arr([K, N], .9, [-50, 50])

            test = s.dot_multiply(A, B)
            true = np.dot(A, B)

            if not arr_equal(test, true):
                print('oof')
            else:
                print(M, K, N, 'sucess')
