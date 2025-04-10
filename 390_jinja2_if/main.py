# 390. Jinja2 control
#
# {% if %} {% for %} {% endif %} is the statement syntax. Whitespace control with - strips
# newlines. Keep logic in Python when it grows.
#
# Run: python 390_jinja2_if/main.py

from jinja2 import Template
t = Template("{% for n in xs if n % 2 == 0 %}{{ n }}{% endfor %}")
print(t.render(xs=[1, 2, 3, 4]))
