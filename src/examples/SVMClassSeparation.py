import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
import numpy as np
import sys

import os
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)
import addtext
import linegraph

def main(imageSaveLocation):
    """Create an image illustrating the separation of a feature space by a hyperplane.
    """

    # Define the image size.
    maxX = 10
    minX = -10
    maxY = 10
    minY = -10

    def hyperplane(x=None, y=None):
        if x:
            return ((4 * x) / 3.0) + 1.5
        elif y:
            return ((y - 1.5) * 3.0) / 4.0

    # Determine the endpoints of the hyperplane withing the image.
    hyperplaneYValueForMinX = hyperplane(x=minX)
    hyperplaneYValueForMaxX = hyperplane(x=maxX)

    # Define line endpoints.
    lineEndPointX = [minX, maxX]
    lineEndPointY = [hyperplaneYValueForMinX, hyperplaneYValueForMaxX]

    # Define the text. Multiply the minX and maxY positions by 2 for the class 1 label in order to shit it
    # left and up, and the class 2 labels's maxX and min Y to shift it right and down.
    labelOne = r'$c_1$'
    labelOneXLocation = sum([minX * 2, min(maxX, hyperplane(y=maxY))]) / 2.0
    labelOneYLocation = sum([max(minY, hyperplaneYValueForMinX), maxY * 2]) / 2.0
    labelTwo = r'$c_2$'
    labelTwoXLocation = sum([max(minX, hyperplane(y=minY)), maxX * 2]) / 2.0
    labelTwoYLocation = sum([minY * 2, min(maxY, hyperplaneYValueForMaxX)]) / 2.0
    classLabels = [labelOne, labelTwo]
    classLabelXLocs = [labelOneXLocation, labelTwoXLocation]
    classLabelYLocs = [labelOneYLocation, labelTwoYLocation]

    # Create the plot.
    currentFigure = plt.figure()
    gs = gridspec.GridSpec(10, 10)
    gs.update(left=0, right=1, bottom=0, top=1, wspace=0.05)#, hspace=0.05)
    plot = plt.subplot(gs[1:-1, 1:-1])
    plot.set_xlim(left=minX, right=maxX)
    plot.set_ylim(bottom=minY, top=maxY)
    linegraph.graphGeneration([lineEndPointX], [lineEndPointY], currentFigure=currentFigure, markerSizes=[0], lineWidths=[5])
    plt.fill_between(lineEndPointX, lineEndPointY, [maxY] * len(lineEndPointX), color='black', alpha=0.3)

    # Add two lines to represent the axes.
    halfWayXAxis = (minX + maxX) / 2.0
    halfWayYAxis = (minY + maxY) / 2.0
    linegraph.graphGeneration([[halfWayXAxis, halfWayXAxis], [minX, maxX]], [[minY, maxY], [halfWayYAxis, halfWayYAxis]], currentFigure=currentFigure, markerSizes=[0, 0], lineWidths=[2, 2])

    # Add the class labels to the graph.
    addtext.graphGeneration(classLabelXLocs, classLabelYLocs, classLabels, currentFigure=currentFigure, sizes=[30] * len(classLabels), zorders=list(range(len(classLabels))))

    removeTickMarks(plot, xAxis=True, yAxis=True)

    plt.savefig(imageSaveLocation, bbox_inches='tight', transparent=True)
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