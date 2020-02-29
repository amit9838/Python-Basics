import math
import os
import re
import sys


n = int(input())
m = n % 2
if n >20 and m == 1:
    print("Weird")
elif 2 <= n < 5 and m == 0:
    print("Not Weird")
elif 6 <= n < 20 and m == 0:
    print("Weird")
elif n > 20:
    print("Not Weird")
else:
    print("Weied")
