import math
import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
import numpy as np
import sys

import os
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)
import addtext
import linegraph
import scatterplot


def main(figureSaveLocation):
    """Create an image that demonstrates the classifcation of data points using the k-NN algorithm.

    @type figureSaveLocation - str
    @use  figureSaveLocation - The location where the figure will be saved.
    """

    # Class 1 data and control variables.
    class1X = np.array([0.0, 0.4, 1.0, 1.3, 1.4, 2.2, 2.5, 2.9, 3.3, 4.0, 4.0, 5.0])
    class1Y = np.array([4.3, 6.5, 5.3, 7.3, 4.0, 3.3, 5.4, 6.9, 7.6, 3.7, 5.6, 4.8])
    class1Color = '#0000FF'  # Blue
    class1Size = 30

    # Class 2 data and control variables.
    class2X = np.array([3.5, 4.4, 4.8, 5.0, 5.5, 6.0, 6.5, 6.9, 7.3, 8.0, 9.0])
    class2Y = np.array([3.3, 0.2, 1.7, 4.0, 5.7, 2.2, 0.7, 3.4, 5.5, 2.8, 2.4])
    class2Color = '#FF0000'  # Red
    class2Size = 30

    # Data point to classify X.
    dataPointXXValue = np.array([4.5])
    dataPointXYValue = np.array([6.3])
    dataPointXColor = '#000000'  # Black
    dataPointXSize = 30
    dataPointXTextXValue = dataPointXXValue + 0.5
    dataPointXTextYValue = dataPointXYValue + 0.5

    # Data point to classify Y.
    dataPointYXValue = np.array([3.5])
    dataPointYYValue = np.array([2.5])
    dataPointYColor = '#000000'  # Black
    dataPointYSize = 30
    dataPointYTextXValue = dataPointYXValue - 0.5
    dataPointYTextYValue = dataPointYYValue - 0.5

    # Aggregate all class information.
    scatterXValues = [class1X, class2X, dataPointXXValue, dataPointYXValue]  # The X values for the classes, A and B.
    scatterXAllValues = [j for i in scatterXValues for j in i]  # A list of the X values for all the datapoints.
    scatterXMin = min(scatterXAllValues)
    scatterXMax = max(scatterXAllValues)
    scatterYValues = [class1Y, class2Y, dataPointXYValue, dataPointYYValue]  # The Y values for the classes, A and B.
    scatterYAllValues = [j for i in scatterYValues for j in i]  # A list of the Y values for all the datapoints.
    scatterYMin = min(scatterYAllValues)
    scatterYMax = max(scatterYAllValues)
    colors = [class1Color, class2Color, dataPointXColor, dataPointYColor]  # The colors for the classes, A and B.
    sizes = [class1Size, class2Size, dataPointXSize, dataPointYSize]  # The size of the markers for the scatterplots.
    scatterZorders = [0, 1, 2, 3]  # Used to determine which points should be plotted on top of which other ones (class 1 is on the bottom and 4 on the top).
    lineZorder = [min(scatterZorders) - 1]  # Put the line below all points.

    # Determine the nearest neighbours for data point A.
    dataPointXDistances = [math.sqrt((dataPointXXValue - i)**2 + (dataPointXYValue - j)**2) for i, j in zip(scatterXAllValues, scatterYAllValues)]
    dataPointXSortedDistances = sorted(zip(dataPointXDistances, range(len(dataPointXDistances))))
    dataPointX1NNIndices = [dataPointXSortedDistances[1][1]]  # Ignore the closest data point as that will be data point A.
    dataPointX1NNXValues = [[dataPointXXValue, scatterXAllValues[i]] for i in dataPointX1NNIndices]
    dataPointX1NNYValues = [[dataPointXYValue, scatterYAllValues[i]] for i in dataPointX1NNIndices]
    dataPointX3NNIndices = [i[1] for i in dataPointXSortedDistances[1:4]]  # Ignore the closest data point as that will be data point A.
    dataPointX3NNXValues = [[dataPointXXValue, scatterXAllValues[i]] for i in dataPointX3NNIndices]
    dataPointX3NNYValues = [[dataPointXYValue, scatterYAllValues[i]] for i in dataPointX3NNIndices]
    dataPointX5NNIndices = [i[1] for i in dataPointXSortedDistances[1:6]]  # Ignore the closest data point as that will be data point A.
    dataPointX5NNXValues = [[dataPointXXValue, scatterXAllValues[i]] for i in dataPointX5NNIndices]
    dataPointX5NNYValues = [[dataPointXYValue, scatterYAllValues[i]] for i in dataPointX5NNIndices]

    # Determine the nearest neighbours for data point B.
    dataPointYDistances = [math.sqrt((dataPointYXValue - i)**2 + (dataPointYYValue - j)**2) for i, j in zip(scatterXAllValues, scatterYAllValues)]
    dataPointYSortedDistances = sorted(zip(dataPointYDistances, range(len(dataPointYDistances))))
    dataPointY1NNIndices = [dataPointYSortedDistances[1][1]]  # Ignore the closest data point as that will be data point B.
    dataPointY1NNXValues = [[dataPointYXValue, scatterXAllValues[i]] for i in dataPointY1NNIndices]
    dataPointY1NNYValues = [[dataPointYYValue, scatterYAllValues[i]] for i in dataPointY1NNIndices]
    dataPointY3NNIndices = [i[1] for i in dataPointYSortedDistances[1:4]]  # Ignore the closest data point as that will be data point B.
    dataPointY3NNXValues = [[dataPointYXValue, scatterXAllValues[i]] for i in dataPointY3NNIndices]
    dataPointY3NNYValues = [[dataPointYYValue, scatterYAllValues[i]] for i in dataPointY3NNIndices]
    dataPointY5NNIndices = [i[1] for i in dataPointYSortedDistances[1:6]]  # Ignore the closest data point as that will be data point B.
    dataPointY5NNXValues = [[dataPointYXValue, scatterXAllValues[i]] for i in dataPointY5NNIndices]
    dataPointY5NNYValues = [[dataPointYYValue, scatterYAllValues[i]] for i in dataPointY5NNIndices]

    # Determine the line coordinates for the kNN lines.
    coords1NNXValues = dataPointX1NNXValues + dataPointY1NNXValues
    coords1NNYValues = dataPointX1NNYValues + dataPointY1NNYValues
    coords3NNXValues = dataPointX3NNXValues + dataPointY3NNXValues
    coords3NNYValues = dataPointX3NNYValues + dataPointY3NNYValues
    coords5NNXValues = dataPointX5NNXValues + dataPointY5NNXValues
    coords5NNYValues = dataPointX5NNYValues + dataPointY5NNYValues

    # Create the figure, the grids for the subplots and determine the spacing for the subplots.
    currentFigure = plt.figure()
    gsTopRow = gridspec.GridSpec(2, 4)
    gsBotRow = gridspec.GridSpec(2, 4)
    gsTopRow.update(left=0.005, right=0.995, bottom=0.05, top=1, wspace=0.05)#, hspace=0.05)
    gsBotRow.update(left=0.005, right=0.995, bottom=0.05, top=1, wspace=0.05)#, hspace=0.05)

    # Create the scatterplot for the 1NN graph.
    scatter1NN = plt.subplot(gsTopRow[0, 0:2])  # Scatter plot for the 1NN example.
    scatter1NN.axis('scaled')
    scatterplot.graphGeneration(scatterXValues, scatterYValues, currentFigure=currentFigure, colors=colors, sizes=sizes, zorders=scatterZorders)
    scatter1NN.set_xlim(left=scatterXMin - 0.5, right=scatterXMax + 0.5)
    scatter1NN.set_ylim(bottom=scatterYMin - 0.5, top=scatterYMax + 0.5)
    linegraph.graphGeneration(coords1NNXValues, coords1NNYValues, currentFigure=currentFigure, markerSizes=[0] * 2, lineWidths=[1.0] * 2, zorders=lineZorder)
    addtext.graphGeneration([dataPointXTextXValue, dataPointYTextXValue], [dataPointXTextYValue, dataPointYTextYValue], ['X', 'Y'], currentFigure=currentFigure)

    # Create the scatterplot for the 3NN graph.
    scatter3NN = plt.subplot(gsTopRow[0, 2:])  # Scatter plot for the 3NN example.
    scatter3NN.axis('scaled')
    scatterplot.graphGeneration(scatterXValues, scatterYValues, currentFigure=currentFigure, colors=colors, sizes=sizes, zorders=scatterZorders)
    scatter3NN.set_xlim(left=scatterXMin - 0.5, right=scatterXMax + 0.5)
    scatter3NN.set_ylim(bottom=scatterYMin - 0.5, top=scatterYMax + 0.5)
    linegraph.graphGeneration(coords3NNXValues, coords3NNYValues, currentFigure=currentFigure, markerSizes=[0] * 6, lineWidths=[1.0] * 6, zorders=lineZorder)
    addtext.graphGeneration([dataPointXTextXValue, dataPointYTextXValue], [dataPointXTextYValue, dataPointYTextYValue], ['X', 'Y'], currentFigure=currentFigure)

    # Create the scatterplot for the 5NN graph.
    scatter5NN = plt.subplot(gsBotRow[1, 1:3])  # Scatter plot for the 5NN example.
    scatter5NN.axis('scaled')	
    scatterplot.graphGeneration(scatterXValues, scatterYValues, currentFigure=currentFigure, colors=colors, sizes=sizes, zorders=scatterZorders)
    scatter5NN.set_xlim(left=scatterXMin - 0.5, right=scatterXMax + 0.5)
    scatter5NN.set_ylim(bottom=scatterYMin - 0.5, top=scatterYMax + 0.5)
    linegraph.graphGeneration(coords5NNXValues, coords5NNYValues, currentFigure=currentFigure, markerSizes=[0] * 10, lineWidths=[1.0] * 10, zorders=lineZorder)
    addtext.graphGeneration([dataPointXTextXValue, dataPointYTextXValue], [dataPointXTextYValue, dataPointYTextYValue], ['X', 'Y'], currentFigure=currentFigure)

    # Make all the tick marks invisible, and label the x axes.
    labels = ['(c)', '(b)', '(a)']
    for ax in currentFigure.get_axes():
        removeTickMarks(ax, xAxis=True, yAxis=True)
        currentLabel = labels.pop()
        setLabels(ax, xLabel=currentLabel)
        ax.xaxis.set_label_coords(0.5, -0.025)

    plt.savefig(figureSaveLocation, bbox_inches=0, transparent=True)
    plt.show()

def setLabels(axes, xLabel='', yLabel=''):
    """Set the X and Y labels of the axes.
    """

    axes.set_xlabel(xLabel)
    axes.set_ylabel(yLabel)

def hideAxesLabelling(axes, xAxis=False, yAxis=False):
    """Hides all tick marks, tick labels, axis labels, etc.
    """

    if xAxis:
        axes.xaxis.set_visible(False)
    if yAxis:
        axes.yaxis.set_visible(False)

def removeTickMarks(axes, xAxis=False, yAxis=False):
    """Removes all tick marks.
    """

    if xAxis:
        axes.set_xticks([])
    if yAxis:
        axes.set_yticks([])

def removeTickLabels(axes, xAxis=False, yAxis=False):
    """Removes that tick labels.
    """

    if xAxis:
        axes.set_xticklabels([])
    if yAxis:
        axes.set_yticklabels([])


if __name__ == '__main__':
    main(sys.argv[1])