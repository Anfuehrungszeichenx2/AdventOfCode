from dataclasses import dataclass


from tqdm import tqdm
@dataclass
class map:
    change: int
    input: int
    output: int
    range: int
    min: int
    max: int


def splitDataBackwards(lines):
    lines = lines.splitlines()
    lines = lines[1:]
    out = []
    for line in lines:
        line = line.split()
        line = [int(i) for i in line]
        x = map(line[1] - line[0],line[0],line[1],line[2],line[0],line[0]+ line[2])
        
        out.append(x)
    return out
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
    out = 0
    '''
    for i in range(int(len(seeds))):
        if i %2!=0:
            out += seeds[i]
            for j in range(seeds[i],seeds[i]+seeds[i+1]):
                trueSeeds.append(j)
             #   i = 0
                #if j not in trueSeeds:
                    #trueSeeds.append(j)
'''

  #  seeds = trueSeeds

    
    seedToSoilx = splitDataBackwards(lines[1])
    soilToFertx = splitDataBackwards(lines[2])
    fertToWaterx = splitDataBackwards(lines[3])
    waterToLightx = splitDataBackwards(lines[4])
    lightToTempx = splitDataBackwards(lines[5])
    tempToHumx = splitDataBackwards(lines[6])
    humToLocx = splitDataBackwards(lines[7])

    for i in range(400000000):

        tmp = findOut(i, humToLocx)
        tmp = findOut(tmp, tempToHumx)
        tmp = findOut(tmp, lightToTempx)
        tmp = findOut(tmp, waterToLightx)
        tmp = findOut(tmp, fertToWaterx)
        tmp = findOut(tmp, soilToFertx)

        tmp = findOut(tmp,seedToSoilx)



        for j in range(len(seeds)):
            if j % 2 == 0:
                if tmp >= seeds[j] and tmp <= seeds[j] + seeds[j+1]:
                    print(i)
                    exit()



    exit()
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
