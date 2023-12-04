def Part1(data):
    pairs = [s.split(": ")[-1].split(' | ') for s in data]
    scores = []
    for pair in pairs:
        scratchcard = {int(n) for n in pair[0].split(' ') if n != ''}
        numbers     = {int(n) for n in pair[1].split(' ') if n != ''}
        numMatches = len(scratchcard & numbers)
        scores.append( 0 if numMatches==0 else 2**(numMatches-1) )
    return sum(scores)
    
def Part2(data):
    pairs = [s.split(": ")[-1].split(' | ') for s in data]

    scores   = [0]*len(pairs)
    numCards = [1]*len(pairs)
    # Count matches
    for i,pair in enumerate(pairs):
        scratchcard = {int(n) for n in pair[0].split(' ') if n != ''}
        numbers     = {int(n) for n in pair[1].split(' ') if n != ''}
        scores[i] = len(scratchcard & numbers)
    # Count cards
    for i in range(len(pairs)):
        for cardNum in range(i+1,min(i+scores[i]+1,len(pairs))):
            numCards[cardNum] += numCards[i]
    return sum(numCards)