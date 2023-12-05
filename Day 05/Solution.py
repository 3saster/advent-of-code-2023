def parseData(data):
    seeds = [int(seed) for seed in data[0].split(': ')[1].split()]
    maps = []

    isMap = False
    for line in data[2:]:
        if line == '':
            isMap = False
            continue
        if isMap:
            maps[-1].append( [int(loc) for loc in line.split()] )
            continue
        if 'map' in line:
            maps.append( [] )
            isMap = True
            continue

    return seeds, maps

def applyMap(input,map):
    output = input
    for end,start,range in map:
        if start <= output < start + range:
            output += end - start
            break
    return output

# The idea here is that when a mapping is viewed as a function,
# we have f(x) = x+const(x), where const(x) is a piecewise constant function.
# If x is a range of consecutive values, then f(x) will still be a
# range of consecutive values as long as a jump discontinuity of const
# is not crossed. Thus, if we can find the jump discontinuities of const
# and split x into sets of consecutive values that do not cross the discontinuities,
# then the output sets will also be consecutive, with the first value of the output being
# the mapping of the first value of the input.
def applyMapRange(firstSeed,range,map):
    # Find points where offset changes
    crits = set()
    for m in map:
        crits.add(m[1])
        crits.add(m[1]+m[2])
    crits = sorted(crits)

    importantInputs = sorted( {firstSeed} | {c for c in crits if firstSeed <= c < firstSeed+range} )
    rangeSets = [b-a for a,b in zip(importantInputs[:-1],importantInputs[1:])]
    rangeSets.append( range-sum(rangeSets) )

    outSeed  = [applyMap(s,map) for s in importantInputs]
    return outSeed,rangeSets


def Part1(data):
    seeds,maps = parseData(data)
    for map in maps:
        seeds = [applyMap(seed,map) for seed in seeds]
    return min(seeds)
     
def Part2(data):
    seedAndRange,maps = parseData(data)
    seeds  = seedAndRange[0::2]
    ranges = seedAndRange[1::2]
    for map in maps:
        newData = [applyMapRange(s,r,map) for s,r in zip(seeds,ranges)]
        # List Flattening
        seeds  = [p for p2 in [pair[0] for pair in newData] for p in p2]
        ranges = [p for p2 in [pair[1] for pair in newData] for p in p2]
    return min(seeds)