# -*- coding: utf-8 -*-
from types import IntType, LongType
from math import pow, sqrt
import numpy as np
import logging

from view import View
from model import NQubit, GateFunctions

__author__ = 'Rafael Martin-Cuevas Redondo'


def main():

    view = View()
    g = GateFunctions()

    try:
        q = NQubit(3, 7)
        view.display(q)

        g.gate_g(q)
        view.display(q)

        g.gate_g(q)
        view.display(q)

    except(ValueError, TypeError) as e:
        logging.warning(str(e))

if __name__ == '__main__':
    main()
