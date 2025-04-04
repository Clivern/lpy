# 386. PyYAML load
#
# yaml.safe_load parses YAML without executing tags. safe_dump writes. YAML is a superset
# of JSON for many documents. Prefer safe_* over load/dump.
#
# Run: python 386_pyyaml_load/main.py

import yaml
data = yaml.safe_load("name: Ada\nyear: 1815\n")
print(data["name"], yaml.safe_dump(data, sort_keys=True).strip())
