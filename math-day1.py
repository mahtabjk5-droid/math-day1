import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

a = np.array([3, 4])
b = np.array([1, 2])

print("Dot:", np.dot(a, b))
print("L2:", np.linalg.norm(a))
print("L1:", np.linalg.norm(a, ord=1))
print("Cosine:", cosine_similarity([a], [b]))