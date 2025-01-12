import numpy as np

def reconstruct_matrix(U, S, V):
    if U.shape[1] != S.shape[0] or V.shape[0] != S.shape[1]:
        raise ValueError("Input matrices have incompatible shapes")

 
    return np.dot(U, np.diag(S)).dot(V)

   