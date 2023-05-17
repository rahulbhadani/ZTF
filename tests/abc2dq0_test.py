#!/usr/bin/env python
# coding: utf-8
# Author : Rahul Bhadani
# Initial Date: 2023-05-06
__author__ = 'Rahul Bhadani'
__email__  = 'rahulbhadani@email.arizona.edu'

from numpy import pi
from numpy import sqrt
import matplotlib.pyplot as plt

import ZTF.DataGenerator
import ZTF.Tools




A = ZTF.DataGenerator.SineGenerator(name = 'Sin Waveform A', amplitude=sqrt(2)*12480/sqrt(3), frequency=60.0, phase=0)
wave = A.generate(end_time=0.1, sample_period=5e-5)

B = ZTF.DataGenerator.SineGenerator(name = 'Sin Waveform B', amplitude=sqrt(2)*12480/sqrt(3), frequency=60.0, phase=-120*(pi/180))
wave = B.generate(end_time=0.1, sample_period=5e-5)

C = ZTF.DataGenerator.SineGenerator(name = 'Sin Waveform C', amplitude=sqrt(2)*12480/sqrt(3), frequency=60.0, phase=120*(pi/180))
wave = C.generate(end_time=0.1, sample_period=5e-5)

S = ZTF.DataGenerator.SawtoothGenerator(name = 'Sawtooth Waveform', maxval=2*pi, minval=0.0, period=1.0/60.0)
wave = S.generate(end_time=0.1, sample_period=5e-5)

dq0 = ZTF.Tools.abc2dq0(A.values, B.values, C.values, S.values)

fig, ax = plt.subplots(3)

ax[0].plot(A.time, dq0[0])
ax[1].plot(A.time, dq0[1])
ax[2].plot(S.time, S.values)
plt.show()