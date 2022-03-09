import numpy as np
A = input("Enter the array:").split()
A= np.array(list(map(int,A)))
B = input("Enter the array:").split()
B =np.array(list(map(int,B)))
checked = np.allclose(A,B)
print(checked)