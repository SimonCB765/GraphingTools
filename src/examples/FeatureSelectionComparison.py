import math
import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import os
import sys

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)
import addtext

def main(figureSaveLocation):
    """Create an image for demonstrating feature subset selection.
    """

    # Create the figure, the grids for the subplots and determine the spacing for the subplots.
    currentFigure = plt.figure()
    gs = gridspec.GridSpec(1, 3)
    gs.update(left=0.005, right=0.995, bottom=0.05, top=1, wspace=0.05)#, hspace=0.05)

    # Create the neighbourhood/degree/support graph.
    backwardsEliminationGraph = plt.subplot(gs[0, 0])
    draw_graph(currentFigure, edges=[['{A,C}', '{A}'], ['{A,C}', '{C}']])

    # Create the non-complement graph.
    forwardSelectionGraph = plt.subplot(gs[0, 1])
    draw_graph(currentFigure, edges=[['{A,C}', '{A,B,C}'], ['{A,C}', '{A,C,D}']])

    # Create the complement graph.
    geneticAlgorithmGraph = plt.subplot(gs[0, 2])
    draw_graph(currentFigure, edges=[['{A,C}', '{A}'], ['{A,C}', '{C}'], ['{A,C}', '{A,B,C}'], ['{A,C}', '{A,C,D}']])

    # Make all the tick marks invisible, and label the x axes.
    labels = ['(c)', '(b)', '(a)']
    for ax in currentFigure.get_axes():
        removeTickMarks(ax, xAxis=True, yAxis=True)
        currentLabel = labels.pop()
        setLabels(ax, xLabel=currentLabel)
        ax.xaxis.set_label_coords(0.5, -0.025)

    plt.savefig(figureSaveLocation, bbox_inches='tight', transparent=True)

def draw_graph(currentFigure, edges):
    """Draw the feature sets.
    """

    # Plot the graph.
    plot = currentFigure.gca()
    plot.axis('scaled')
    plot.spines['top'].set_visible(False)
    plot.spines['right'].set_visible(False)
    plot.spines['bottom'].set_visible(False)
    plot.spines['left'].set_visible(False)
    plot.set_xlim(left=-3.5, right=3.5)
    plot.set_ylim(bottom=-2.5, top=2.5)

    # Define the nodes.
    numberOfNodes = 5
    nodeNames = ['{A}', '{C}', '{A,C}', '{A,B,C}', '{A,C,D}']
    nodeCenterXValues = [-2, 2, 0, -2,  2]
    nodeCenterYValues = [ 2, 2, 0, -2, -2]

    # Define the edges.
    for i in edges:
        edgeStartX = (nodeCenterXValues[nodeNames.index(i[1])] - nodeCenterXValues[nodeNames.index(i[0])]) * (1 / 7)
        edgeStartY = (nodeCenterYValues[nodeNames.index(i[1])] - nodeCenterYValues[nodeNames.index(i[0])]) * (1 / 7)
        edgeEndX = (nodeCenterXValues[nodeNames.index(i[1])] - nodeCenterXValues[nodeNames.index(i[0])]) * (3 / 5)
        edgeEndY = (nodeCenterYValues[nodeNames.index(i[1])] - nodeCenterYValues[nodeNames.index(i[0])]) * (3 / 5)
        plot.arrow(nodeCenterXValues[nodeNames.index(i[0])] + edgeStartX, nodeCenterYValues[nodeNames.index(i[0])] + edgeStartY,
                   nodeCenterXValues[nodeNames.index(i[0])] + edgeEndX, nodeCenterYValues[nodeNames.index(i[0])] + edgeEndY,
                   head_width=0.25, head_length=0.25, fc='k', ec='k')

    # Plot the graph.
    addtext.graphGeneration(nodeCenterXValues, nodeCenterYValues, nodeNames, currentFigure=currentFigure, sizes=[12] * numberOfNodes,
        colors=['black' for i in range(numberOfNodes)], zorders=[2 for i in range(numberOfNodes)])

def setLabels(axes, xLabel='', yLabel=''):
    """Set the X and Y labels of the axes.
    """

    axes.set_xlabel(xLabel)
    axes.set_ylabel(yLabel)

def removeTickMarks(axes, xAxis=False, yAxis=False):
    """Removes all tick marks for the given axes.
    """

    if xAxis:
        axes.set_xticks([])
    if yAxis:
        axes.set_yticks([])


if __name__ == '__main__':
    main(sys.argv[1])