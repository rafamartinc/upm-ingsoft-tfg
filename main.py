# -*- coding: utf-8 -*-
from types import IntType, LongType
from math import pow, sqrt
import numpy as np
import logging

from view import View
from model import NQubit, Gates

__author__ = 'Rafael Martin-Cuevas Redondo'


def main():

    view = View()

    try:
        q = NQubit(1, 1)
        view.display(q)

        Gates.gate_z(q)
        view.display(q)

    except(ValueError, TypeError) as e:
        logging.warning(str(e))

if __name__ == '__main__':
    main()
