def distBetween(g1,g2,emptyRows,emptyCols, emptySize = 1):
    yDiff = abs(g2[0] - g1[0]) + (emptySize-1)*sum( 1 for y in emptyRows if min(g1[0],g2[0]) < y < max(g1[0],g2[0]) )
    xDiff = abs(g2[1] - g1[1]) + (emptySize-1)*sum( 1 for x in emptyCols if min(g1[1],g2[1]) < x < max(g1[1],g2[1]) )
    return xDiff + yDiff


galaxies  = []
emptyCols = []
emptyRows = []

def Part1(data):
    global galaxies
    global emptyCols
    global emptyRows

    space = data
    # Fill galaxies, empty rows, and empty columns
    for y in range(len(space)):
        for x in range(len(space[0])):
            if data[y][x] == '#':
                galaxies.append( (y,x) )
    for y in range(len(space)):
        if '#' not in space[y]:
            emptyRows.append(y)
    for x in range(len(space[0])):
        if '#' not in [*zip(*space)][x]:
            emptyCols.append(x)

    distDict = dict()
    for g1 in galaxies:
        for g2 in galaxies:
            # Impose "canonical" order
            if g1 < g2:
                distDict[(g1,g2)] = distBetween(g1,g2,emptyRows,emptyCols,2)
    return sum(distDict.values())

def Part2(data):
    global galaxies
    global emptyCols
    global emptyRows

    distDict = dict()
    for g1 in galaxies:
        for g2 in galaxies:
            # Impose "canonical" order
            if g1 < g2:
                distDict[(g1,g2)] = distBetween(g1,g2,emptyRows,emptyCols,1000000)
    return sum(distDict.values())