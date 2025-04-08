# 389. Jinja2 filters
#
# |e escapes. |join, |length, and custom filters via Environment.filters. Filters are
# functions: value is the left side.
#
# Run: python 389_jinja2_filter/main.py

from jinja2 import Environment
env = Environment()
t = env.from_string("{{ names|join(', ') }} ({{ names|length }})")
print(t.render(names=["Ada", "Alan"]))
