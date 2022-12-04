import sys

opponent = {'A': 1, 'B': 2, 'C': 3}
me = {'X': 1, 'Y': 2, 'Z': 3}


def handle_line(line):
    v1 = opponent[line[0]]
    v2 = me[line[2]]
    if v2 == 2:
        return v1+3
    if v2 == 1:
        if (v1>1):
            return v1-1
        return 3
    # v2==3:
    if (v1 < 3):
        return v1+1+6
    return 7


sum = 0
for line in sys.stdin:
    sum += handle_line(line)
    print(sum)

print(sum)
