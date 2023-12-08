import re
from math import lcm
from functools import reduce

def pathDist(pathDict,dir,startingPos,endingPos=None):
    i = 0
    pos = startingPos
    if endingPos:
        endCond = lambda p,e: p == e
    else:
        endCond = lambda p,e: p[-1] == 'Z'

    while not endCond(pos,endingPos):
        if dir[i%len(dir)] == 'L':
            pos = pathDict[pos][0]
        else:
            pos = pathDict[pos][1]
        i += 1
    return i

pathDict = dict()
dir = list()
def Part1(data):
    global pathDict
    global dir
    
    dir = data[0]
    paths = [d.split(' = ') for d in data[2:]]
    pathDict = dict()
    for path in paths:
        pathDict[path[0]] = re.findall("(\w+)",path[1])
    return pathDist(pathDict,dir,'AAA','ZZZ')


def Part2(data):
    global pathDict
    global dir

    # The data seems to fit the assumption that the distance
    # from a start node to an endnode is the same as from that
    # endnode to another endnode, which is itself
    pathConds = [pathDist(pathDict,dir,p) for p in pathDict.keys() if p[-1]=='A']
    return reduce(lcm,pathConds)