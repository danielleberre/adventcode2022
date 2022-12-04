import sys

opponent = {'A':1,'B':2,'C':3}
me = {'X':1,'Y':2,'Z':3}

def handle_line(line):
    v1 = opponent[line[0]]
    v2 = me[line[2]]
    if v1==v2:
        return v2+3
    diff = v2-v1
    if diff==1 or diff==-2:
        return v2+6
    return v2



sum=0
for line in sys.stdin:
    sum += handle_line(line)
    print(sum)

print(sum)