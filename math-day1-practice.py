import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Problem 1
print("P1:", np.dot([1,2], [3,4]))

# Problem 2
print("P2:", np.dot([1,0], [0,1]))

# Problem 3
print("P3:", np.dot([2,3], [4,1]))

# Problem 4
print("P4:", cosine_similarity([[1,1]], [[1,1]])[0][0])

# Problem 5
print("P5:", cosine_similarity([[1,0]], [[-1,0]])[0][0])
