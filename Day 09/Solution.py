from itertools import pairwise

def extrapolateValue(row,flipped=False):
    layers = [row]
    while min(layers[-1]) != 0 or max(layers[-1]) != 0 :
        bottom = [y - x for x, y in pairwise(layers[-1])]
        layers.append( bottom )
    layers = list(reversed(layers))
    if flipped:
        layers[0].insert(0,0)
    for i in range(len(layers)-1):
        if not flipped:
            layers[i+1].append( layers[i+1][-1] + layers[i][-1] )
        else:
            layers[i+1].insert(0, layers[i+1][0] - layers[i][0] )
    return layers[-1][-1] if not flipped else layers[-1][0]


def Part1(data):
    layers = [ [int(num) for num in d.split()] for d in data ]
    return sum( [extrapolateValue(row,False) for row in layers] )

def Part2(data):
    layers = [ [int(num) for num in d.split()] for d in data ]
    return sum( [extrapolateValue(row,True) for row in layers] )