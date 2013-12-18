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
import patchplotting

def main(figureSaveLocation):
    """Create an image for demonstrating graph definitions.
    """

    # Create the figure, the grids for the subplots and determine the spacing for the subplots.
    currentFigure = plt.figure()
    gsTopRow = gridspec.GridSpec(2, 4)
    gsBotRow = gridspec.GridSpec(2, 4)
    gsTopRow.update(left=0.005, right=0.995, bottom=0.05, top=1, wspace=0.05)#, hspace=0.05)
    gsBotRow.update(left=0.005, right=0.995, bottom=0.05, top=1, wspace=0.05)#, hspace=0.05)

    # Create the neighbourhood/degree/support graph.
    neighbourhoodGraph = plt.subplot(gsTopRow[0, 1:3])
    generate_neighbourhod_graph(currentFigure)

    # Create the non-complement graph.
    noncomplementGraph = plt.subplot(gsTopRow[1, 0:2])
    generate_complement_graph(currentFigure, blackNodes=['C', 'D', 'F', 'G'], complement=True)

    # Create the complement graph.
    complementGraph = plt.subplot(gsBotRow[1, 2:])
    generate_complement_graph(currentFigure, blackNodes=['C', 'D', 'F', 'G'], complement=False)

    # Make all the tick marks invisible, and label the x axes.
    labels = ['(c)', '(b)', '(a)']
    for ax in currentFigure.get_axes():
        removeTickMarks(ax, xAxis=True, yAxis=True)
        currentLabel = labels.pop()
        setLabels(ax, xLabel=currentLabel)
        ax.xaxis.set_label_coords(0.5, -0.025)

    plt.savefig(figureSaveLocation, bbox_inches='tight', transparent=True)

def generate_complement_graph(currentFigure, blackNodes=[], complement=False):
    """Draw the graph for the clique/independent set/vertex cover demo.
    """

    # Define the image size.
    maxX = 5
    minX = -5
    maxY = 5
    minY = -5

    # Define the nodes as numberOfNodes nodes evenly spaced around a circle of radius nodeCirclePlacementRadius.
    numberOfNodes = 7
    nodeWidth = 1.3
    nodeNames = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    nodeCirclePlacementRadius = 4
    nodeCenterXValues = [nodeCirclePlacementRadius * math.cos(math.pi * (2/7) * (i + 1)) for i in range(len(nodeNames))]
    nodeCenterYValues = [nodeCirclePlacementRadius * math.sin(math.pi * (2/7) * (i + 1)) for i in range(len(nodeNames))]
    nodeColors = ['black' if i in blackNodes else 'white' for i in nodeNames]
    nodeNameColors = ['white' if i in blackNodes else 'black' for i in nodeNames]

    # Define the edges.
    edges = [['C', 'D'], ['C', 'F'], ['C', 'G'], ['D', 'F'], ['D', 'G'], ['F', 'G'],  # The clique.
        ['B', 'D'], ['A', 'F'], ['A', 'C'], ['A', 'E'], ['D', 'E']]
    if complement:
        allEdges = [[nodeNames[i], nodeNames[j]] for i in range(len(nodeNames)) for j in range(i+1,len(nodeNames))]
        edges = [i for i in allEdges if i not in edges]
    edgeXValues = [[nodeCenterXValues[nodeNames.index(i[0])], nodeCenterXValues[nodeNames.index(i[1])]] for i in edges]
    edgeYValues = [[nodeCenterYValues[nodeNames.index(i[0])], nodeCenterYValues[nodeNames.index(i[1])]] for i in edges]
    edgeTypes = ['-' for i in edges]
    edgeThickness = [2 for i in edges]

    # Plot the graph.
    plot = currentFigure.gca()
    plot.axis('scaled')
    plot.set_xlim(left=minX, right=maxX)
    plot.set_ylim(bottom=minY, top=maxY)
    plot.spines['top'].set_visible(False)
    plot.spines['right'].set_visible(False)
    plot.spines['bottom'].set_visible(False)
    plot.spines['left'].set_visible(False)
    nodes = [patches.Circle((nodeCenterXValues[i], nodeCenterYValues[i]), nodeWidth / 2) for i in range(numberOfNodes)]
    patchplotting.graphGeneration(nodes, currentFigure=currentFigure, faceColors=nodeColors, zorders=[1 for i in range(numberOfNodes)])
    addtext.graphGeneration(nodeCenterXValues, nodeCenterYValues, nodeNames, currentFigure=currentFigure, sizes=[20] * numberOfNodes,
        colors=nodeNameColors, zorders=[2 for i in range(numberOfNodes)])
    linegraph.graphGeneration(edgeXValues, edgeYValues, currentFigure=currentFigure, markerSizes=[0 for i in range(numberOfNodes)],
        lineStyles=edgeTypes, lineWidths=edgeThickness, zorders=[0 for i in range(numberOfNodes)])

def generate_neighbourhod_graph(currentFigure):
    """Draw the graph for the neighbourhood demo.
    """

    # Define the image size.
    maxX = 5
    minX = -5
    maxY = 5
    minY = -5

    # Define the nodes.
    numberOfNodes = 11
    nodeWidth = 1.3
    nodeNames = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']
    nodeCenterXValues = [-3, -2, -3, -1, 0, 0, 2, 3,  3,  1,  0]
    nodeCenterYValues = [ 3,  1, -1, -1, 1, 3, 1, 3, -1, -1, -3]
    nodeColors = ['white' for i in nodeNames]
    nodeNameColors = ['black' for i in nodeNames]

    # Define the edges.
    edges = [['A', 'B'], ['B', 'C'], ['B', 'E'], ['C', 'D'], ['E', 'F'], ['E', 'G'], ['G', 'H'], ['G', 'I'], ['I', 'J'], ['J', 'K']]
    edgeXValues = [[nodeCenterXValues[nodeNames.index(i[0])], nodeCenterXValues[nodeNames.index(i[1])]] for i in edges]
    edgeYValues = [[nodeCenterYValues[nodeNames.index(i[0])], nodeCenterYValues[nodeNames.index(i[1])]] for i in edges]
    edgeTypes = ['-' for i in edges]
    edgeThickness = [2 for i in edges]

    # Plot the graph.
    plot = currentFigure.gca()
    plot.axis('scaled')
    plot.spines['top'].set_visible(False)
    plot.spines['right'].set_visible(False)
    plot.spines['bottom'].set_visible(False)
    plot.spines['left'].set_visible(False)
    plot.set_xlim(left=minX, right=maxX)
    plot.set_ylim(bottom=minY, top=maxY)
    nodes = [patches.Circle((nodeCenterXValues[i], nodeCenterYValues[i]), nodeWidth / 2) for i in range(numberOfNodes)]
    patchplotting.graphGeneration(nodes, currentFigure=currentFigure, faceColors=nodeColors, zorders=[1 for i in range(numberOfNodes)])
    addtext.graphGeneration(nodeCenterXValues, nodeCenterYValues, nodeNames, currentFigure=currentFigure, sizes=[20] * numberOfNodes,
        colors=nodeNameColors, zorders=[2 for i in range(numberOfNodes)])
    linegraph.graphGeneration(edgeXValues, edgeYValues, currentFigure=currentFigure, markerSizes=[0 for i in range(numberOfNodes)],
        lineStyles=edgeTypes, lineWidths=edgeThickness, zorders=[0 for i in range(numberOfNodes)])

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