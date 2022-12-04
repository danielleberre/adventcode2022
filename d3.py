import sys
import string

priorities = dict((i, (j+1)) for i, j in zip(string.ascii_lowercase+string.ascii_uppercase, range(52)))

print(priorities)

def handle_line(line):
    seen = [False for i in range(53)]
    middle = len(line)//2
    for i in range(middle):
        seen[priorities[line[i]]] = True
    for i in range(middle):
        priority = priorities[line[middle+i]]
        if (seen[priority]):
            return priority
    raise RuntimeError("Aucune lettre en commun trouvée")


sum = 0
for line in sys.stdin:
    sum += handle_line(line)
    print(sum)

print(sum)
