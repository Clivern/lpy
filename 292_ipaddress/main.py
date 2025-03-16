# 292. ipaddress
#
# ip_address parses IPv4/IPv6. ip_network understands CIDR. num_addresses and supernet are
# for inventory. hosts() skips network and broadcast.
#
# Run: python 292_ipaddress/main.py

import ipaddress
n = ipaddress.ip_network("10.0.0.0/30")
print(n.num_addresses, list(n.hosts()))
print(ipaddress.ip_address("127.0.0.1").is_loopback)
