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
    """
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
    goodPlaneClass1XCoords = [minX, maxX - goodShift]
    goodPlaneClass1YCoords = [goodHyperlpaneDividing(x=minX+goodShift), goodDividingPlaneMaxY]
    goodPlaneClass2XCoords = [minX + goodShift, maxX]
    goodPlaneClass2YCoords = [goodDividingPlaneMinY, goodHyperlpaneDividing(x=maxX-goodShift)]
    goodPlanesXCoords = [goodDividingPlaneXCoords, goodPlaneClass1XCoords, goodPlaneClass2XCoords]
    goodPlanesYCoords = [goodDividingPlaneYCoords, goodPlaneClass1YCoords, goodPlaneClass2YCoords]

    # Determine support vectors.
    class1SupportVectorsX = np.array([8.5])
    class1SupportVectorsY = np.array([goodHyperlpaneDividing(x=class1SupportVectorsX[0] + goodShift)])
    goodClass2SupportVectorsX = np.array([6.5, 13.0])
    goodClass2SupportVectorsY = np.array([goodHyperlpaneDividing(x=goodClass2SupportVectorsX[0] - goodShift), goodHyperlpaneDividing(x=goodClass2SupportVectorsX[1] - goodShift)])
    poorClass2SupportVectorsX = np.array([goodClass2SupportVectorsX[0]])
    poorClass2SupportVectorsY = np.array([goodClass2SupportVectorsY[0]])

    # Determine the equation of the line for the poor hyperplane.
    yOffsetOfPoorHyperplane = 2
    pointPoorHyperplaneMustGoThroughX = (class1SupportVectorsX[0] + goodClass2SupportVectorsX[0]) / 2
    pointPoorHyperplaneMustGoThroughY = (class1SupportVectorsY[0] + goodClass2SupportVectorsY[0]) / 2
    arbitrarySecondPointOnPoorHyperplaneX = goodClass2SupportVectorsX[1]
    arbitrarySecondPointOnPoorHyperplaneY = goodClass2SupportVectorsX[1] + yOffsetOfPoorHyperplane
    gradientOfPoorHyperplane = (pointPoorHyperplaneMustGoThroughY - arbitrarySecondPointOnPoorHyperplaneY) / (pointPoorHyperplaneMustGoThroughX - arbitrarySecondPointOnPoorHyperplaneX)
    c = pointPoorHyperplaneMustGoThroughY - (pointPoorHyperplaneMustGoThroughX * gradientOfPoorHyperplane)

    # Define the poor hyperplane.
    def poorHyperlpaneDividing(x=None, y=None):
        if x != None:
            return (x * gradientOfPoorHyperplane) + c
        if y != None:
            return (y - c) / gradientOfPoorHyperplane
    poorShiftClass1 = abs(class1SupportVectorsX[0] - poorHyperlpaneDividing(y=class1SupportVectorsY[0]))
    poorShiftClass2 = abs(goodClass2SupportVectorsX[0] - poorHyperlpaneDividing(y=goodClass2SupportVectorsY[0]))
    poorDividingPlaneMinY = poorHyperlpaneDividing(x=minX)
    poorDividingPlaneMaxY = poorHyperlpaneDividing(x=maxX)
    poorDividingPlaneXCoords = [minX, maxX]
    poorDividingPlaneYCoords = [poorDividingPlaneMinY, poorDividingPlaneMaxY]
    poorPlaneClass1XCoords = [minX, maxX - poorShiftClass1]
    poorPlaneClass1YCoords = [poorHyperlpaneDividing(x=minX+poorShiftClass1), poorDividingPlaneMaxY]
    poorPlaneClass2XCoords = [minX + poorShiftClass2, maxX]
    poorPlaneClass2YCoords = [poorDividingPlaneMinY, poorHyperlpaneDividing(x=maxX-poorShiftClass2)]
    poorPlanesXCoords = [poorDividingPlaneXCoords, poorPlaneClass1XCoords, poorPlaneClass2XCoords]
    poorPlanesYCoords = [poorDividingPlaneYCoords, poorPlaneClass1YCoords, poorPlaneClass2YCoords]

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
    class2X = np.concatenate([goodClass2SupportVectorsX, np.array([
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
    class2Y = np.concatenate([goodClass2SupportVectorsY, np.array([
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

    # Define the z orders for the scatter points and lines.
    scatterZorders = [0, 1]  # Used to determine which points should be plotted on top of which other ones.
    lineZorders = [min(scatterZorders) - 1] * 3  # Put the lines below all points.

    # Create the figure, the grids for the subplots and determine the spacing for the subplots.
    currentFigure = plt.figure()
    gs = gridspec.GridSpec(2, 3)
    gs.update(left=0, right=1, bottom=0.05, top=1, wspace=0.05)#, hspace=0.05)

    # Create the graph for the poor hyperplane.
    poorDividingPlot = plt.subplot(gs[0, 1])
    poorDividingPlot.axis('scaled')
    poorDividingPlot.set_xlim(left=minX, right=maxX)
    poorDividingPlot.set_ylim(bottom=minY, top=maxY)
    scatterplot.graphGeneration(scatterXValues, scatterYValues, currentFigure=currentFigure, colors=colors, sizes=sizes, zorders=scatterZorders)
    linegraph.graphGeneration(poorPlanesXCoords, poorPlanesYCoords, currentFigure=currentFigure, markerSizes=[0] * 3, lineWidths=planeWidths, lineStyles=planeStyles, zorders=lineZorders)
    for i in range(len(class1SupportVectorsX)):
        # Add the circles around the class 1 support vectors.
        currentFigure.gca().add_artist(plt.Circle((class1SupportVectorsX[i], class1SupportVectorsY[i]), 0.5, fill=False))
    for i in range(len(poorClass2SupportVectorsX)):
        # Add the circles around the class 1 support vectors.
        currentFigure.gca().add_artist(plt.Circle((poorClass2SupportVectorsX[i], poorClass2SupportVectorsY[i]), 0.5, fill=False))

    # Create the graph for the good hyperplane.
    goodDividingPlot = plt.subplot(gs[1, 1])
    goodDividingPlot.axis('scaled')
    goodDividingPlot.set_xlim(left=minX, right=maxX)
    goodDividingPlot.set_ylim(bottom=minY, top=maxY)
    scatterplot.graphGeneration(scatterXValues, scatterYValues, currentFigure=currentFigure, colors=colors, sizes=sizes, zorders=scatterZorders)
    linegraph.graphGeneration(goodPlanesXCoords, goodPlanesYCoords, currentFigure=currentFigure, markerSizes=[0] * 3, lineWidths=planeWidths, lineStyles=planeStyles, zorders=lineZorders)
    for i in range(len(class1SupportVectorsX)):
        # Add the circles around the class 1 support vectors.
        currentFigure.gca().add_artist(plt.Circle((class1SupportVectorsX[i], class1SupportVectorsY[i]), 0.5, fill=False))
    for i in range(len(goodClass2SupportVectorsX)):
        # Add the circles around the class 1 support vectors.
        currentFigure.gca().add_artist(plt.Circle((goodClass2SupportVectorsX[i], goodClass2SupportVectorsY[i]), 0.5, fill=False))

    # Make all the tick marks invisible, and label the x axes.
    labels = ['(b)', '(a)']
    for ax in currentFigure.get_axes():
        removeTickMarks(ax, xAxis=True, yAxis=True)
        currentLabel = labels.pop()
        setLabels(ax, xLabel=currentLabel)
        ax.xaxis.set_label_coords(0.5, -0.025)

    plt.savefig(figureSaveLocation, bbox_inches=0, transparent=True)
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

def setLabels(axes, xLabel='', yLabel=''):
    """Set the X and Y labels of the axes.
    """

    axes.set_xlabel(xLabel)
    axes.set_ylabel(yLabel)

if __name__ == '__main__':
    main(sys.argv[1])