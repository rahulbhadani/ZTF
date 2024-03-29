#!/usr/bin/env python
# coding: utf-8
# Author : Rahul Bhadani
# Initial Date: 2023-05-06
__author__ = 'Rahul Bhadani'
__email__  = 'rahulbhadani@email.arizona.edu'

import ZTF.DataGenerator
from numpy import pi

# Step 1: create a SawtoothGenerator object
S = ZTF.DataGenerator.SawtoothGenerator(name = 'Sawtooth Waveform', maxval=2*pi, minval=0.0, period=1.0/60.0)

# Step 2: generate waveform 
wave = S.generate(end_time=1.0, sample_period=5e-5)

# Step 3: make a plot
S.plot()