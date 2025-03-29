# 344. numpy broadcasting
#
# Shapes (3, 1) and (1, 4) add to (3, 4). A scalar stretches. Incompatible shapes raise.
# Broadcasting avoids tile and repeat in most numeric code.
#
# Run: python 344_numpy_broadcast/main.py

import numpy as np
col = np.arange(3).reshape(3, 1)
row = np.arange(4).reshape(1, 4)
print((col + row).shape)
print(col + row)
