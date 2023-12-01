def FrontMatch(string: str, strDict: dict):
    """
    Returns the value of the first matching key in the string.
    """
    matchInd = float('inf')
    matchVal = ""
    for k in strDict.keys():
        i = string.find(k)

        if i != -1 and i < matchInd:
            matchInd = i
            matchVal = k
            
    try : return strDict[matchVal]
    except KeyError: return 0

def BackMatch(string: str, strDict: dict):
    """
    Returns the value of the last matching key in the string.
    """
    matchInd = -1
    matchVal = ""
    for k in strDict.keys():
        try: i = string.rindex(k)
        except ValueError: i = -1

        if i != -1 and i > matchInd:
            matchInd = i
            matchVal = k
            
    try : return strDict[matchVal]
    except KeyError: return 0


def Part1(data):
    data = [l.strip() for l in data]
    strDict = {  "1":1,   "2":2,     "3":3,    "4":4,    "5":5,   "6":6,     "7":7,     "8":8,    "9":9 }
    return sum( FrontMatch(str,strDict)*10 + BackMatch(str,strDict) for str in data )

def Part2(data):
    data = [l.strip() for l in data]
    strDict = {  "1":1,   "2":2,     "3":3,    "4":4,    "5":5,   "6":6,     "7":7,     "8":8,    "9":9, \
               "one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}
    return sum( FrontMatch(str,strDict)*10 + BackMatch(str,strDict) for str in data )