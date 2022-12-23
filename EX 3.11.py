# Write a function validate_phone(tmp_str) to validate a given phone number.

# Test data:
# Input: ab122
# Output: False

# Test data:
# Input: 0932095456
# Output: True

# Test data:
# Input: 02836229888
# Output: True

import re

def validate_phone(tmp_str):
    a = "[0-9]*$"
    state = bool(re.match(a, tmp_str))
    return state
tmp_str = input()
print(validate_phone(tmp_str))