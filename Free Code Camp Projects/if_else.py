import math
import os
import re
import sys


n = int(input().strip)
m = n % 2
if n == 1:
    message = "Weired"
elif 2 <= n < 5 and m == 0:
    message = "Not Weird"
elif 6 <= n < 20 and m == 0:
    message = "Weird"
elif n > 20:
    message = "Not Weird"

print(message)
