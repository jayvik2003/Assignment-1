import numpy as np

from line_operations import line_section,dir_vec,line_intersect

A = np.array([1,-1])

B = np.array([-4,6])

C = np.array([-3,-5])
E = np.array([0,0])
F = np.array([0,0])

E = line_section(C,A,1)
F = line_section(A,B,1.0)

G=line_intersect(B,E,C,F)

print("The intersection of BE and CF is ",G)

#by manipulating the section formula for BGE we can find k 

k = (G[0]-B[0])/(E[0]-G[0])

print("the value of k in the section formula for BGE is",k)


