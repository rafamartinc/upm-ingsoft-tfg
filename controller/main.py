# -*- coding: utf-8 -*-
import logging

from view.view import View
from model.nqubit import NQubit
from model.sequence import Sequence
from controller.gates import Gates

__author__ = 'Rafael Martin-Cuevas Redondo'


def main():

    view = View()

    try:
        s = Sequence('G', '1', '0')
        view.display(s)

        q = NQubit(3, 6)
        view.display(q)

        Gates.gate_h(q, s)
        view.display(q)

        Gates.gate_v(q, s)
        view.display(q)

    except(ValueError, TypeError) as e:
        logging.warning(str(e))

if __name__ == '__main__':
    main()
