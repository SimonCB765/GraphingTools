import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os
import sys

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)
import addtext
import linegraph
import patchplotting

def main(figureSaveLocation):
    """Create an image for demonstrating the suboptimal nature of list removal MIS approximaters.
    """

    # Initialise the figure.
    currentFigure = plt.figure()
    gs = gridspec.GridSpec(1, 2)
    gs.update(left=0.005, right=0.995, bottom=0.05, top=1, wspace=0.05)#, hspace=0.05)

    # Generate the graph with an independent set of two nodes.
    twoNodeISGraph = plt.subplot(gs[0, 0])
    generate_graph(currentFigure, blackNodes=['B\n50 AA\n', 'C\n75 AA\n'])

    # Generate the graph with an independent set of one node.
    oneNodeISGraph = plt.subplot(gs[0, 1])
    generate_graph(currentFigure, blackNodes=['A\n100 AA\n'])

    # Make all the tick marks invisible.
    for ax in currentFigure.get_axes():
        removeTickMarks(ax, xAxis=True, yAxis=True)

    plt.savefig(figureSaveLocation, bbox_inches='tight', transparent=True)

def generate_graph(currentFigure, blackNodes=[]):
    """Draw the graph for the demo.
    """

    # Define the image size.
    maxX = 4
    minX = -4
    maxY = 4
    minY = -3

    # Define the nodes as numberOfNodes nodes evenly spaced around a circle of radius nodeCirclePlacementRadius.
    nodeWidth = 1.3
    nodeNames = ['A\n100 AA\n', 'B\n50 AA\n', 'C\n75 AA\n']
    nodeCenterXValues = [0, -3, 3]
    nodeCenterYValues = [1, -1, -1]
    nodeColors = ['black' if i in blackNodes else 'white' for i in nodeNames]

    # Define the edges.
    edges = [['A\n100 AA\n', 'B\n50 AA\n'], ['A\n100 AA\n', 'C\n75 AA\n']]
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
    nodes = [patches.Circle((i, j), nodeWidth / 2) for i, j in zip(nodeCenterXValues, nodeCenterYValues)]
    patchplotting.graphGeneration(nodes, currentFigure=currentFigure, faceColors=nodeColors, zorders=[1 for i in nodeCenterXValues])
    addtext.graphGeneration(nodeCenterXValues, [i + 1 for i in nodeCenterYValues], nodeNames, currentFigure=currentFigure, sizes=[15] * len(nodeCenterXValues),
        zorders=[2 for i in nodeCenterXValues])
    linegraph.graphGeneration(edgeXValues, edgeYValues, currentFigure=currentFigure, markerSizes=[0 for i in nodeCenterXValues],
        lineStyles=edgeTypes, lineWidths=edgeThickness, zorders=[0 for i in nodeCenterXValues])

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