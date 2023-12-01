import sys

if __name__ == "__main__":
    out = 0
    file = open('task2.input', mode='r')
    lines = file.read()
    lines = lines.splitlines()
    numbers = ['one','two','three','four','five','six','seven','eight','nine']
    fixxed = []
    for line in lines:
        word = ''
        numx = ''
        found = False
        for char in line:
            if found == True:
                break
            if char.isnumeric():
                numx += char
                break
            word += char
            for number in numbers:
                if word.find(number) != -1:
                    numx += str(numbers.index(number)+1)
                    word = word.replace(number,str(numbers.index(number)+1))
                    found = True
        word = ''
        found = False
        for char in reversed(line):
            if found == True:
                break
            if char.isnumeric():
                numx += char
                break
            word = char + word
            for number in numbers:
                if word.find(number) != -1:
                    numx += str(numbers.index(number)+1)
                    found = True

        fixxed.append(numx)



    for line in fixxed:

        tmp = ''
        for i in line:
            if i.isnumeric():
                tmp += i
        if len(tmp) == 1:
            tmp += tmp
        if len(tmp) > 2:
            out += int(tmp[0] + tmp[-1])
            print(tmp[0] + tmp[-1])
            continue
        print(tmp)
        out += int(tmp)
    print(out)