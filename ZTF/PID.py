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
from .ZTF import ZTF

class PID:
    """
    Implements a realizable discrete PID Control in the form of parallel structure consisting of three Z-transform blocks.

    .. math::
        H(Z) = P + I\cdot T_s\cdot \cfrac{1}{z-1} + D\cdot \cfrac{N}{1 + N\cdot T_s \cfrac{1}{z-1}  }

    Parameters
    -----------
    P: `double`
        Proportional term of a PID controller

    I: `double`
        Integrator term of a PID contoller

    D: `double`
        Derivative term of a PID controller

    N: `double`
        Filter coefficient for the derivative term

    Ts: `double`
        Sample time in seconds for digital PID controller

    """
    def __init__(self, P, I, D, N, Ts):
        self.P = P
        self.I = I
        self.D = D
        self.N = N
        self.Ts = Ts

        self.ztf1 = ZTF([P], [1.0])
        self.ztf2 = ZTF([I * Ts], [-1.0, 1.0])
        self.ztf3 = ZTF([-D * N, D * N], [(N * Ts - 1), 1.0])

    def processing(self, error):
        """
        Returns the value controlled value from the PID controller

        Parameters
        -----------
        error: `double`
            Error term as an input the PID controller

        Returns
        --------
        `double`
            Returns the next control command

        """
        return self.ztf1.processing(error) + self.ztf2.processing(error) + self.ztf3.processing(error)

