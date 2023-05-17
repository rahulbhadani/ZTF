#!/usr/bin/env python
# coding: utf-8
# Author : Rahul Bhadani
# Initial Date: 2023-05-06
__author__ = 'Rahul Bhadani'
__email__  = 'rahulbhadani@email.arizona.edu'


import numpy as np
import matplotlib.pyplot as plt


class WaveformGenerator:
    """
    Base class to implement a waveform generator

    Parameters
    -----------

    name: `str`
        Name of the waveform generator


    """
    def __init__(self, name, *args, **kwargs):
        self.name = name
        self.time = None
        self.values = None
        
    def waveform(self, time):
        """
        A function to represent the waveform

        Parameters
        ------------
        t: `np.array`
            A numpy array representing an array of time-points


        Returns
        ---------
        `np.array`
            A numpy array representing value of the waveform at the given time-points

        """
        raise NotImplementedError

    def generate(self, end_time, sample_period):
        """
        Function to return a waveform as a timeseries, returned as a numpy array

        Parameters
        -----------
        end_time: `double`
            End time in seconds of the  waveform

        sample_period: `double`
            Sample period in seconds of the waveform

        Returns
        -------
        `np.ndarray`
            numpy 2D array representing the waveform as a timeseries

        """
        self.time = np.arange(0, end_time + sample_period, sample_period )
        self.values = self.waveform(self.time)
        return np.array([self.time, self.values]).T
    
    def plot(self, **kwargs):
        """
        Make a plot of the waveform
        """

        plot_title = kwargs.get("title", self.name)

        plt.plot(self.time, self.values)
        plt.xlabel('Time (seconds)')
        plt.ylabel('Amplitude')
        plt.title('{}'.format(plot_title))
        plt.grid()
        plt.show()



#####################################################################################
class SawtoothGenerator(WaveformGenerator):
    """
    A class to implement SawToothGenerator

    Parameters
    -----------

    maxval: `double`
        The maximum value of the sawtooth waveform

    minval: `double`
        The minimum value of the sawtooth waveform

    period: `double`
        Time period of the sawtooth waveform
    
        
    """
    def __init__(self, name, maxval, minval, period, *args, **kwargs):
        super().__init__(name)
        self.maxval = maxval
        self.minval = minval
        self.period = period
        self.time = None
        self.values = None

    def waveform(self, time):
        """
        A function to represent the waveform

        Parameters
        ------------
        t: `np.array`
            A numpy array representing an array of time-points


        Returns
        ---------
        `np.array`
            A numpy array representing value of the waveform at the given time-points

        """
        return (self.maxval/self.period)*(time - np.floor(time/self.period)*self.period) + self.minval

#####################################################################################
class SineGenerator(WaveformGenerator):
    """
    A class to implement sine wave generator

    Parameters
    -----------

    amplitude: `double`
        Amplitude or maximum value of the sine wave

    frequency: `double`
        Frequency of the sine wave in Hz

    phase: `double`
        Phase of the sinewave in radian
    
        
    """
    def __init__(self, name, amplitude, frequency, phase, *args, **kwargs):
        super().__init__(name)
        self.amplitude = amplitude
        self.frequency = frequency
        self.phase = phase
        self.time = None
        self.values = None

    def waveform(self, time):
        """
        A function to represent the waveform

        Parameters
        ------------
        t: `np.array`
            A numpy array representing an array of time-points


        Returns
        ---------
        `np.array`
            A numpy array representing value of the waveform at the given time-points

        """
        return self.amplitude * np.sin(2 * np.pi * self.frequency * time + self.phase)
