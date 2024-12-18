from functools import *
import operator

def main():
    return sum(map(abs, map(operator.sub, *map(sorted, zip(*((map(int, filter(lambda x: x != '', line.split(' ')))) for line in open("input.txt")))))))

print(main())
