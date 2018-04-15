# -*- coding: utf-8 -*-

__author__ = 'Rafael Martin-Cuevas Redondo'


class View:
    """
    Establishes communication with the user, through the application's console.
    """

    @staticmethod
    def display(o=""):
        """
        Main console output of the app.

        :param o: Object to be printed.
        """

        print(str(o))
