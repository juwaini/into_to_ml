# %matplotlib inline

import numpy as np
from scipy import sparse
import matplotlib.pyplot as plt

x = np.array([[1, 2, 3], [4, 5, 6]])
print(f'\nx: {x}\n')

# Create a 2D numpy array with a diagonal of ones, and zeros everywhere else

eye = np.eye(4)
print(f'numpy array: \n{eye}\n')

# Convert the numpy array to a scip sparse matrix in CSR format
# Only the non-zero entries are stored
sparse_matrix = sparse.csr_matrix(eye)
print(f'Scipy sparse CSR matrix:\n{sparse_matrix}\n')

data = np.ones(4)
row_indices = np.arange(4)
col_indices = np.arange(4)
eye_coo = sparse.coo_matrix((data, (row_indices, col_indices)))
print(f'COO representation:\n{eye_coo}\n')

# Generate a sequence of numbers from -10 to 10 with 100 steps in between
x = np.linspace(-10, 10, 100)

# Create a second array using sine
y = np.sin(x)

# The plot function makes a line chart of one array against another
plt.plot(x, y, marker='x')
