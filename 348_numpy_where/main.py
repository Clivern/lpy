# 348. numpy where
#
# np.where(cond, a, b) is elementwise if-then-else. clip limits values. unique returns
# sorted distinct items. These replace many Python loops.
#
# Run: python 348_numpy_where/main.py

import numpy as np
a = np.array([1, 2, 3, 4])
print(np.where(a % 2 == 0, a, 0))
print(np.clip(a, 2, 3), np.unique([1, 1, 2]))
