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
import linegraph

def main(figureSaveLocation):
    """Create an image for demonstrating feature subset selection.
    """

    # Initialise the figure.
    currentFigure = plt.figure()
    gs = gridspec.GridSpec(10, 10)
    gs.update(left=0, right=1, bottom=0, top=1, wspace=0.05)
    axes = plt.subplot(gs[1:-1, 1:-1])
    removeTickMarks(axes, xAxis=True, yAxis=True)
    axes.spines['top'].set_visible(False)
    axes.spines['right'].set_visible(False)
    axes.spines['bottom'].set_visible(False)
    axes.spines['left'].set_visible(False)
    axes.set_xlim(left=-1, right=11)
    axes.set_ylim(bottom=-1, top=9)

    # Define the nodes.
    numberOfNodes = 16
    nodeNames = ['{}\n0.0', '{A}\n0.25', '{B}\n0.1', '{C}\n0.2', '{D}\n0.3', '{A,B}\n0.8', '{A,C}\n0.75', '{A,D}\n0.55', '{B,C}\n0.35', '{B,D}\n0.5',
                 '{C,D}\n0.4', '{A,B,C}\n0.6', '{A,B,D}\n0.5', '{A,C,D}\n0.7', '{B,C,D}\n0.55', '{A,B,C,D}\n0.6']
    nodeCenterXValues = [  5, 2, 4, 6, 8, 0, 2, 4, 6, 8, 10, 2, 4, 6, 8, 5]
    nodeCenterYValues = [7.5, 6, 6, 6, 6, 4, 4, 4, 4, 4,  4, 2, 2, 2, 2, 0.5]

    # Define the edges.
    edges = [[nodeNames[0], nodeNames[1]], [nodeNames[0], nodeNames[2]], [nodeNames[0], nodeNames[3]], [nodeNames[0], nodeNames[4]],
             [nodeNames[1], nodeNames[5]], [nodeNames[1], nodeNames[6]], [nodeNames[1], nodeNames[7]],
             [nodeNames[2], nodeNames[5]], [nodeNames[2], nodeNames[8]], [nodeNames[2], nodeNames[9]],
             [nodeNames[3], nodeNames[6]], [nodeNames[3], nodeNames[8]], [nodeNames[3], nodeNames[10]],
             [nodeNames[4], nodeNames[7]], [nodeNames[4], nodeNames[9]], [nodeNames[4], nodeNames[10]],
             [nodeNames[5], nodeNames[11]], [nodeNames[5], nodeNames[12]],
             [nodeNames[6], nodeNames[11]], [nodeNames[6], nodeNames[13]],
             [nodeNames[7], nodeNames[12]], [nodeNames[7], nodeNames[13]],
             [nodeNames[8], nodeNames[11]], [nodeNames[8], nodeNames[14]],
             [nodeNames[9], nodeNames[12]], [nodeNames[9], nodeNames[14]],
             [nodeNames[10], nodeNames[13]], [nodeNames[10], nodeNames[14]],
             [nodeNames[11], nodeNames[15]],
             [nodeNames[12], nodeNames[15]],
             [nodeNames[13], nodeNames[15]],
             [nodeNames[14], nodeNames[15]]
            ]
    edgeXValues = [[nodeCenterXValues[nodeNames.index(i[0])], nodeCenterXValues[nodeNames.index(i[1])]] for i in edges]
    edgeYValues = [[nodeCenterYValues[nodeNames.index(i[0])], nodeCenterYValues[nodeNames.index(i[1])]] for i in edges]

    # Plot the graph.
    for i, j in zip(nodeCenterXValues, nodeCenterYValues):
        if j > 5:
            rect = patches.Rectangle(xy=[i - 0.3, j - 0.35], width=0.6, height=0.7)
        elif j > 3:
            rect = patches.Rectangle(xy=[i - 0.35, j - 0.325], width=0.7, height=0.65)
        elif j > 1:
            rect = patches.Rectangle(xy=[i - 0.5, j - 0.325], width=1, height=0.65)
        else:
            rect = patches.Rectangle(xy=[i - 0.6, j - 0.325], width=1.2, height=0.65)
        rect.set_edgecolor('none')
        rect.set_facecolor('white')
        rect.set_zorder(1)
        axes.add_artist(rect)
    addtext.graphGeneration(nodeCenterXValues, nodeCenterYValues, nodeNames, currentFigure=currentFigure, sizes=[10] * numberOfNodes,
        colors=['black' for i in range(numberOfNodes)], zorders=[2 for i in range(numberOfNodes)])
    linegraph.graphGeneration(edgeXValues, edgeYValues, currentFigure=currentFigure, markerSizes=[0 for i in range(numberOfNodes)],
        lineStyles=['-' for i in edges], lineWidths=[1 for i in edges], zorders=[0 for i in range(numberOfNodes)])

    plt.savefig(figureSaveLocation, bbox_inches='tight', transparent=True)

def removeTickMarks(axes, xAxis=False, yAxis=False):
    """Removes all tick marks for the given axes.
    """

    if xAxis:
        axes.set_xticks([])
    if yAxis:
        axes.set_yticks([])


if __name__ == '__main__':
    main(sys.argv[1])