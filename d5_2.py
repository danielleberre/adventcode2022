import sys
import re


def handle_preamble(lines):
    global numbers
    numbers = map(int,re.findall(r"\d+", lines.pop()))
    crates = dict((i, [])
                  for i in numbers)
    while len(lines) > 0:
        line = lines.pop()
        i = 0
        crate = 1
        while i < len(line):
            content = line[i:i+3]
            if '' != content.rstrip():
                crates[crate].append(content[1:2])
            i += 4
            crate += 1
    return crates


def handle_line(line):
    quantity, source, target = map(int, re.match(
        r"move (\d+) from (\d+) to (\d+)", line).groups())
    index = len(crates[target])
    for i in range(quantity):
        crates[target].insert(index,crates[source].pop())

preamble = True
lines = []
numbers = []

for line in sys.stdin:
    if '' == line.rstrip():
        preamble = False
        crates = handle_preamble(lines)
        continue
    if preamble:
        lines.append(line)
    else:
        handle_line(line)

top = ''
for i in crates.keys():
    top += crates[i][-1]
print(top)

print(crates)