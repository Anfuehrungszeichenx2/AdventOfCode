from dataclasses import dataclass
@dataclass
class Point:
    name: str
    left: str
    right: str



if __name__ == "__main__":
    file = open('Task15.input', mode='r')
    lines = file.read().splitlines()
    points = []
    input = lines[0]
    for i in range(2,len(lines)):
        line = lines[i].split()
        name = line[0]
        left = line[2][:-1]
        left = left[1:]
        right = line[3][:-1]
        points.append(Point(name,left,right))
    i = 0
    point = 'AAA'
    counter = 0
    while point != 'ZZZ':
        for char in input:
            x = list(filter(lambda p: p.name == point,points))[0]
            counter += 1
            if char == 'L':
                point = x.left
            else:
                point = x.right

    print(counter)