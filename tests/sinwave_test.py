#!/usr/bin/env python
# coding: utf-8
# Author : Rahul Bhadani
# Initial Date: 2023-05-06
__author__ = 'Rahul Bhadani'
__email__  = 'rahulbhadani@email.arizona.edu'

from numpy import pi
from numpy import sqrt

import ZTF.DataGenerator


# Step 1: create a SawtoothGenerator object
S = ZTF.DataGenerator.SineGenerator(name = 'Sin Waveform', amplitude=sqrt(2)*12480/sqrt(3), frequency=60.0, phase=-120*(pi/180))

# Step 2: generate waveform 
wave = S.generate(end_time=0.5, sample_period=5e-5)

# Step 3: make a plot
S.plot()