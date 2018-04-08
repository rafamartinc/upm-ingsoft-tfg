# -*- coding: utf-8 -*-
from app.model.family import Family
from app.view.view import View
import time

__author__ = 'Rafael Martin-Cuevas Redondo'


def main():
    start_time = time.time()

    f = Family(length=2, max_complexity=6)
    f.count_family_members()

    View.display("--- " + str(time.time() - start_time) + " seconds ---")

if __name__ == '__main__':
    main()
