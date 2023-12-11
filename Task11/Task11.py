if __name__ == "__main__":
    file = open('Task11.input', mode='r')
    lines = file.read().splitlines()
    list = []
    lines[0] = lines[0].split()
    lines[1] = lines[1].split()
    lines[0] = lines[0][1:]
    lines[1] = lines[1][1:]
    out = 1
    for i in range(len(lines[1])):
        time = int(lines[0][i])
        winner = int(lines[1][i])
        coutn = 0
        for j in range(time):
            len = ((time)-j) * j
            if len > winner:
                coutn += 1
        if coutn == 0:
            coutn = 1
        out = coutn * out
    print(out)