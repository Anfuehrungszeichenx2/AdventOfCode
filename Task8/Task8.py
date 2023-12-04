if __name__ == "__main__":
    file = open('Task8.input', mode='r')
    lines = file.read()
    lines = lines.splitlines()
    out = 0
    amounts = len(lines) * [1]

    for j,line in enumerate(lines):
        tmp = 0
        count = 0
        numbers,winners = line.split('|')
        numbers = numbers.split()
        winners = winners.split()
        for i,number in enumerate(numbers):
            if number in winners:
                count += 1
        for win in range(count):
            amounts[j+win+1] += amounts[j]
    print (sum(amounts))
