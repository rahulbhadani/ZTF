#!/usr/bin/env python
# coding: utf-8
# Author : Rahul Bhadani
# Initial Date: 2023-05-06
__author__ = 'Rahul Bhadani'
__email__  = 'rahulbhadani@email.arizona.edu'


import numpy as np
from numpy import pi
from numpy import cos
from numpy import sin


"""
Mathematical Transformations for Various Applications
"""

def abc2dq0(a, b, c, omega):
    """
    abc to dq0 transformation to convert a three-phase sinusoidal signal to a dq0 rotating frame.
    Based on code by Github.com/JDWarner/Conpy
    """   
    transformation_matrix = 2.0/3.0 * np.array([
        [ cos(omega), cos( omega - 2.0*pi/3.0), cos(omega + 2*pi/3.0 )  ],
            [ sin(omega), sin( omega - 2.0*pi/3.0), sin(omega + 2*pi/3.0 )  ],
            [1.0/2.0, 1.0/2.0, 1.0/2.0 ]
            ])
    dq0 = np.dot( transformation_matrix, np.array ([[a, b, c]]) )
    return dq0
