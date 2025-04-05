# 387. PyYAML dump
#
# default_flow_style=False is block style. sort_keys keeps diffs stable.
# allow_unicode=True writes café instead of escapes.
#
# Run: python 387_yaml_dump/main.py

import yaml
print(yaml.safe_dump({"items": [1, 2], "name": "café"}, sort_keys=True, allow_unicode=True).strip())
