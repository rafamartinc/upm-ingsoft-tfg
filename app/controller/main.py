# -*- coding: utf-8 -*-
import logging
from app.model.family import Family

from app.view.view import View
from app.model.nqubit import NQubit
from app.model.sequence import Sequence
from gates import Gates

__author__ = 'Rafael Martin-Cuevas Redondo'


def main():

    view = View()
    g = Family(length=3, max_complexity=8)
    view.display(g)

if __name__ == '__main__':
    main()
