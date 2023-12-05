if __name__ == "__main__":
    allValidFields = []
    file = open('Task6.input', mode='r')
    lines = file.read()
    nl = (2+len(lines)) * '.'
    lines = nl + '\n' + lines + '\n' + nl
    lines = lines.splitlines()
    for line in range(1,len(lines)-1):
        lineString = '.'+lines[line]+'.'
        for char in range(len(lineString)):
            if lineString[char]  ==  '*':
                allValidFields.append(str(line-1)+'-'+str(char-1))
                allValidFields.append(str(line-1)+'-'+str(char))
                allValidFields.append(str(line-1)+'-'+str(char+1))
                allValidFields.append(str(line)+'-'+str(char-1))
                allValidFields.append(str(line)+'-'+str(char+1))
                allValidFields.append(str(line+1)+'-'+str(char-1))
                allValidFields.append(str(line+1)+'-'+str(char))
                allValidFields.append(str(line+1)+'-'+str(char+1))


    out = 0
    gear = int((len(allValidFields)/8)) * [0]
    for line in range(1,len(lines)-1):
        lineString = '.'+lines[line]+'.'
        numToCheck  = 0
        validId = 0
        isValig = False
        for char in range(len(lineString)):
            if lineString[char].isdigit():
                if not lineString[char-1].isdigit():
                    numToCheck = lineString[char]
                    isValig = False
                else:
                    numToCheck += lineString[char]
                if str(line) + '-'+str(char) in allValidFields:
                    isValig = True
                    validId = int(allValidFields.index(str(line) + '-'+str(char))/8 )
                if not lineString[char+1].isdigit():
                    if isValig:
                        if gear[validId] == 0:
                            gear[validId] = int(numToCheck)
                        else:
                            out += gear[validId] * int(numToCheck)
                        numToCheck = 0
    print(out)



