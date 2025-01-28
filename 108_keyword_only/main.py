# 108. Keyword-only parameters
#
# Parameters after a bare * must be passed by name. That keeps call sites readable when
# several booleans would otherwise be positional.
#
# Run: python 108_keyword_only/main.py

def connect(host, *, timeout=1.0, tls=True):
    return host, timeout, tls

print(connect("db", timeout=2.5))
