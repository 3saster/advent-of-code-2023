def arrangements(line,info):
    if '?' in line:
        return arrangements( line.replace('?','#',1),info ) + arrangements( line.replace('?','.',1),info )
    else:
        runs = [len(l) for l in line.split('.') if l != '']
        return 1 if runs == info else 0


def Part1(data):
    line = [d.split()[0] for d in data]
    lineInfo = [[int(nums) for nums in d.split()[1].split(',')] for d in data]
    output = []
    for l,info in zip(line,lineInfo):
        output.append( arrangements(l,info) )
    return sum(output)

def Part2(data):
    pass