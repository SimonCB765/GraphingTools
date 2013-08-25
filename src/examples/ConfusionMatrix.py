import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
import numpy as np
import sys

import os
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)
import addtext
import linegraph


def main(figureSaveLocation):
    """Create an example cofusion matrix image.

    @type figureSaveLocation - str
    @use  figureSaveLocation - The location where the figure will be saved.
    """
    
    # Define the axes sizes.
    axisMinValue = 0
    axisMaxValue = 8
    
    # Define the lines used for the confusion matrix.
    lineXCoords = [[axisMinValue, axisMaxValue], [axisMinValue, axisMaxValue],  # Lines at the top and bottom of the matrix.
                   [2, 2], [6, 6],                                              # Lines at the left and right of the matrix.
                   [axisMinValue + 1, axisMaxValue],                            # Line separating true classes.
                   [4, 4],                                                      # Line separating predicted classes.
                   [axisMinValue + 1, axisMinValue + 1],                        # Line under true class heading.
                   [2, 6]]                                                      # Line under predicted class heading.
    lineYCoords = [[6, 6], [2, 2],                                              # Lines at the left and right of the matrix.
                   [axisMinValue, axisMaxValue], [axisMinValue, axisMaxValue],  # Lines at the top and bottom of the matrix.
                   [4, 4],                                                      # Line separating true classes.
                   [axisMinValue, axisMaxValue - 1],                            # Line separating predicted classes.
                   [2, 6],                                                      # Line under true class heading.
                   [axisMaxValue - 1, axisMaxValue - 1]]                        # Line under predicted class heading.
    
    # Initialise the figure.
    currentFigure = plt.figure()
    gs = gridspec.GridSpec(10, 10)
    gs.update(left=0, right=1, bottom=0, top=1, wspace=0.05)
    axes = plt.subplot(gs[1:-1, 1:-1])
    axes.axis('equal')
    axes.axis('off')
    axes.set_xlim(left=axisMinValue, right=axisMaxValue)
    axes.set_ylim(bottom=axisMinValue, top=axisMaxValue)
    
    # Draw the lines for the confusion matrix.
    linegraph.graphGeneration(lineXCoords, lineYCoords, currentFigure=currentFigure, markerSizes=[0] * len(lineXCoords))

    # Add the text.
    addtext.graphGeneration([axisMinValue + 0.5], [4], ['True Class'], currentFigure=currentFigure, sizes=[20], rotations=[90])
    addtext.graphGeneration([4], [axisMaxValue - 0.5], ['Predicted Class'], currentFigure=currentFigure, sizes=[20])
    addtext.graphGeneration([axisMinValue + 1.5, axisMinValue + 1.5], [3, 5], ['Unlabelled', 'Positive'], currentFigure=currentFigure,
        sizes=[15, 15], rotations=[90, 90])  # True class class labels.
    addtext.graphGeneration([3, 5], [axisMaxValue - 1.5, axisMaxValue - 1.5], ['Positive', 'Unlabelled'], currentFigure=currentFigure,
        sizes=[15, 15])  # Predicted class class labels.
    addtext.graphGeneration([3, 5], [5, 5], ['TP', 'FN'], currentFigure=currentFigure, sizes=[20, 20])
    addtext.graphGeneration([3, 5], [3, 3], ['FP', 'TN'], currentFigure=currentFigure, sizes=[20, 20])

    addtext.graphGeneration([3, 5], [axisMinValue + 1, axisMinValue + 1], ['TP + FP\n(' + r'$P_P$' + ')', 'TN + FN\n(' + r'$N_P$' + ')'], currentFigure=currentFigure, sizes=[20, 20])
    addtext.graphGeneration([axisMaxValue - 1, axisMaxValue - 1], [5, 3], ['TP + FN\n(' + r'$P_T$' + ')', 'TN + FP\n(' + r'$N_T$' + ')'], currentFigure=currentFigure, sizes=[20, 20])
    addtext.graphGeneration([axisMaxValue - 1], [axisMinValue + 1], [r'$\mathcal{N}$'], currentFigure=currentFigure, sizes=[20])

    # Finalise the figure.
    hideAxesLabelling(axes, xAxis=True, yAxis=True)

    # Save the figure.
    plt.savefig(figureSaveLocation, bbox_inches='tight', transparent=True)
    plt.show()

def hideAxesLabelling(axes, xAxis=False, yAxis=False):
    """Hides all tick marks, tick labels, axis labels, etc.
    """

    if xAxis:
        axes.xaxis.set_visible(False)
    if yAxis:
        axes.yaxis.set_visible(False)


if __name__ == '__main__':
    main(sys.argv[1])