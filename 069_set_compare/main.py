# 069. Set comparisons
#
# <= is issubset, >= is issuperset. < and > are proper (not equal). isdisjoint is true
# when the intersection is empty. == tests equality of members.
#
# Run: python 069_set_compare/main.py

a, b, c = {1, 2}, {1, 2, 3}, {1, 2}
print(a <= b, a < b, a <= c, a < c)
print(b >= a, a.isdisjoint({9}), a == c)
