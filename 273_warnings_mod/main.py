# 273. warnings
#
# warnings.warn issues a warning without aborting. filterwarnings can error, ignore, or
# once. DeprecationWarning is how stdlib signals old APIs.
#
# Run: python 273_warnings_mod/main.py

import warnings
warnings.filterwarnings("error", category=UserWarning)
try:
    warnings.warn("careful", UserWarning)
except UserWarning as e:
    print(e)
