import numpy as np
from pycocotools import mask as m

n_a = np.random.normal(size=(10, 10))
b_a = np.array(n_a > 0.5, dtype=np.bool, order='F')
e_a = m.encode(b_a)
d_a = m.decode(e_a)
