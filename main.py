import sys
import statistics


def printStat():
    numStr = []
    f = open(sys.argv[1],"r")
    Lines = f.readlines()
    count = 0;
    for line in Lines:
        count += 1
        numStr.append(int(line))

    min = numStr
    min.sort()
    print(f'mean: {sum(numStr) / len(numStr)}')
    print(f'std: {statistics.stdev(numStr)}')
    print(f'min: {min[0]}')
    print(f'max: {min[-1]}')


if __name__ == '__main__':
    printStat()
