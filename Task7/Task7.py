if __name__ == "__main__":
    file = open('task7.input', mode='r')
    lines = file.read()
    lines = lines.splitlines()
    out = 0
    for line in lines:
        tmp = 0
        numbers,winners = line.split('|')
        numbers = numbers.split()
        winners = winners.split()
        counter = 0
        for number in numbers:
            if number in winners:

                tmp = pow(2,counter)
                counter += 1
        out += tmp
    print (out)
