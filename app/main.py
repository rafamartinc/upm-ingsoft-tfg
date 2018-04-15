# -*- coding: utf-8 -*-
import time

from app.family.family import Family
from app.view.view import View

__author__ = 'Rafael Martin-Cuevas Redondo'


def main():
    start_time = time.time()

    Family(length=1, max_complexity=50)

    View.display("--- " + str(time.time() - start_time) + " seconds ---")

if __name__ == '__main__':
    main()
