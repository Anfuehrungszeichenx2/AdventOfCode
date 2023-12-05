if __name__ == "__main__":
    file = open('task3.input', mode='r')
    lines = file.read()
    lines = lines.splitlines()
    out = 0
    gRed = 12
    gGreen = 13
    gBlue = 14
    colorCheck = ['red', 'green', 'blue']
    for line in lines:
        red = 0
        green = 0
        blue = 0
        line += ','
        line = line.split()
        check = True

        for color in range(2, len(line)):
            if color % 2 == 0:
                continue
            if line[color][:-1] not in colorCheck:
                check = False
                break
            else:
                if line[color][:-1] == 'red':
                    if int(line[color - 1]) > gRed:
                        check = False
                elif line[color][:-1] == 'blue':
                    if int(line[color - 1]) > gBlue:
                        check = False
                elif line[color][:-1] == 'green':
                    if int(line[color - 1]) > gGreen:
                        check = False

        if check == True:
            out += int(line[1][:-1])
    print(out)
