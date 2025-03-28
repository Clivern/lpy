# 326. signal
#
# signal.signal installs a handler for SIGINT and friends. Handlers are restricted; they
# should set a flag. Windows supports a smaller set than POSIX.
#
# Run: python 326_signal_mod/main.py

import signal
print(signal.SIGINT)
old = signal.getsignal(signal.SIGINT)
print(old is not None)
