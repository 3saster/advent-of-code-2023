pipeDict = { \
            '|':[(1,0),(-1,0)], \
            '-':[(0,1),(0,-1)], \
            'L':[(-1,0),(0,1)], \
            'J':[(-1,0),(0,-1)], \
            '7':[(1,0),(0,-1)], \
            'F':[(1,0),(0,1)], \
}

def getNextPoint(pos,curPoint,lastPoint):
    pipe = pos[curPoint[0]][curPoint[1]]
    p1,p2 = [tuple([c+m for c,m in zip(curPoint,move)]) for move in pipeDict[pipe]]
    return p1 if p1 != lastPoint else p2

def loopLength(pos,start):
    y,x = start
    nextPoint = None
    # Down
    if not nextPoint:
        if y+1 < len(pos):
            pipe = pos[y+1][x]
            if pipe in '|LJ':
                nextPoint = (y+1,x)
    # Up
    if not nextPoint:
        if y-1 >= 0:
            pipe = pos[y-1][x]
            if pipe in '|7F':
                nextPoint = (y-1,x)
    # Right
    if not nextPoint:
        if x+1 < len(pos[0]):
            pipe = pos[y][x+1]
            if pipe in '-J7':
                nextPoint = (y,x+1)
    # Left
    if not nextPoint:
        if x+1 >= 0:
            pipe = pos[y][x-1]
            if pipe in '-LF':
                nextPoint = (y,x-1)

    dist = 1
    corners = [start]
    while pos[nextPoint[0]][nextPoint[1]] != 'S':
        if pos[nextPoint[0]][nextPoint[1]] in 'LJ7F':
            corners.append(nextPoint)
        nextPoint, start = (getNextPoint(pos,nextPoint,start),nextPoint)
        dist += 1
    return dist,corners


def Part1(data):
    pos = data
    start = [(y,x) for y in range(len(pos)) for x in range(len(pos[0])) if pos[y][x] == 'S'][0]
    # Half loop length is distance to farthest point
    return loopLength(pos,start)[0]//2

def Part2(data):
    pos = data
    start = [(y,x) for y in range(len(pos)) for x in range(len(pos[0])) if pos[y][x] == 'S'][0]
    dist,corners = loopLength(pos,start)
    # Shoelace formula
    area = 0
    for i in range(len(corners)):
        y1,x1 = corners[i]
        y2,x2 = corners[(i+1)%len(corners)]
        area += 1/2 * (y1+y2) * (x1-x2)
    area = abs(area)
    # Pick's theorem
    return int(area + 1 - dist/2)