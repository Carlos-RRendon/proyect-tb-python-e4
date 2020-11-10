#!/usr/bin/env python

import re
import string
import random

bus_width = int(32)
bus_range = 2 ** bus_width
random_number = random.randint(0, (bus_range - 1))

# Hexadecimal
hex_string = hex(random_number)
hex_base = str(bus_width) + ("'h")
hex_string = hex_string.replace("0x", hex_base)

# Octal
oct_string = oct(random_number)
oct_base = str(bus_width) + ("'o")
oct_string = oct_string.replace("0o", oct_base)

# Binary
bin_string = bin(random_number)
bin_base = str(bus_width) + ("'b")
bin_string = bin_string.replace("0b", bin_base)


print(random_number)
print(hex_string)
print(oct_string)
print(bin_string)