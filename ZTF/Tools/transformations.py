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

    Parameters
    -----------

    a:`double` | `np.array`
        the first phase of abc
    
    b:`double` | `np.array`
        the second phase of abc

    c:`double` | `np.array`
        the third phase of abc

    omega: `double` | `np.array`
        Frequency

    Returns
    ----------

    `np.array`
        dq0 transformed matrix
    
    """

    if(isinstance(omega, np.ndarray)):

        d = np.zeros(omega.shape)
        q = np.zeros(omega.shape)
        z = np.zeros(omega.shape)
        for i, om in enumerate(omega):
            transformation_matrix = 2.0/3.0 * np.array([
                [ sin(om), sin( om - 2.0*pi/3.0), sin(om + 2*pi/3.0 )  ],
                    [ cos(om), cos( om - 2.0*pi/3.0), cos(om + 2*pi/3.0 )  ],
                    [1.0/2.0, 1.0/2.0, 1.0/2.0 ]
                    ])
            ai = a[i]
            bi = b[i]
            ci = c[i]

            dq0 = np.dot( transformation_matrix, np.array ([ai, bi, ci]) )
            d[i] = dq0[0]
            q[i] = dq0[1]
            z[i] = dq0[2]

        dq0 = np.vstack((d, q, z))
        return dq0
    else:
        transformation_matrix = 2.0/3.0 * np.array([
                    [ sin(omega), sin( omega - 2.0*pi/3.0), sin(omega + 2*pi/3.0 )  ],
                        [ cos(omega), cos( omega - 2.0*pi/3.0), cos(omega + 2*pi/3.0 )  ],
                        [1.0/2.0, 1.0/2.0, 1.0/2.0 ]
                        ])
        
        dq0 = np.dot( transformation_matrix, np.array ([a, b, c]) )
        return dq0
