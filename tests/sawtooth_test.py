import ZTF.DataGenerator
from numpy import pi

# Step 1: create a SawtoothGenerator object
S = ZTF.DataGenerator.SawtoothGenerator(maxval=2*pi, minval=0.0, period=1.0/60.0)

# Step 2: generate waveform 
wave = S.generate(end_time=1.0, sample_period=5e-5)

# Step 3: make a plot
S.plot()