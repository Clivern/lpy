# 385. tqdm
#
# tqdm(iterable) wraps a loop with a progress bar. write() prints without breaking the
# bar. disable=True is for tests and logs.
#
# Run: python 385_tqdm_bar/main.py

from tqdm import tqdm
total = 0
for n in tqdm(range(4), disable=True):
    total += n
print(total)
