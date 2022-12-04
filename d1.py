import sys

def sort():
    for i in range(3):
        if (sum>bestsum[i]):
            # first should be smallest
            # third largest
            for j in range (i+1,3):
                if sum>bestsum[j]:
                    bestsum[j-1] = bestsum[j]
                else:
                    j-=1
                    break
            bestsum[j] = sum
            break

bestsum=[0,0,0]
sum=0
for line in sys.stdin:
    if '' == line.rstrip():
        sort()
        sum = 0
    else:
        sum += int(line)
sort()
print(bestsum[0]+bestsum[1]+bestsum[2])