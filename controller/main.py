# -*- coding: utf-8 -*-
import logging

from view.view import View
from model.nqubit import NQubit
from controller.gates import Gates

__author__ = 'Rafael Martin-Cuevas Redondo'


def main():

    view = View()

    try:
        q = NQubit(1, 1)
        view.display(q)

        Gates.gate_h(q)
        view.display(q)

    except(ValueError, TypeError) as e:
        logging.warning(str(e))

if __name__ == '__main__':
    main()
