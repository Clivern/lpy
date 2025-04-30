# 069. YAML and Jinja2
#
# safe_load/dump and Jinja2 render, filters, and control.
#
# Run: python 069_templates/main.py

# --- pyyaml load ---
import yaml
data = yaml.safe_load("name: Ada\nyear: 1815\n")
print(data["name"], yaml.safe_dump(data, sort_keys=True).strip())

# --- yaml dump ---
import yaml
print(yaml.safe_dump({"items": [1, 2], "name": "café"}, sort_keys=True, allow_unicode=True).strip())

# --- jinja2 render ---
from jinja2 import Template
t = Template("hello {{ name }}")
print(t.render(name="Ada"))

# --- jinja2 filter ---
from jinja2 import Environment
env = Environment()
t = env.from_string("{{ names|join(', ') }} ({{ names|length }})")
print(t.render(names=["Ada", "Alan"]))

# --- jinja2 if ---
from jinja2 import Template
t = Template("{% for n in xs if n % 2 == 0 %}{{ n }}{% endfor %}")
print(t.render(xs=[1, 2, 3, 4]))
