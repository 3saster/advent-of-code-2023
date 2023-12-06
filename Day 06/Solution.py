import re
from math import sqrt,floor,ceil,prod

# How many s such that (t-s)s > d, where s is seconds button is held down,
# t = time allowed, d = distance to beat
def ways2win(t,d):
    minS = 1/2*(t - sqrt( t**2 - 4*d ))
    maxS = 1/2*(t + sqrt( t**2 - 4*d ))
    return ceil(maxS-1) - floor(minS+1) + 1


def Part1(data):
    time,distance = [[int(string) for string in re.findall('\d+',d)] for d in data]
    ways2win(time[0],distance[0])
    raceWins = [ways2win(t,d) for t,d in zip(time,distance)]
    return prod(raceWins)
     
def Part2(data):
    time,distance = [[int(string) for string in re.findall('\d+',d.replace(' ',''))] for d in data]
    ways2win(time[0],distance[0])
    raceWins = [ways2win(t,d) for t,d in zip(time,distance)]
    return prod(raceWins)