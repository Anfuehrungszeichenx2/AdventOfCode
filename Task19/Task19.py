def addCon(graph,first,second):
    conns =graph.get(first,[])
    conns.append(second)
    graph[first] = conns
    return graph
if __name__ == "__main__":
    file = open('Task19.input', mode='r')
    lines = file.read().splitlines()
    lns = []
    a=0
    b=0
    for i,line in enumerate(lines):
        tmp = []
        for j,char in enumerate(line):
            tmp.append(char)
            if char == 'S':
                a = i
                b = j

        lns.append(tmp)

    loop = False
    graph = []
    current = '7'
    lok = ''
    counter = 0
    a = 25
    b = 33
    lok = 'left'
    while loop == False:
        counter += 1
        if current == 'S':
            loop = True

        elif current == '|':
            if lok == 'top':
                current = lns[a+1][b]
                a += 1
            if lok == 'bot':
                current = lns[a-1][b]
                a += -1
        elif current == '-':
            if lok == 'left':
                current = lns[a][b+1]
                b+=1
            else:
                current = lns[a][b-1]
                b-=1
        elif current == 'L':
            if lok == 'top':
                lok = 'left'
                current = lns[a][b+1]
                b += 1
            else:
                lok = 'bot'
                current = lns[a-1][b]
                a -= 1
        elif current == 'J':
            if lok == 'top':
                lok = 'right'
                current = lns[a][b-1]
                b -= 1
            else:
                lok = 'bot'
                current = lns[a-1][b]
                a -= 1
        elif current == '7':
            if lok == 'left':
                lok = 'top'
                current = lns[a+1][b]
                a += 1
            else:
                lok = 'right'
                current = lns[a][b-1]
                b -=1
        elif current == 'F':
            if lok == 'right':
                lok = 'top'
                current = lns[a+1][b]
                a += 1
            else:
                lok = 'left'
                current = lns[a][b+1]
                b += 1
    print(int(counter/2))



    i = -1