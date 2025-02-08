# 174. format specs
#
# format(x, spec) and f"{x:spec}" share Mini-language: width, align, fill, precision,
# type. d o x b for ints; f e g for floats; % for percent.
#
# Run: python 174_format_spec/main.py

print(format(42, "08d"), f"{42:x}", f"{3.14159:6.2f}")
print(f"{'hi':>6}", f"{0.25:.1%}")
print("{0} {1}".format("a", "b"))
