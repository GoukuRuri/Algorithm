# -*- coding:utf-8 -*-

import numpy

def LD(A,B):

    # initialize
    matrix = numpy.zeros([len(A)+1,len(B)+1])
    for i in xrange(1,len(A)+1):
        matrix[i][0] = i
    for j in xrange(1,len(B)+1):
        matrix[0][j] = j
    # LD
    for i in range(1,len(A)+1):
        for j in range(1,len(B)+1):
            if A[i-1] == B[j-1]:
                matrix[i][j] = matrix[i-1][j-1]
            else:
                matrix[i][j] = min(matrix[i-1][j-1],matrix[i][j-1],matrix[i-1][j]) + 1
    print matrix
    return matrix[len(A)][len(B)]


if "__main__":
    print LD('GGATCGA','GAATTCAGTTA')