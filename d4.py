import sys
import re

def handle_line(line):
    a1,b1,a2,b2 = map(int,re.match(r'(\d+)-(\d+),(\d+)-(\d+)',line).groups())
    assert a1<=b1
    assert a2<=b2
    if (a1 <= a2 <= b2 <= b1 or a2 <= a1 <= b1 <= b2):
        return 1
    return 0

sum = 0
for line in sys.stdin:
    sum += handle_line(line)

print(sum)
