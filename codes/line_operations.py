import numpy as np

#for finding the direction vector
def dir_vec(A, B):
    return B - A

#for finding the norm of the vector
def norm_vec(A,B):
    N = np.array([0.0,0.0])
    N = np.linalg.norm(B-A)
    return N

#section formula
def line_section(A,B,k):
    P = np.array([0.0,0.0])
    P[0] = ((B[0]*k)+A[0])/(k+1)
    P[1] = ((B[1]*k)+A[1])/(k+1)

    return P

