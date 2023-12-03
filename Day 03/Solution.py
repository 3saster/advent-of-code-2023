import re
from collections import defaultdict
from math import prod

def isPart(schematic,pos,gears=None):
    base = '0123456789.'

    # Slightly inefficient but easy
    for y in range(pos[0]-1,pos[0]+2):
        for x in range(pos[1][0]-1,pos[1][1]+1):
            if (symbol:=schematic[y][x]) not in base:
                # for part 2
                if gears != None and symbol == "*":
                    gears[(y,x)].append( int(schematic[pos[0]][pos[1][0]:pos[1][1]]) )
                return True
    return False, gears


gears = defaultdict(lambda: [])

def Part1(data):
    global gears
    # Add dots on border
    schematic = ["."*len(data[0])] + ["."+l+"." for l in data] + ["."*len(data[0])]

    numbers = [ [i,r.span()] for i,line in enumerate(schematic) for r in re.finditer("(?<!\d)(\d+)",line) ]
    partNumbers = [n for n in numbers if isPart(schematic,n,gears)]
    partNumbers = [int(schematic[line][span[0]:span[1]]) for line,span in partNumbers]
    return sum(partNumbers)
    
def Part2(data):
    global gears
    return sum( [prod(v) for k,v in gears.items() if len(v) == 2] )