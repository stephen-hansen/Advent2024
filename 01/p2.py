from functools import *
from collections import Counter
import operator

def main():
    return ((lists := list(zip(*((map(int, filter(lambda x: x != '', line.split(' ')))) for line in open("input.txt"))))), (ctr := Counter(lists[1])), sum(y*ctr[y] for y in lists[0]))[-1]

print(main())
