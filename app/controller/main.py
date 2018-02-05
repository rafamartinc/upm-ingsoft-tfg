# -*- coding: utf-8 -*-
from app.model.family import Family
import time

__author__ = 'Rafael Martin-Cuevas Redondo'


def main():
    start_time = time.time()
    Family(length=2, max_complexity=5)
    print "--- " + str(time.time() - start_time) + " seconds ---"

if __name__ == '__main__':
    main()
