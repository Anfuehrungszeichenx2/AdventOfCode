if __name__ == "__main__":
    allValidFields = []
    file = open('task5.input', mode='r')
    lines = file.read()
    nl = (2+len(lines)) * '.'
    lines = nl + '\n' + lines + '\n' + nl
    lines = lines.splitlines()
    for line in range(1,len(lines)-1):
        lineString = '.'+lines[line]+'.'
        for char in range(len(lineString)):
            if lineString[char] != '.' and  not lineString[char].isdigit():
                allValidFields.append(str(line-1)+'-'+str(char-1))
                allValidFields.append(str(line-1)+'-'+str(char))
                allValidFields.append(str(line-1)+'-'+str(char+1))
                allValidFields.append(str(line)+'-'+str(char-1))
                allValidFields.append(str(line)+'-'+str(char+1))
                allValidFields.append(str(line+1)+'-'+str(char-1))
                allValidFields.append(str(line+1)+'-'+str(char))
                allValidFields.append(str(line+1)+'-'+str(char+1))


    out = 0
    for line in range(1,len(lines)-1):
        lineString = '.'+lines[line]+'.'
        numToCheck  = 0
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
                if not lineString[char+1].isdigit():
                    if isValig:
                        out += int(numToCheck)
                        numToCheck = 0
    print(out)



