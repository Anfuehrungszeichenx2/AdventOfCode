import sys

if __name__ == "__main__":
    out = 0
    file = open('../task1.input', mode='r')
    lines = file.read()
    lines = lines.splitlines()

    for line in lines:

        tmp = ''
        for i in line:
            if i.isnumeric():
                tmp += i
        if len(tmp) == 1:
            tmp += tmp
        if len(tmp) > 2:
            out += int(tmp[0] + tmp[-1])
            continue
        print(tmp)
        out += int(tmp)
    print(out)