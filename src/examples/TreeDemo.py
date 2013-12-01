import math
import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import sys

import os
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)
import addtext
import linegraph
import patchplotting


def main(treeSaveLocation):
    """Create an image of a tree.

    @type treeSaveLocation - str
    @use  treeSaveLocation - The location where the image of the tree will be saved.
    """

    # Define the positions of the non-leaf nodes in the tree.
    nonLeafNodeCoords = {'0' : {'x' : 5, 'y' : 9},
                         '1' : {'x' : 2.5, 'y' : 7},
                         '2' : {'x' : 7.5, 'y' : 7},
                         '3' : {'x' : 1.25, 'y' : 5},
                         '4' : {'x' : 3.75, 'y' : 5},
                         '5' : {'x' : 6.25, 'y' : 5},
                         '9' : {'x' : 3.125, 'y' : 3}
                        }
    leafNodeCoords = {'6' : {'x' : 8.75, 'y' : 5},
                      '7' : {'x' : 0.625, 'y' : 3},
                      '8' : {'x' : 1.875, 'y' : 3},
                      '10' : {'x' : 4.375, 'y' : 3},
                      '11' : {'x' : 5.625, 'y' : 3},
                      '12' : {'x' : 6.875, 'y' : 3},
                      '13' : {'x' : 2.375, 'y' : 1},
                      '14' : {'x' : 3.875, 'y' : 1}
                     }

    # Define the edge relationships.
    edges = {'0' : ['1', '2'],
             '1' : ['3', '4'],
             '2' : ['5' ,'6'],
             '3' : ['7', '8'],
             '4' : ['9', '10'],
             '5' : ['11', '12'],
             '9' : ['13', '14']
            }

    # Define the node properties.
    nodeWidth = 1.0
    nodeColour = 'white'

    # Define the axis size.
    axisMinValue = 0.0
    axisMaxValue = 10.0

    # Determine the node centres and labels.
    nodeCenterXValues = [nonLeafNodeCoords[i]['x'] for i in nonLeafNodeCoords] + [leafNodeCoords[i]['x'] for i in leafNodeCoords]
    nodeCenterYValues = [nonLeafNodeCoords[i]['y'] for i in nonLeafNodeCoords] + [leafNodeCoords[i]['y'] for i in leafNodeCoords]
    nodeLabels = [i for i in nonLeafNodeCoords] + [i for i in leafNodeCoords]

    # Determine the tree edges.
    treeEdgesXValues = []
    treeEdgesYValues = []
    for i in edges:
        iCentreXValue = nonLeafNodeCoords[i]['x']
        iCentreYValue = nonLeafNodeCoords[i]['y']
        children = edges[i]
        for j in children:
            if j in nonLeafNodeCoords:
                jCoords = nonLeafNodeCoords[j]
            else:
                jCoords = leafNodeCoords[j]
            treeEdgesXValues.append([iCentreXValue, jCoords['x']])
            treeEdgesYValues.append([iCentreYValue, jCoords['y']])

    # Create the plot for the tree.
    currentFigure = plt.figure()
    gsTree = gridspec.GridSpec(10, 10)
    gsTree.update(left=0, right=1, bottom=0, top=1, wspace=0.05)#, hspace=0.05)
    treePlot = plt.subplot(gsTree[1:-1, 1:-1])
    treePlot.set_xlim(left=axisMinValue, right=axisMaxValue)
    treePlot.set_ylim(bottom=axisMinValue, top=axisMaxValue)
    nodes = [patches.Circle((nodeCenterXValues[i], nodeCenterYValues[i]), nodeWidth / 2) for i in range(len(nodeCenterXValues))]
    patchplotting.graphGeneration(nodes, currentFigure=currentFigure, faceColors=[nodeColour] * len(nodes), zorders=[-1])
    addtext.graphGeneration(nodeCenterXValues, nodeCenterYValues, nodeLabels, currentFigure=currentFigure, sizes=[15] * len(nodeLabels), zorders=list(range(len(nodeLabels))))
    linegraph.graphGeneration(treeEdgesXValues, treeEdgesYValues, currentFigure=currentFigure, markerSizes=[0] * len(treeEdgesYValues), zorders=[-len(treeEdgesXValues)])
    removeTickMarks(treePlot, xAxis=True, yAxis=True)

    plt.savefig(treeSaveLocation, bbox_inches='tight', transparent=True)

    sys.exit()

    # Define the number of nodes in the tree and their labels.
    numberOfNodes = 15
    nodesWithOutgoingEdge = int((numberOfNodes - 1) / 2)
    nodeLabels = [str(i) for i in range(numberOfNodes)]

    # Define the axis size.
    axisMinValue = 0.0
    axisMaxValue = 10.0

    # Define the tree node sizes and positions.
    nodeWidth = 1.0
    nodeHeight = 1.0
    gapBetweenLevels = 1.0
    gapBetweenCousins = 0.5
    nodeDepths = [int(math.log(i+1,2)) for i in range(len(nodeLabels))]
    maxDepth = max(nodeDepths)
    nodesAtDepth = [(2**nodeDepths[i], nodeDepths[:i].count(nodeDepths[i]) + 1) for i in range(len(nodeDepths))]  # The depth of the node along with the position on the row (leftmost is 1).
    nodeCenterXValues = []
    nodeCenterYValues = [axisMaxValue - (i * nodeHeight + ((i + 1) * gapBetweenLevels) + (nodeHeight / 2)) for i in nodeDepths]
    for i in range(len(nodeLabels)):
        splits = [(axisMaxValue / nodesAtDepth[i][0]) * j for j in range(nodesAtDepth[i][0] + 1)]
        positions = [(splits[j] + splits[j+1]) / 2 for j in range(nodesAtDepth[i][0])]
        nodeCenterXValues.append(positions[nodesAtDepth[i][1] - 1])
    treeEdgesXValues = []
    treeEdgesYValues = []
    for i in range(nodesWithOutgoingEdge):
        leftChildIndex = int((i * 2) + 1)
        rightChildIndex = int((i * 2) + 2)
        treeEdgesXValues += [[nodeCenterXValues[i], nodeCenterXValues[leftChildIndex]], [nodeCenterXValues[i], nodeCenterXValues[rightChildIndex]]]
        treeEdgesYValues += [[nodeCenterYValues[i], nodeCenterYValues[leftChildIndex]], [nodeCenterYValues[i], nodeCenterYValues[rightChildIndex]]]

    # Create the plot for the tree.
    currentFigure = plt.figure()
    gsTree = gridspec.GridSpec(10, 10)
    gsTree.update(left=0, right=1, bottom=0, top=1, wspace=0.05)#, hspace=0.05)
    treePlot = plt.subplot(gsTree[1:-1, 1:-1])
    treePlot.set_xlim(left=axisMinValue, right=axisMaxValue)
    treePlot.set_ylim(bottom=axisMinValue, top=axisMaxValue)
    nodes = [patches.Circle((nodeCenterXValues[i], nodeCenterYValues[i]), nodeWidth / 2) for i in range(len(nodeDepths))]
    patchplotting.graphGeneration(nodes, currentFigure=currentFigure, faceColors=['white'] * len(nodes), zorders=[-1])
    addtext.graphGeneration(nodeCenterXValues, nodeCenterYValues, nodeLabels, currentFigure=currentFigure, sizes=[15] * len(nodeLabels), zorders=list(range(len(nodeLabels))))
    linegraph.graphGeneration(treeEdgesXValues, treeEdgesYValues, currentFigure=currentFigure, markerSizes=[0] * len(treeEdgesYValues), zorders=[-len(nodes)])
    removeTickMarks(treePlot, xAxis=True, yAxis=True)

    plt.savefig(treeSaveLocation, bbox_inches='tight', transparent=True)

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