import fileinput


def check(x,y):
    visible = True
    for i in range(x):
        if grid[y][i]>=grid[y][x]:
            visible = False
            break
    if visible:
        return 1
    visible = True
    for i in range(x+1,nb_cols):
        if grid[y][i]>=grid[y][x]:
            visible = False
            break
    if visible:
        return 1
    visible = True
    for i in range(y):
        if grid[i][x]>=grid[y][x]:
            visible = False
            break
    if visible:
        return 1
    visible = True
    for i in range(y+1,nb_rows):
        if grid[i][x]>=grid[y][x]:
            visible = False
            break
    if visible:
        return 1
    return 0

def scenic_score(x,y):
    score_left = 0
    for i in range(x):
        score_left += 1
        if grid[y][x-i-1]>=grid[y][x]:
            break
        
    score_right = 0
    for i in range(x+1,nb_cols):
        score_right += 1
        if grid[y][i]>=grid[y][x]:
            break
        
    score_up = 0
    for i in range(y):
        score_up += 1
        if grid[y-i-1][x]>=grid[y][x]:
            break
        
    score_down = 0
    for i in range(y+1,nb_rows):
        score_down += 1
        if grid[i][x]>=grid[y][x]:
            break
        
    return score_left * score_right * score_up * score_down

grid = []
for line in fileinput.input():
    grid.append([int(j) for j in line.strip()])

nb_rows = len(grid)
nb_cols = len(grid[0])

visibles = nb_rows*2+(nb_cols-2)*2

for y in range(1,nb_rows-1):
    for x in range(1,nb_cols-1):
        visibles += check(x,y)


print(visibles)
scenic_scores = []

for y in range(1,nb_rows-1):
    for x in range(1,nb_cols-1):
        scenic_scores.append(scenic_score(x, y))
scenic_scores.sort()

print(scenic_scores[-1])