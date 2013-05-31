import math
import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
import numpy as np
import sys

import os
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)
import linegraph
import scatterplot

def main(figureSaveLocation):
    """Create an image that demonstrates the difference between the step boundary of a decision tree and the boundary induced by an SVM.
    """

    # Define the image size.
    maxX = 20
    minX = 0
    maxY = 20
    minY = 0

    # Define the good hyperplanes.
    goodShift = 1.75
    goodDividingPlaneMinY = goodHyperlpaneDividing(x=minX)
    goodDividingPlaneMaxY = goodHyperlpaneDividing(x=maxX)
    goodDividingPlaneXCoords = [minX, maxX]
    goodDividingPlaneYCoords = [goodDividingPlaneMinY, goodDividingPlaneMaxY]

    # Determine support vectors.
    class1SupportVectorsX = np.array([8.5])
    class1SupportVectorsY = np.array([goodHyperlpaneDividing(x=class1SupportVectorsX[0] + goodShift)])
    class2SupportVectorsX = np.array([6.5, 13.0])
    class2SupportVectorsY = np.array([goodHyperlpaneDividing(x=class2SupportVectorsX[0] - goodShift), goodHyperlpaneDividing(x=class2SupportVectorsX[1] - goodShift)])

    # Define plane appearances.
    planeStyles = ['-', '--', '--']
    planeWidths = [2.0, 1.0, 1.0]

    # Class 1 data and control variables.
    class1X = np.concatenate([class1SupportVectorsX, np.array([
        1.0, 1.3, 1.5, 1.7,
        2.0, 2.2, 2.5, 2.9,
        3.0, 3.5, 3.7,
        4.0, 4.3, 4.8,
        5.1, 5.4, 5.8,
        6.5, 6.9,
        7.3, 7.6, 7.9,
        8.2, 8.5,
        9.1, 9.5,
        10.6, 10.9,
        13.3, 13.6,
        14.0])])
    class1Y = np.concatenate([class1SupportVectorsY, np.array([
        4.0, 7.9, 12.5, 16.3,
        6.7, 8.1, 17.9, 10.3,
        5.8, 13.2, 19.0,
        9.3, 17.6, 12.0,
        14.5, 8.3, 12.3,
        10.1, 17.1,
        11.7, 16.2, 19.1,
        13.7, 18.3,
        12.3, 16.7,
        15.7, 18.2,
        19.8, 17.9,
        19.0])])
    class1Color = '#0000FF'  # Blue
    class1Size = 30

    # Class 2 data and control variables.
    class2X = np.concatenate([class2SupportVectorsX, np.array([
        4.0,
        5.3, 5.7,
        6.2, 6.6, 6.9,
        7.5,
        8.1, 8.3, 8.7,
        9.2, 9.6,
        10.1, 10.5, 10.9,
        11.4, 11.7,
        12.2, 12.5, 12.9,
        13.1, 13.7,
        14.1, 14.5, 14.6,
        15.0, 15.3, 15.7, 15.9,
        16.1, 16.3, 16.5, 16.9,
        17.0, 17.5, 17.7,
        18.2, 18.3, 18.7,
        19.0, 19.3, 19.7])])
    class2Y = np.concatenate([class2SupportVectorsY, np.array([
        0.6,
        2.2, 1.2,
        0.3, 3.2, 1.7,
        2.4,
        2.3, 5.4, 3.1,
        0.7, 4.3,
        3.2, 5.6, 1.3,
        6.2, 3.4,
        7.8, 1.2, 4.3,
        2.3, 10.0,
        6.8, 11.5, 8.9,
        4.5, 7.5, 13.2, 8.3,
        2.1, 12.0, 5.7, 9.3,
        1.2, 14.4, 4.5,
        3.4, 6.7, 12.3,
        14.3, 10.1, 15.8])])
    class2Color = '#FF0000'  # Red
    class2Size = 30

    # Aggregate all class information.
    scatterXValues = [class1X, class2X]  # The X values for the classes.
    scatterXAllValues = [j for i in scatterXValues for j in i]  # A list of the X values for all the datapoints.
    scatterYValues = [class1Y, class2Y]  # The Y values for the classes.
    scatterYAllValues = [j for i in scatterYValues for j in i]  # A list of the Y values for all the datapoints.
    colors = [class1Color, class2Color]  # The colors for the classes.
    sizes = [class1Size, class2Size]  # The size of the markers for the scatterplots.

    # Define the decision tree boundary.
    decisionBoundarySegmentsXCoords = [[0.0, 0.0], [0.0, 6.0], [6.0, 6.0], [6.0, 11.0], [11.0, 11.0], [11.0, 17.0], [17.0, 17.0], [17.0, 20.0]]
    decisionBoundarySegmentsYCoords = [[0.0, 3.0], [3.0, 3.0], [3.0, 7.0], [7.0, 7.0], [7.0, 15.0], [15.0, 15.0], [15.0, 20.0], [20.0, 20.0]]

    # Create the plot.
    currentFigure = plt.figure()
    gs = gridspec.GridSpec(10, 10)
    gs.update(left=0, right=1, bottom=0, top=1, wspace=0.05)#, hspace=0.05)
    plot = plt.subplot(gs[1:-1, 1:-1])
    plot.set_xlim(left=minX, right=maxX)
    plot.set_ylim(bottom=minY, top=maxY)
    scatterplot.graphGeneration(scatterXValues, scatterYValues, currentFigure=currentFigure, colors=colors, sizes=sizes)
    linegraph.graphGeneration([goodDividingPlaneXCoords], [goodDividingPlaneYCoords], currentFigure=currentFigure, markerSizes=[0], lineWidths=[1], lineStyles=['--'])

    # Create the decision tree boundary.
    for i, j in zip(decisionBoundarySegmentsXCoords, decisionBoundarySegmentsYCoords):
        linegraph.graphGeneration([i], [j], currentFigure=currentFigure, markerSizes=[0], lineWidths=[2])
        if i[0] == i[1]:
            plt.fill_betweenx(j, i, [goodHyperlpaneDividing(y=j[0]), goodHyperlpaneDividing(y=j[1])], color='green', alpha=0.2)
        else:
            plt.fill_between(i, j, [goodHyperlpaneDividing(x=i[0]), goodHyperlpaneDividing(x=i[1])], color='green', alpha=0.2)

    # Make all the tick marks invisible.
    for ax in currentFigure.get_axes():
        removeTickMarks(ax, xAxis=True, yAxis=True)

    plt.savefig(figureSaveLocation, bbox_inches='tight', transparent=True)
    plt.show()

def goodHyperlpaneDividing(x=None, y=None):
    if x != None:
        return x
    if y != None:
        return y

def removeTickMarks(axes, xAxis=False, yAxis=False):
    """Removes all tick marks.
    """

    if xAxis:
        axes.set_xticks([])
    if yAxis:
        axes.set_yticks([])

if __name__ == '__main__':
    main(sys.argv[1])