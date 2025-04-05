# 388. Jinja2 render
#
# Template.render interpolates {{ name }}. Environment from a dict of strings is
# FileSystemLoader's cousin. autoescape=True is for HTML.
#
# Run: python 388_jinja2_render/main.py

from jinja2 import Template
t = Template("hello {{ name }}")
print(t.render(name="Ada"))
