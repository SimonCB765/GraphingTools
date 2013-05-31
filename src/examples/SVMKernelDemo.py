import math
import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import sys

import os
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)
import linegraph
import scatterplot
import scatterplot3D
import surface3D

def main(figureSaveLocation):
    """Create an image that demonstrates the use of a kernel to classify non-linear data.
    The hyperplane in the 3D plot sometimes appears without its edge colour. If you want the edge colour, then run the script until it appears.
    """

    # Define the image size.
    maxX = 5
    minX = -5
    maxY = 5
    minY = -5
    maxZ = 5
    minZ = -5

    # Define the width of the circular border.
    circleWidth = 2.2

    # Setup the scatter data for class 1.
    class1XValues = np.array([
        -1.8, -1.7, -1.6, -1.5, -1.4, -1.3, -1.2, -1.1,
        -1.0, -0.9, -0.8, -0.8, -0.7, -0.6, -0.5, -0.5, -0.4, -0.3, -0.2, -0.2, -0.1,
        0.0, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9,
        1.0, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8
        ])
    class1YValues = np.array([
        0.1, -0.2, 0.4, -0.4, 0.3, 0.5, -1.0, 0.4,
        0.3, 1.1, 1.35, -0.2, 0.5, -0.9, 1.3, 0.3, 1.6, -1.2, -0.5, -1.6, 0.7,
        1.3, 0.4, -1.3, 0.6, 0.1, -0.5, 1.3, 0.4, -1.1, -0.8, -1.5,
        1.1, 0.3, -0.3, 0.9, -0.9, 1.2, -0.6, 0.3, 0.6, -0.2
        ])
    class1ZValues = np.array([maxZ - math.sqrt(i**2 + j**2) for i, j in zip(class1XValues, class1YValues)])
    class1Color = '#0000FF'  # Blue
    class1Size = 30

    # Setup the scatter data for class 2.
    class2XValues = np.array([
        -0.0, -0.1, -0.2, -0.3, -0.4, -0.5, -0.6, -0.7, -0.8, -0.9,
        -0.0, -0.1, -0.2, -0.3, -0.4, -0.5, -0.6, -0.7, -0.8, -0.9,
        -1.0, -1.1, -1.2, -1.3, -1.4, -1.5, -1.6, -1.7, -1.7, -1.8, -1.9,
        -1.0, -1.1, -1.2, -1.3, -1.4, -1.5, -1.6, -1.7, -1.7, -1.8, -1.9,
        -2.0, -2.0, -2.1, -2.2, -2.3, -2.3, -2.4, -2.4, -2.4, -2.5, -2.5, -2.6, -2.7, -2.8, -2.8, -2.8, -2.9,
        -2.0, -2.0, -2.1, -2.2, -2.3, -2.3, -2.4, -2.4, -2.4, -2.5, -2.5, -2.6, -2.7, -2.8, -2.8, -2.8, -2.9,
        -3.0, -3.0, -3.1, -3.2, -3.2, -3.3, -3.4, -3.4, -3.4, -3.5, -3.5, -3.6, -3.7, -3.8, -3.9,
        -3.0, -3.0, -3.1, -3.2, -3.2, -3.3, -3.4, -3.4, -3.4, -3.5, -3.5, -3.6, -3.7, -3.8, -3.9,
        -4.0, -4.0, -4.1, -4.1, -4.2, -4.2, -4.3, -4.4, -4.5, -4.6, -4.6, -4.7,
        -4.0, -4.0, -4.1, -4.1, -4.2, -4.2, -4.3, -4.4, -4.5, -4.6, -4.6, -4.7,
        -4.0, -4.2, -4.6,
        0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9,
        0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9,
        1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.7, 1.8, 1.9,
        1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.7, 1.8, 1.9,
        2.0, 2.0, 2.1, 2.2, 2.3, 2.3, 2.4, 2.4, 2.4, 2.5, 2.5, 2.6, 2.7, 2.8, 2.8, 2.8, 2.9,
        2.0, 2.0, 2.1, 2.2, 2.3, 2.3, 2.4, 2.4, 2.4, 2.5, 2.5, 2.6, 2.7, 2.8, 2.8, 2.8, 2.9,
        3.0, 3.0, 3.1, 3.2, 3.2, 3.3, 3.4, 3.4, 3.4, 3.5, 3.5, 3.6, 3.7, 3.8, 3.9,
        3.0, 3.0, 3.1, 3.2, 3.2, 3.3, 3.4, 3.4, 3.4, 3.5, 3.5, 3.6, 3.7, 3.8, 3.9,
        4.0, 4.0, 4.1, 4.1, 4.2, 4.2, 4.3, 4.4, 4.5, 4.6, 4.6, 4.7,
        4.0, 4.0, 4.1, 4.1, 4.2, 4.2, 4.3, 4.4, 4.5, 4.6, 4.6, 4.7,
        4.0, 4.2, 4.6
        ])
    class2YValues = np.array([
        3.0, 4.2, 4.7, 2.6, 3.5, 3.9, 4.4, 2.9, 4.1, 3.7,
        -3.0, -4.2, -4.7, -2.6, -3.5, -3.9, -4.4, -2.9, -4.1, -3.7,
        2.4, 3.8, 4.2, 3.1, 2.7, 4.7, 3.4, 2.5, 2.0, 4.3, 3.6,
        -2.4, -3.8, -4.2, -3.1, -2.7, -4.7, -3.4, -2.5, -2.0, -4.3, -3.6,
        1.7, 2.6, 4.5, 3.2, 1.9, 4.1, 0.6, 1.0, 2.4, 1.5, 3.8, 2.6, 4.7, 0.3, 3.3, 0.7, 4.0,
        -1.7, -2.6, -4.5, -3.2, -1.9, -4.1, -0.6, -1.0, -2.4, -1.5, -3.8, -2.6, -4.7, -0.3, -3.3, -0.7, -4.0,
        0.7, 2.0, 3.4, 2.5, 1.6, 4.6, 0.4, 1.1, 2.1, 0.9, 3.7, 2.9, 4.3, 1.7, 4.1,
        -0.7, -2.0, -3.4, -2.5, -1.6, -4.6, -0.4, -1.1, -2.1, -0.9, -3.7, -2.9, -4.3, -1.7, -4.1,
        0.9, 3.6, 2.8, 1.3, 2.0, 4.1, 2.3, 0.7, 4.5, 3.2, 1.6, 3.9,
        -0.9, -3.6, -2.8, -1.3, -2.0, -4.1, -2.3, -0.7, -4.5, -3.2, -1.6, -3.9,
        0.4, 0.0, 0.2,
        3.0, 4.2, 4.7, 2.6, 3.5, 3.9, 4.4, 2.9, 4.1, 3.7,
        -3.0, -4.2, -4.7, -2.6, -3.5, -3.9, -4.4, -2.9, -4.1, -3.7,
        2.4, 3.8, 4.2, 3.1, 2.7, 4.7, 3.4, 2.5, 2.0, 4.3, 3.6,
        -2.4, -3.8, -4.2, -3.1, -2.7, -4.7, -3.4, -2.5, -2.0, -4.3, -3.6,
        1.7, 2.6, 4.5, 3.2, 1.9, 4.1, 0.6, 1.0, 2.4, 1.5, 3.8, 2.6, 4.7, 0.3, 3.3, 0.7, 4.0,
        -1.7, -2.6, -4.5, -3.2, -1.9, -4.1, -0.6, -1.0, -2.4, -1.5, -3.8, -2.6, -4.7, -0.3, -3.3, -0.7, -4.0,
        0.7, 2.0, 3.4, 2.5, 1.6, 4.6, 0.4, 1.1, 2.1, 0.9, 3.7, 2.9, 4.3, 1.7, 4.1,
        -0.7, -2.0, -3.4, -2.5, -1.6, -4.6, -0.4, -1.1, -2.1, -0.9, -3.7, -2.9, -4.3, -1.7, -4.1,
        0.9, 3.6, 2.8, 1.3, 2.0, 4.1, 2.3, 0.7, 4.5, 3.2, 1.6, 3.9,
        -0.9, -3.6, -2.8, -1.3, -2.0, -4.1, -2.3, -0.7, -4.5, -3.2, -1.6, -3.9,
        0.4, 0.0, 0.2
        ])
    class2ZValues = np.array([max(maxZ - math.sqrt(i**2 + j**2), 0.0) for i, j in zip(class2XValues, class2YValues)])
    class2Color = '#FF0000'  # Red
    class2Size = 30

    # Aggregate all class information.
    scatterXValues = [class1XValues, class2XValues]  # The X values for the classes.
    scatterXAllValues = [j for i in scatterXValues for j in i]  # A list of the X values for all the datapoints.
    scatterYValues = [class1YValues, class2YValues]  # The Y values for the classes.
    scatterYAllValues = [j for i in scatterYValues for j in i]  # A list of the Y values for all the datapoints.
    scatterZValues = [class1ZValues, class2ZValues]  # The Z values for the classes.
    scatterZAllValues = [j for i in scatterZValues for j in i]  # A list of the Z values for all the datapoints.
    colors = [class1Color, class2Color]  # The colors for the classes.
    sizes = [class1Size, class2Size]  # The size of the markers for the scatterplots.

    # Create the figure, the grids for the subplots and determine the spacing for the subplots.
    currentFigure = plt.figure()
    gsTopRow = gridspec.GridSpec(2, 4)
    gsBotRow = gridspec.GridSpec(2, 4)
    gsTopRow.update(left=0.005, right=0.995, bottom=0.05, top=1, wspace=0.05)#, hspace=0.05)
    gsBotRow.update(left=0.005, right=0.995, bottom=0.05, top=1, wspace=0.05)#, hspace=0.05)

    # Create the scatterplot for the initial graph with no boundary.
    plotWithoutBoundary = plt.subplot(gsTopRow[0, 0:2])
    plotWithoutBoundary.axis('scaled')
    scatterplot.graphGeneration(scatterXValues, scatterYValues, currentFigure=currentFigure, colors=colors, sizes=sizes)
    plotWithoutBoundary.set_xlim(left=minX, right=maxX)
    plotWithoutBoundary.set_ylim(bottom=minY, top=maxY)

    # Create the 3D graph showing the new division.
    scatter3D = plt.subplot(gsTopRow[0, 2:])
    scatter3D.axis('scaled')

    # Create the scatterplot for the final graph with boundary.
    plotWithBoundary = plt.subplot(gsBotRow[1, 1:3])
    plotWithBoundary.axis('scaled')
    scatterplot.graphGeneration(scatterXValues, scatterYValues, currentFigure=currentFigure, colors=colors, sizes=sizes)
    plotWithBoundary.set_xlim(left=minX, right=maxX)
    plotWithBoundary.set_ylim(bottom=minY, top=maxY)
    currentFigure.gca().add_artist(plt.Circle((0, 0), circleWidth, fill=False))

    # Make all the tick marks invisible, and label the x axes.
    labels = ['(c)', '(b)', '(a)']
    for ax in currentFigure.get_axes():
        removeTickMarks(ax, xAxis=True, yAxis=True)
        currentLabel = labels.pop()
        setLabels(ax, xLabel=currentLabel)
        ax.xaxis.set_label_coords(0.5, -0.025)

    plt.savefig(figureSaveLocation + '2D', bbox_inches='tight', transparent=True)

    # Create the 3D graph showing the new division.
    currentFigure = plt.figure()
    gs = gridspec.GridSpec(10, 10)
    gs.update(left=0, right=1, bottom=0, top=1, wspace=0.05)#, hspace=0.05)
    scatter3D = plt.subplot(gs[1:-1, 1:-1], projection='3d')
    scatter3D.axis('scaled')
    scatter3D.set_xlim3d(minX, maxX)
    scatter3D.set_ylim3d(minY, maxY)
    scatter3D.set_zlim3d(0, maxZ)
    scatterplot3D.graphGeneration(scatterXValues, scatterYValues, scatterZValues, currentFigure=currentFigure, colors=colors, sizes=sizes)
    X = np.arange(minX, maxX + 1)
    Y = np.arange(minY, maxY + 1)
    X, Y = np.meshgrid(X, Y)
    Z = np.zeros(np.shape(X)) + (maxZ - circleWidth)
    surface3D.graphGeneration([X], [Y], [Z], currentFigure=currentFigure, color=['black'], edgeColor=['black'], transparency=[0.2])
    removeTickMarks(scatter3D, xAxis=True, yAxis=True)
    for a in scatter3D.w_zaxis.get_ticklines()+scatter3D.w_zaxis.get_ticklabels():
	    # Used to remove the z axis ticks and tick labels.
        a.set_visible(False)
    scatter3D.view_init(2, 104)  # Rotate figure to nicer angle.

    plt.savefig(figureSaveLocation + '3D', bbox_inches='tight', transparent=True)
    plt.show()


def setLabels(axes, xLabel='', yLabel=''):
    """Set the X and Y labels of the axes.
    """

    axes.set_xlabel(xLabel)
    axes.set_ylabel(yLabel)

def removeTickMarks(axes, xAxis=False, yAxis=False):
    """Removes all tick marks.
    """

    if xAxis:
        axes.set_xticks([])
    if yAxis:
        axes.set_yticks([])


if __name__ == '__main__':
    main(sys.argv[1])