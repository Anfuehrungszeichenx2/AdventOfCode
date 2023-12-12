from dataclasses import dataclass
from math import lcm
@dataclass
class Point:
    name: str
    left: str
    right: str


def getRoundLen(start,input,points):
    check = False
    counter = 0
    while check == False:
        for char in input:
            x = list(filter(lambda p: p.name == start,points))[0]
            counter += 1
            if char == 'L':
                start = x.left
            else:
                start = x.right
            if start[2] == 'Z':
                check = True
                break
    return counter

if __name__ == "__main__":
    file = open('Task16.input', mode='r')
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
    meow = []
    for p in points:
        if p.name[2] == 'A':
            meow.append(getRoundLen(p.name,input,points))
    nums = []
    print(lcm(meow[0],meow[1],meow[2],meow[3],meow[4],meow[5]))
