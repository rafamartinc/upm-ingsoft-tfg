# -*- coding: utf-8 -*-
from app.model.family import Family
from app.view.view import View
import time

__author__ = 'Rafael Martin-Cuevas Redondo'


def main():
    start_time = time.time()
    Family(length=1, max_complexity=100)

    file = open("output.txt", "r")

    count = {}
    complexity = 0
    pattern = 'sqrt(2)^('
    line = file.readline()
    while line is not '':
        if 'COMPLEXITY' in line:
            complexity += 1
            count[complexity] = {}
        elif pattern in line:
            pos = line.index(pattern) + len(pattern)
            if line[pos] == '-':
                pos += 1
            k = int(line[pos])
            if count[complexity].has_key(k):
                count[complexity][k] += 1
            else:
                count[complexity][k] = 1
        line = file.readline()

    for compl in count.keys():
        View.display("COMPLEXITY " + str(compl))
        for k in count[compl].keys():
            View.display(print "     Level " + str(k) + ": " + str(count[compl][k]))

    file.close()

    View.display("--- " + str(time.time() - start_time) + " seconds ---")

if __name__ == '__main__':
    main()
