import re
from math import prod

def getGameInfo(input):
    input = [l.split(': ')[1].split('; ') for l in input]
    games = []
    for game in input:
        for i in range(len(game)):
            cubes = {'red':0,'green':0,'blue':0}
            for colour in cubes.keys():
                if (num := re.findall(f"(\d+) {colour}",game[i])) != []:
                    cubes[colour] = int(num[0])
            game[i] = dict(cubes)
        games.append(game)
    return games

# For part 1
def isGameValid(game,max):
    for balls in game:
        for colour in max.keys():
            if balls[colour] > max[colour]:
                return False
    return True

# For part 2
def minGame(game):
    minBalls = {k:0 for k in game[0].keys()}
    for balls in game:
        for colour in minBalls.keys():
            minBalls[colour] = max( minBalls[colour],balls[colour] )
    return minBalls


def Part1(data):
    games = getGameInfo(data)
    maxes = {'red':12,'green':13,'blue':14}
    goodGames = [i+1 for i,game in enumerate(games) if isGameValid(game,maxes)]
    return sum(goodGames)
    
def Part2(data):
    games = getGameInfo(data)
    minGames = [minGame(game) for game in games]
    return sum( [prod(ballset.values()) for ballset in minGames] )