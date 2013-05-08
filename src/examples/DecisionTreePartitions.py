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


def main(treeSaveLocation, partitionSaveLocation):
    """Create an image that demonstrates the partition induced by a decision tree.

    @type treeSaveLocation - str
    @use  treeSaveLocation - The location where the image of the tree will be saved.
    @type partitionSaveLocation - str
    @use  partitionSaveLocation - The location where the image of the partitioning will be saved.
    """

    # Define the decision tree split points and partitions.
    splitValues = [5, 3, 6, 2, 8, 8, 7]
    splitVariables = ['X', 'Y', 'Y', 'X', 'Y', 'X', 'X']
    nodeLabels = splitVariables + [str(i) for i in range(len(splitValues) + 1)]
    partitionLabels = [str(i) for i in range(len(splitValues) + 1)]
    splitValues = splitValues + ([None] * (len(splitValues) + 1))  # Pad out the splitValues with empty values for the leaves.
    splitVariables = splitVariables + ([None] * (len(splitValues) + 1))  # Pad out the splitVariables with empty values for the leaves.

    # Define the axis size;
    axisMinValue = 0.0
    axisMaxValue = 10.0

    # Define the decision tree node sizes and positions.
    nodeWidth = 1.0
    nodeHeight = 1.0
    gapBetweenLevels = 1.0
    gapBetweenCousins = 0.5
    nodeDepths = [int(math.log(i+1,2)) for i in range(len(splitValues))]
    maxDepth = max(nodeDepths)
    nodesAtDepth = [(2**nodeDepths[i], nodeDepths[:i].count(nodeDepths[i]) + 1) for i in range(len(nodeDepths))]  # The depth of the node along with the position on the row (leftmost is 1).
    nodeCenterXValues = []
    nodeCenterYValues = [axisMaxValue - (i * nodeHeight + ((i + 1) * gapBetweenLevels) + (nodeHeight / 2)) for i in nodeDepths]
    for i in range(len(splitValues)):
        splits = [(axisMaxValue / nodesAtDepth[i][0]) * j for j in range(nodesAtDepth[i][0] + 1)]
        positions = [(splits[j] + splits[j+1]) / 2 for j in range(nodesAtDepth[i][0])]
        nodeCenterXValues.append(positions[nodesAtDepth[i][1] - 1])
    treeEdgesXValues = []
    treeEdgesYValues = []
    treeEdgeLabels = []
    for i in range(len(splitValues)):
        if not splitValues[i]:
            # If i is the index of a leaf node, then continue as the leaf does not hold any information about he partition.
            continue
        leftChildIndex = int((i * 2) + 1)
        rightChildIndex = int((i * 2) + 2)
        treeEdgesXValues += [[nodeCenterXValues[i], nodeCenterXValues[leftChildIndex]], [nodeCenterXValues[i], nodeCenterXValues[rightChildIndex]]]
        treeEdgesYValues += [[nodeCenterYValues[i], nodeCenterYValues[leftChildIndex]], [nodeCenterYValues[i], nodeCenterYValues[rightChildIndex]]]
        treeEdgeLabels += [r'$\leq$' + str(splitValues[i]), r'$>$' + str(splitValues[i])]
    edgeCenterXValues = [sum(i) / 2 for i in treeEdgesXValues]
    edgeCenterXValues = [edgeCenterXValues[i] + 0.5 if i % 2 else edgeCenterXValues[i] - 0.5 for i in range(len(edgeCenterXValues))]
    edgeCenterYValues = [sum(i) / 2 for i in treeEdgesYValues]

    # Determine the partitions used, and the locatations for the labels of the partitions.
    partitionXValues = []
    partitionYValues = []
    partitionWidths = []
    partitionHeights = []
    partitionLabelXValues = []
    partitionLabelYValues = []
    for i in range(len(splitValues)):
        if not splitValues[i]:
            # If i is the index of a leaf node, then continue as the leaf does not hold any information about he partition.
            continue

        valueOfI = splitValues[i]
        variableOfI = splitVariables[i]

        # Determine the starting bounds for the partition rectangle.
        currentVarLessThan = axisMaxValue
        currentVarMoreThan = axisMinValue
        otherVarLessThan = axisMaxValue
        otherVarMoreThan = axisMinValue

        # Determine if the current node is a leaf node (i.e. it has no children).
        isLeaf = False
        leftChildIndex = int((i * 2) + 1)
        if (not splitValues[leftChildIndex]):
            # If the left child does not exist, then the current node is the parent of two leaves
            # (as each node either has two children (internal node) or none (leaf node)).
            currentNodeIndex = i
            while currentNodeIndex > 0:
                # Loop through all the ancestors of the current node, and determine the partition that they induce.
                currentNodeIsLeftChild = True if currentNodeIndex % 2 == 1 else False
                if currentNodeIsLeftChild:
                    parentNodeIndex = int((currentNodeIndex - 1) / 2)
                    currentNodeIndex = parentNodeIndex
                else:
                    parentNodeIndex = int((currentNodeIndex - 2) / 2)
                    currentNodeIndex = parentNodeIndex

                parentNodeVariable = splitVariables[parentNodeIndex]
                parentNodeValue = splitValues[parentNodeIndex]
                if parentNodeVariable != variableOfI:
                    if currentNodeIsLeftChild:
                        otherVarLessThan = min(otherVarLessThan, parentNodeValue)
                    else:
                        otherVarMoreThan = max(otherVarMoreThan, parentNodeValue)
                else:
                    if currentNodeIsLeftChild:
                        currentVarLessThan = min(currentVarLessThan, parentNodeValue)
                    else:
                        currentVarMoreThan = max(currentVarMoreThan, parentNodeValue)
            if variableOfI == 'X':
                partitionXValues += [currentVarMoreThan, valueOfI]
                partitionYValues += [otherVarMoreThan, otherVarMoreThan]
                height = otherVarLessThan - otherVarMoreThan
                partitionWidths += [valueOfI - currentVarMoreThan, currentVarLessThan - valueOfI]
                partitionHeights += [height, height]
                partitionLabelXValues.append((valueOfI + currentVarMoreThan) / 2.0)
                partitionLabelYValues.append((otherVarLessThan + otherVarMoreThan) / 2.0)
                partitionLabelXValues.append((currentVarLessThan + valueOfI) / 2.0)
                partitionLabelYValues.append((otherVarLessThan + otherVarMoreThan) / 2.0)
            else:
                partitionXValues += [otherVarMoreThan, otherVarMoreThan]
                partitionYValues += [currentVarMoreThan, valueOfI]
                width = otherVarLessThan - otherVarMoreThan
                partitionWidths += [width, width]
                partitionHeights += [valueOfI - currentVarMoreThan, currentVarLessThan - valueOfI]
                partitionLabelXValues.append((otherVarLessThan + otherVarMoreThan) / 2.0)
                partitionLabelYValues.append((valueOfI + currentVarMoreThan) / 2.0)
                partitionLabelXValues.append((otherVarLessThan + otherVarMoreThan) / 2.0)
                partitionLabelYValues.append((currentVarLessThan + valueOfI) / 2.0)

    # Create the plot for the decision tree.
    currentFigure = plt.figure()
    gsTree = gridspec.GridSpec(10, 10)
    gsTree.update(left=0, right=1, bottom=0, top=1, wspace=0.05)#, hspace=0.05)
    treePlot = plt.subplot(gsTree[1:-1, 1:-1])
    treePlot.set_xlim(left=axisMinValue, right=axisMaxValue)
    treePlot.set_ylim(bottom=axisMinValue, top=axisMaxValue)
    nodes = [patches.Rectangle((nodeCenterXValues[i] - (nodeWidth / 2), nodeCenterYValues[i] - (nodeHeight / 2)), nodeWidth, nodeHeight) if nodeDepths[i] < maxDepth
             else patches.Circle((nodeCenterXValues[i], nodeCenterYValues[i]), nodeWidth / 2)
             for i in range(len(nodeDepths))]
    patchplotting.graphGeneration(nodes, currentFigure=currentFigure, faceColors=['white'] * len(nodes), zorders=[-1])
    addtext.graphGeneration(nodeCenterXValues, nodeCenterYValues, nodeLabels, currentFigure=currentFigure, sizes=[15] * len(nodeLabels), zorders=list(range(len(nodeLabels))))
    linegraph.graphGeneration(treeEdgesXValues, treeEdgesYValues, currentFigure=currentFigure, markerSizes=[0] * len(treeEdgesYValues), zorders=[-len(nodes)])
    addtext.graphGeneration(edgeCenterXValues, edgeCenterYValues, treeEdgeLabels, currentFigure=currentFigure, sizes=[15] * len(treeEdgeLabels), zorders=list(range(len(treeEdgeLabels))))
    removeTickMarks(treePlot, xAxis=True, yAxis=True)
    plt.savefig(treeSaveLocation, bbox_inches=0, transparent=True)

    # Create the plot for the feature space partition.
    currentFigure = plt.figure()
    gsPartition = gridspec.GridSpec(10, 10)
    gsPartition.update(left=0, right=1, bottom=0, top=1, wspace=0.05)#, hspace=0.05)
    partitionPlot = plt.subplot(gsPartition[1:-1, 1:-1])
    partitionPlot.set_xlim(left=axisMinValue, right=axisMaxValue)
    partitionPlot.set_ylim(bottom=axisMinValue, top=axisMaxValue)
    rectangles = [patches.Rectangle((partitionXValues[i], partitionYValues[i]), partitionWidths[i], partitionHeights[i]) for i in range(len(partitionXValues))]
    patchplotting.graphGeneration(rectangles, currentFigure=currentFigure, faceColors=['white'] * len(rectangles), zorders=[-1])
    addtext.graphGeneration(partitionLabelXValues, partitionLabelYValues, partitionLabels, currentFigure=currentFigure, sizes=[20] * len(partitionLabels), zorders=list(range(len(partitionLabels))))
    removeTickMarks(partitionPlot, xAxis=True, yAxis=True)
    plt.savefig(partitionSaveLocation, bbox_inches=0, transparent=True)
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
    main(sys.argv[1], sys.argv[2])