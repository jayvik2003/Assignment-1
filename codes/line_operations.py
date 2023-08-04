import numpy as np

def dir_vec(A, B):
    return B - A

def line_section(A,B,k):
    P = np.array([0.0,0.0])
    P[0] = ((B[0]*k)+A[0])/(k+1)
    P[1] = ((B[1]*k)+A[1])/(k+1)

    return P

def line_intersect(B,E,C,F):
    x=np.array([0,0])
    m1=dir_vec(B,E)
    m2=dir_vec(C,F)
    #using the 1.1.4 equations
    x[0]=(m2[0]*B[0]-m1[0]*C[0])/(m2[0]-m1[0])
    x[1]=(m2[1]*B[1]-m1[1]*C[1])/(m2[1]-m1[1])


    return x
