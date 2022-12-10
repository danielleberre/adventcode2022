import fileinput

SIZE = 14

def alldiff(buffer):
    return len(set(buffer))==SIZE

buffer = []

for line in fileinput.input():
    index = 1
    for i in line:
        buffer.append(i)
        if len(buffer)>SIZE:
            buffer.pop(0)
            assert len(buffer)==SIZE
            if alldiff(buffer):
                print(index)
                buffer.clear()
                index = 1
                break
        index += 1

