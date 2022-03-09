import numpy as np
S = np.array([1, 2, 3, 4, 5])
n_of_zeros = 5
do = np.zeros(len(S) + (len(S)-1)*n_of_zeros)
do[::n_of_zeros+1] = S
print(do)
