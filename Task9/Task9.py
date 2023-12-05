from dataclasses import dataclass

@dataclass
class map:
    change: int
    input: int
    output: int
    range: int
    min: int
    max: int


def splitData(lines):
    lines = lines.splitlines()
    lines = lines[1:]
    out = []
    for line in lines:
        line = line.split()
        line = [int(i) for i in line]
        x = map(line[0] - line[1],line[1],line[0],line[2],line[1],line[1]+line[2])
        out.append(x)
    return out
def findOut(input,x):
    check = False
    for i in x:
        if input >= i.min and input <= i.max:
            check = True
            input += i.change
            return input
    return input

if __name__ == "__main__":
    file = open('Task9.input', mode='r')
    lines = file.read().split('\n\n')

    seeds = lines[0].split()
    seeds = seeds[1:]
    seeds = [int(i) for i in seeds]
    trueSeeds = []
    for i in range(seeds[0],seeds[0]+seeds[1]):
        trueSeeds.append(i)
    for i in range(seeds[2],seeds[2]+seeds[3]):
        trueSeeds.append(i)
    seeds = trueSeeds
    seedToSoil = splitData(lines[1])
    soilToFert = splitData(lines[2])
    fertToWater = splitData(lines[3])
    waterToLight = splitData(lines[4])
    lightToTemp = splitData(lines[5])
    tempToHum = splitData(lines[6])
    humToLoc = splitData(lines[7])
    lowest = -1
    for seed in seeds:
        seed = int(seed)
        tmp = findOut(seed,seedToSoil)
        tmp = findOut(tmp,soilToFert)
        tmp = findOut(tmp,fertToWater)
        tmp = findOut(tmp,waterToLight)
        tmp = findOut(tmp,lightToTemp)
        tmp = findOut(tmp,tempToHum)
        tmp = findOut(tmp,humToLoc)
        if lowest == -1:
            lowest = tmp
        else:
            if tmp < lowest:
                lowest = tmp
    print(lowest)
    tt = 0
