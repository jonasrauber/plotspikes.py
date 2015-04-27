from matplotlib import pyplot as plt

def plotspikes(spiketimes, style='k-', lower=-2., upper=-1.):
    """Plots spikes as vertical lines"""
    for t in spiketimes:
        plt.plot([t, t], [lower, upper], style, hold=True)
