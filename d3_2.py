import sys
import string

priorities = dict((i, (j+1))
                  for i, j in zip(string.ascii_lowercase+string.ascii_uppercase, range(52)))

group_line = 1


def handle_line(line):
    global group_line
    global seen
    if group_line == 1:
        seen = [0 for i in range(53)]
    seenb = [False for i in range(53)]
    for i in range(len(line)-1):
        priority = priorities[line[i]]
        seenb[priority] = True
    for i in range(53):
        if seenb[i]:
            seen[i] += 1
        if seen[i] == 3:
            print(seen)
            group_line = 1
            return i
    print(seen)
    group_line += 1
    return 0


sum = 0
for line in sys.stdin:
    sum += handle_line(line)

print(sum)
