#!/usr/bin/env python

from plotspikes import plotspikes
from matplotlib import pyplot as plt
import numpy as np

def main():
    """Example how to use plotspikes"""
    
    # create a figure and plot some random signal
    plt.figure(0, figsize=(15,5))
    np.random.seed(22)
    xsignal = 20 * np.arange(100)
    ysignal = 6. + np.cumsum(np.random.randn(100))
    plt.plot(xsignal, ysignal, 'm', hold=True)
    
    # create random spikes and plot them using plotspikes
    spiketimes = 40 * np.arange(0, 50) + 40 * np.random.randn(50)
    plotspikes(spiketimes, 'c-', -2.5, -1.5)
    
    # add labels and axis limits
    plt.xlabel("time in ms")
    plt.xlim([-50, 2050])
    
    # show the complete plot
    plt.show()

if __name__ == "__main__":
    main()
