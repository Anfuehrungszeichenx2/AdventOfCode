def addCon(graph,first,second):
    conns =graph.get(first,[])
    conns.append(second)
    graph[first] = conns
    return graph
if __name__ == "__main__":
    file = open('Task20.input', mode='r')
    lines = file.read().splitlines()
    lns = []
    a=0
    b=0
    current = ''
    lok = ''
    for i,line in enumerate(lines):
        tmp = []
        for j,char in enumerate(line):
            tmp.append(char)
        lns.append(tmp)

    for i,line in enumerate(lines):
        for j,char in enumerate(line):
        
            if char == 'S':
                a = i
                b = j
                if lns[a][b+1] == '-' or lns[a][b+1] == 'J' or lns[a][b+1] == '7':
                    current = lns[a][b+1]
                    b += 1
                    lok = 'left'

                elif lns[a][b-1] == '-' or lns[a][b-1] == 'L' or lns[a][b-1]== 'F':
                    current = lns[a][b+1]
                    b -= 1
                    lok = 'right'
                elif lns[a+1][b] == '|' or lns[a+1][b] == 'L' or lns[a+1][b] == 'J':
                    current = lns[a+1][b]
                    a += 1
                    lok = 'top'
                elif lns[a-1][b] == '|' or lns[a-1][b] == '7' or lns[a-1][b] == 'F':
                    current = lns[a-1][b]
                    a -= 1
                    lok = 'bot'
    loop = False
    graph = []
    counter = 0

    field = []

    for i in range(142):
        l = []
        for i in range(143):
            l.append(-1)
        field.append(l)
    field[a][b] = 9
    while loop == False:
        field[a][b] =current
        out = 0
        counter += 1
        if current == 'S':
            loop = True
            break

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

    counter = 0

    for l in field:
        if len(l)>0:
            inside = False
            insidec = 0
            for i in range(len(l)):
                cur = l[i]
                if cur != -1 and cur != '-':
                    if l[i-1] != -1:
                        insidec = 2

                    else:
                        insidec +=1


                if not inside:

                    if l[i] != -1:
                        if insidec % 2 != 0:
                            inside = True
                else:

                    if l[i] == -1:
                        counter +=1

                    elif l[i] != '-':
                        inside = False



    print(counter)




    i = -1