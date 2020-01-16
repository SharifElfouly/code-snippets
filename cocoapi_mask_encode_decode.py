import numpy as np
from pycocotools import mask as m

n_a = np.random.normal(size=(10, 10))
b_a = np.array(n_a > 0.5, dtype=np.bool, order='F')
e_a = m.encode(b_a)
d_a = m.decode(e_a)

# Decode byte string rle encoded mask.
sz = pred['mask']['size']
c = pred['mask']['counts'][2:-1]
es = str.encode(c)
t = {'size': [450, 800], 'counts': es}
dm = m.decode(t)
