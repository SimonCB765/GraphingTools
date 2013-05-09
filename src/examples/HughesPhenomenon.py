import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
import numpy as np
import sys

import os
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)
import linegraph

def main(imageSaveLocation):
    """Create an image illustrating the hughes phenomenon.
    """

    # Create the lines for the graph.

    # Create the plot.
    currentFigure = plt.figure()
    gs = gridspec.GridSpec(10, 10)
    gs.update(left=0, right=1, bottom=0, top=1, wspace=0.05)#, hspace=0.05)
    plot = plt.subplot(gs[1:-1, 1:-1])
    plot.set_xlabel('Data Dimensionality')
    plot.set_ylabel('Classifier Performance')
    removeTickMarks(plot, xAxis=True, yAxis=True)

    plt.savefig(imageSaveLocation, bbox_inches=0, transparent=True)
    plt.show()
	


def removeTickMarks(axes, xAxis=False, yAxis=False):
    """Removes all tick marks.
    """

    if xAxis:
        axes.set_xticks([])
    if yAxis:
        axes.set_yticks([])


if __name__ == '__main__':
    main(sys.argv[1])