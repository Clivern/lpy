# 238. random
#
# random.random() is [0.0, 1.0). randint is inclusive. choice, sample, and shuffle work on
# sequences. seed makes a run reproducible. secrets is for tokens.
#
# Run: python 238_random_mod/main.py

import random
random.seed(0)
print(random.randint(1, 6), random.choice("abc"))
xs = [1, 2, 3, 4]
print(random.sample(xs, 2))
