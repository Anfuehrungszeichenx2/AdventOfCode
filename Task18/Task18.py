if __name__ == "__main__":
    file = open('Task18.input', mode='r')
    lines = file.read().splitlines()
    out = 0
    for line in lines:
        line = line.split()
        line = [int(x) for x in line]
        lines = []
        lines.append(line.copy())
        check = True
        while check:
            new = []
            line = lines[len(lines)-1]
            for i in range(len(line)-1):
                new.append(line[i+1]-line[i])
            lines.append(new.copy())
            line = new
            if line.count(0) == len(line):
                check = False
            line.clear()
        lines.reverse()
        for i in range(len(lines)-1):
            a =lines[i+1][0]
            b =lines[i][0]
            lines[i+1].insert(0,a-b)
        lines.reverse()
        out += lines[0][0]
    print(out)