#!/usr/bin/env python
# coding: utf-8
# Author : Rahul Bhadani
# Initial Date: 2023-02-06
__author__ = 'Rahul Bhadani'
__email__  = 'rahulbhadani@email.arizona.edu'
# For System and OS level task
import sys, getopt
import time
import math

class ZTF:
    """
    Z Transform implementation as difference equation.

    Z transform is defined as

    .. math::
        H(z) = \cfrac{Y(z)}{X(z)} = \cfrac{\sum_{i= 0}^n b_i z^i  }{ \sum_{j = 0}^m a_jz^j }


    which is implemented as difference equation.


    Parameters
    -----------

    num: `list`
        Coefficients of the numerator in ascending order of the power of z.

    den: `list`
        Coefficients of the denominator in ascending order of the power of z.

    """
    def __init__(self, num, den, *args, **kwargs):
        self.num = num
        self.den = den

        self.Ts = 0.05

        self.rnum = list(reversed(num))
        self.rden = list(reversed(den))
        self.zx = [0.0] * len(den)
        self.zy = [0.0] * len(den)

        self.nsize = len(num)
        self.dsize = len(den)

    def print_coefficients(self):
        """
        Print coefficients of the numerator and the denominator
        """
        print("Numerator Coefficients:", self.rnum)
        print("Denominator Coefficients:", self.rden)

    def processing(self, x):
        """

        Parameters
        -----------
        x: `double`
            Input value for which next value y in the chain is to be predicted.

        Returns
        -------
        `double`
            The next predicted value for the given input `x` as per the transfer function.

        """
        self.zx[0] = x

        y = sum(self.rnum[i] * self.zx[self.dsize - self.nsize + i] for i in range(self.nsize))
        y -= sum(self.rden[i] * self.zy[i] for i in range(self.dsize))
        y /= self.rden[0]

        self.zy[0] = y
        self.zx = self.zx[-1:] + self.zx[:-1]
        self.zy = self.zy[-1:] + self.zy[:-1]

        self.zy[0] = 0.0

        return y
