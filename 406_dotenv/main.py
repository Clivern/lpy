# 406. python-dotenv
#
# load_dotenv() reads .env into os.environ without overwriting by default. dotenv_values()
# returns a dict. Keep .env out of git.
#
# Run: python 406_dotenv/main.py

from pathlib import Path
import tempfile
from dotenv import dotenv_values
with tempfile.TemporaryDirectory() as d:
    p = Path(d) / ".env"
    p.write_text("TOKEN=abc\n", encoding="utf-8")
    print(dotenv_values(p)["TOKEN"])
