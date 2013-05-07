import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
import numpy as np
import sys

import os
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)
import barchart
import linegraph
import scatterplot


def main(figureSaveLocation):
    """Create an image that shows the impact that different splits have on the purity of two child nodes in a decision tree.

    @type figureSaveLocation - str
    @use  figureSaveLocation - The location where the figure will be saved.
    """

    # Class 1 data and control variables.
    class1X = np.array([0.0, 0.3, 0.7, 0.8, 1.1, 1.2, 1.4, 1.7, 1.9, 2.2, 2.3, 2.5, 2.6, 2.8, 3.2, 3.3, 3.5, 3.75])
    class1Y = np.array([3.3, 0.2, 4.3, 1.7, 2.2, 0.7, 3.4, 5.5, 2.8, 2.4, 3.1, 0.3, 5.6, 1.3, 3.2, 4.5, 1.0, 2.1])
    class1Color = '#000000'  # Black
    class1Size = 30
    class1BarXLoc = 0
    class1BarWidth = 0.5

    # Class 2 data and control variables.
    class2X = np.array([0.1, 0.3, 0.5, 0.8, 1.0, 1.2, 1.3, 1.4, 1.7, 2.1, 2.4, 2.5, 2.7, 2.9, 3.2, 3.4, 3.5, 3.75])
    class2Y = np.array([4.3, 6.5, 5.3, 7.3, 3.3, 5.4, 6.9, 7.6, 3.7, 4.8, 6.1, 7.8, 5.2, 4.3, 6.3, 7.2, 5.1, 6.2])
    class2Color = '#FF0000'  # Red
    class2Size = 30
    class2BarXLoc = 0.75
    class2BarWidth = 0.5

    # Class 3 data and control variables.
    class3X = np.array([4.25, 4.4, 4.6, 4.7, 5.0, 5.1, 5.3, 5.6, 6.0, 6.3, 6.3, 6.4, 6.6, 6.9, 7.3, 7.5, 7.6, 7.8])
    class3Y = np.array([7.3, 5.3, 6.1, 7.9, 4.3, 3.4, 5.9, 7.0, 5.8, 3.1, 4.7, 7.4, 6.2, 3.3, 7.3, 5.2, 6.4, 6.9])
    class3Color = '#00FF00'  # Green
    class3Size = 30
    class3BarXLoc = 1.5
    class3BarWidth = 0.5

    # Class 4 data and control variables.
    class4X = np.array([4.3, 4.5, 4.6, 4.8, 5.0, 5.2, 5.4, 5.7, 5.8, 6.1, 6.3, 6.5, 6.7, 7.0, 7.2, 7.5, 7.6, 8.0])
    class4Y = np.array([3.3, 1.2, 4.4, 0.7, 2.6, 1.7, 0.4, 4.7, 3.2, 1.7, 0.3, 3.4, 2.6, 4.9, 2.2, 3.7, 1.3, 2.1])
    class4Color = '#0000FF'  # Blue
    class4Size = 30
    class4BarXLoc = 2.25
    class4BarWidth = 0.5

    # Aggregate all class information.
    scatterXValues = [class1X, class2X, class3X, class4X]  # The X values for the four different classes.
    scatterXAllValues = [j for i in scatterXValues for j in i]  # A list of the X values for all the datapoints.
    scatterXMin = min(scatterXAllValues)
    scatterXMax = max(scatterXAllValues)
    scatterYValues = [class1Y, class2Y, class3Y, class4Y]  # The Y values for the four different classes.
    scatterYAllValues = [j for i in scatterYValues for j in i]  # A list of the Y values for all the datapoints.
    scatterYMin = min(scatterYAllValues)
    scatterYMax = max(scatterYAllValues)
    colors = [class1Color, class2Color, class3Color, class4Color]  # The colors for the different classes.
    sizes = [class1Size, class2Size, class3Size, class4Size]  # The size of the markers for the scatterplots.
    barChartXLocations = [class1BarXLoc, class2BarXLoc, class3BarXLoc, class4BarXLoc]  # The locations on the X axis of the bars in the barchart.
    barChartWidths = [class1BarWidth, class2BarWidth, class3BarWidth, class4BarWidth]  # The widths of the individual bars.
    scatterZorders = [0, 1, 2, 3]  # Used to determine which points should be plotted on top of which other ones (class 1 is on the bottom and 4 on the top).
    lineZorder = [min(scatterZorders) - 1]  # Put the line below all points.
    midPlotHorizontalSplit = 4.0  # The location on the Y axis to make the split.
    botPlotVerticalSplit = 4.0  # The location on the X axis to make the split.

    # Create the figure, the grids for the subplots and determine the spacing for the subplots.
    currentFigure = plt.figure()
    gsTopRow = gridspec.GridSpec(3, 6)
    gsMidRow = gridspec.GridSpec(3, 6)
    gsBotRow = gridspec.GridSpec(3, 6)
    gsTopRow.update(left=0.005, right=0.995, bottom=0.05, top=1, wspace=0.05)#, hspace=0.05)
    gsMidRow.update(left=0.005, right=0.995, bottom=0.05, top=1, wspace=0.05)#, hspace=0.05)
    gsBotRow.update(left=0.005, right=0.995, bottom=0.05, top=1, wspace=0.05)#, hspace=0.05)

    # Create the scatter plots of the data, and for the middle and bottom rows add a horizontal and vertical line respectively.
    topRowScatterPlot = plt.subplot(gsTopRow[0, 1:3])  # Scatter plot for the top row takes up the second and thrid of the six columns.
    scatterplot.graphGeneration(scatterXValues, scatterYValues, currentFigure=currentFigure, colors=colors, sizes=sizes, zorders=scatterZorders)
    topRowScatterPlot.set_xlim(left=scatterXMin - 0.5, right=scatterXMax + 0.5)
    topRowScatterPlot.set_ylim(bottom=scatterYMin - 0.5, top=scatterYMax + 0.5)
    midRowScatterPlot = plt.subplot(gsMidRow[1, :2])  # Scatter plot for the middle row takes up the first and second of the six columns.
    scatterplot.graphGeneration(scatterXValues, scatterYValues, currentFigure=currentFigure, colors=colors, sizes=sizes, zorders=scatterZorders)
    midRowScatterPlot.set_xlim(left=scatterXMin - 0.5, right=scatterXMax + 0.5)
    midRowScatterPlot.set_ylim(bottom=scatterYMin - 0.5, top=scatterYMax + 0.5)
    linegraph.graphGeneration([[scatterXMin - 0.5, scatterXMax + 0.5]], [[midPlotHorizontalSplit, midPlotHorizontalSplit]], currentFigure=currentFigure, markerSizes=[0], lineWidths=[2], zorders=lineZorder)
    botRowScatterPlot = plt.subplot(gsBotRow[2, :2])  # Scatter plot for the bottom row takes up the first and second of the six columns.
    scatterplot.graphGeneration(scatterXValues, scatterYValues, currentFigure=currentFigure, colors=colors, sizes=sizes, zorders=scatterZorders)
    botRowScatterPlot.set_xlim(left=scatterXMin - 0.5, right=scatterXMax + 0.5)
    botRowScatterPlot.set_ylim(bottom=scatterYMin - 0.5, top=scatterYMax + 0.5)
    linegraph.graphGeneration([[botPlotVerticalSplit, botPlotVerticalSplit]], [[scatterYMin - 0.5, scatterYMax + 0.5]], currentFigure=currentFigure, markerSizes=[0], lineWidths=[2], zorders=lineZorder)

    # Create the bar chart for the top row.
    topRowBarChart = plt.subplot(gsTopRow[0, 3:-1])  # Bar chart for the top row takes up the fourth and fifth of the six columns.
    class1BarHeight = len(class1X)
    class2BarHeight = len(class2X)
    class3BarHeight = len(class3X)
    class4BarHeight = len(class4X)
    barHeightValues = [class1BarHeight, class2BarHeight, class3BarHeight, class4BarHeight]
    totalObservations = sum(barHeightValues)  # Determine how many datapoints are in the scatter plot.
    barHeightValues = [i / totalObservations for i in barHeightValues]  # The height of each bar is the fraction of the total datapoints from the class the bar corresponds to.
    barchart.graphGeneration(barChartXLocations, barHeightValues, currentFigure=currentFigure, colors=colors, widths=barChartWidths)
    topRowBarChart.set_xlim(left=min(barChartXLocations) - 0.5, right=max(barChartXLocations) + (0.5 + class4BarWidth))  # Get the same amount of white space on the left of the class 1 bar and right of the class 4 bar.
    topRowBarChart.set_ylim(bottom=0.0, top=1.0)

    # Create the left bar chart for the middle row.
    midRowLeftBarChart = plt.subplot(gsMidRow[1, 2:4])  # Left bar chart for the middle row takes up the third and fourth of the six columns.
    class1LeftPlotBarHeight = len([i for i in class1Y if i <= midPlotHorizontalSplit])  # The number of class 1 points in the left split is the number with Y value <= the Y value of the horizontal split.
    class2LeftPlotBarHeight = len([i for i in class2Y if i <= midPlotHorizontalSplit])  # The number of class 2 points in the left split is the number with Y value <= the Y value of the horizontal split.
    class3LeftPlotBarHeight = len([i for i in class3Y if i <= midPlotHorizontalSplit])  # The number of class 3 points in the left split is the number with Y value <= the Y value of the horizontal split.
    class4LeftPlotBarHeight = len([i for i in class4Y if i <= midPlotHorizontalSplit])  # The number of class 4 points in the left split is the number with Y value <= the Y value of the horizontal split.
    barHeightValues = [class1LeftPlotBarHeight, class2LeftPlotBarHeight, class3LeftPlotBarHeight, class4LeftPlotBarHeight]
    totalObservationsInSplit = sum(barHeightValues)  # Determine how many datapoints are below or on the line in the scatter plot.
    barHeightValues = [i / totalObservationsInSplit for i in barHeightValues] # The height of each bar is the fraction of the total datapoints from the class the bar corresponds to.
    barchart.graphGeneration(barChartXLocations, barHeightValues, currentFigure=currentFigure, colors=colors, widths=barChartWidths)
    midRowLeftBarChart.set_xlim(left=min(barChartXLocations) - 0.5, right=max(barChartXLocations) + (0.5 + class4BarWidth))  # Get the same amount of white space on the left of the class 1 bar and right of the class 4 bar.
    midRowLeftBarChart.set_ylim(bottom=0.0, top=1.0)

    # Create the right bar chart for the middle row.
    midRowRightBarChart = plt.subplot(gsMidRow[1, 4:])  # Right bar chart for the middle row takes up the fifth and sixth of the six columns.
    class1RightPlotBarHeight = len([i for i in class1Y if i > midPlotHorizontalSplit])  # The number of class 1 points in the right split is the number with Y value > the Y value of the horizontal split.
    class2RightPlotBarHeight = len([i for i in class2Y if i > midPlotHorizontalSplit])  # The number of class 2 points in the right split is the number with Y value > the Y value of the horizontal split.
    class3RightPlotBarHeight = len([i for i in class3Y if i > midPlotHorizontalSplit])  # The number of class 3 points in the right split is the number with Y value > the Y value of the horizontal split.
    class4RightPlotBarHeight = len([i for i in class4Y if i > midPlotHorizontalSplit])  # The number of class 4 points in the right split is the number with Y value > the Y value of the horizontal split.
    barHeightValues = [class1RightPlotBarHeight, class2RightPlotBarHeight, class3RightPlotBarHeight, class4RightPlotBarHeight]
    totalObservationsInSplit = sum(barHeightValues)  # Determine how many datapoints are above the line in the scatter plot.
    barHeightValues = [i / totalObservationsInSplit for i in barHeightValues] # The height of each bar is the fraction of the total datapoints from the class the bar corresponds to.
    barchart.graphGeneration(barChartXLocations, barHeightValues, currentFigure=currentFigure, colors=colors, widths=barChartWidths)
    midRowRightBarChart.set_xlim(left=min(barChartXLocations) - 0.5, right=max(barChartXLocations) + (0.5 + class4BarWidth))  # Get the same amount of white space on the left of the class 1 bar and right of the class 4 bar.
    midRowRightBarChart.set_ylim(bottom=0.0, top=1.0)

    # Create the left bar chart for the bottom row.
    botRowLeftBarChart = plt.subplot(gsBotRow[2, 2:4])  # Left bar chart for the bottom row takes up the third and fourth of the six columns.
    class1LeftPlotBarHeight = len([i for i in class1X if i <= botPlotVerticalSplit])  # The number of class 1 points in the right split is the number with X value <= the X value of the vertical split.
    class2LeftPlotBarHeight = len([i for i in class2X if i <= botPlotVerticalSplit])  # The number of class 2 points in the right split is the number with X value <= the X value of the vertical split.
    class3LeftPlotBarHeight = len([i for i in class3X if i <= botPlotVerticalSplit])  # The number of class 3 points in the right split is the number with X value <= the X value of the vertical split.
    class4LeftPlotBarHeight = len([i for i in class4X if i <= botPlotVerticalSplit])  # The number of class 4 points in the right split is the number with X value <= the X value of the vertical split.
    barHeightValues = [class1LeftPlotBarHeight, class2LeftPlotBarHeight, class3LeftPlotBarHeight, class4LeftPlotBarHeight]
    totalObservationsInSplit = sum(barHeightValues)  # Determine how many datapoints are to the left or on the line in the scatter plot.
    barHeightValues = [i / totalObservationsInSplit for i in barHeightValues] # The height of each bar is the fraction of the total datapoints from the class the bar corresponds to.
    barchart.graphGeneration(barChartXLocations, barHeightValues, currentFigure=currentFigure, colors=colors, widths=barChartWidths)
    botRowLeftBarChart.set_xlim(left=min(barChartXLocations) - 0.5, right=max(barChartXLocations) + (0.5 + class4BarWidth))  # Get the same amount of white space on the left of the class 1 bar and right of the class 4 bar.
    botRowLeftBarChart.set_ylim(bottom=0.0, top=1.0)

    # Create the rigt bar chart for the bottom row.
    botRowRightBarChart = plt.subplot(gsBotRow[2, 4:])  # Right bar chart for the bottom row takes up the fifth and sixth of the six columns.
    class1RightPlotBarHeight = len([i for i in class1X if i > botPlotVerticalSplit])  # The number of class 1 points in the right split is the number with X value > the X value of the vertical split.
    class2RightPlotBarHeight = len([i for i in class2X if i > botPlotVerticalSplit])  # The number of class 2 points in the right split is the number with X value > the X value of the vertical split.
    class3RightPlotBarHeight = len([i for i in class3X if i > botPlotVerticalSplit])  # The number of class 3 points in the right split is the number with X value > the X value of the vertical split.
    class4RightPlotBarHeight = len([i for i in class4X if i > botPlotVerticalSplit])  # The number of class 4 points in the right split is the number with X value > the X value of the vertical split.
    barHeightValues = [class1RightPlotBarHeight, class2RightPlotBarHeight, class3RightPlotBarHeight, class4RightPlotBarHeight]
    totalObservationsInSplit = sum(barHeightValues)  # Determine how many datapoints are to the right of the line in the scatter plot.
    barHeightValues = [i / totalObservationsInSplit for i in barHeightValues] # The height of each bar is the fraction of the total datapoints from the class the bar corresponds to.
    barchart.graphGeneration(barChartXLocations, barHeightValues, currentFigure=currentFigure, colors=colors, widths=barChartWidths)
    botRowRightBarChart.set_xlim(left=min(barChartXLocations) - 0.5, right=max(barChartXLocations) + (0.5 + class4BarWidth))  # Get the same amount of white space on the left of the class 1 bar and right of the class 4 bar.
    botRowRightBarChart.set_ylim(bottom=0.0, top=1.0)

    # Make all the tick marks invisible, and label the x axes.
    labels = ['(h)', '(g)', '(f)', '(e)', '(d)', '(c)', '(b)', '(a)']
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