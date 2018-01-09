# -*- coding: utf-8 -*-
from app.model.family import Family

from app.view.view import View

__author__ = 'Rafael Martin-Cuevas Redondo'


def main():

    view = View()
    g = Family(length=2, max_complexity=10)
    view.display(g)

if __name__ == '__main__':
    main()
