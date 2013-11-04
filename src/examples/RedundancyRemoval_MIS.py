import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import os
import shutil
import sys

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)
import addtext
import linegraph
import patchplotting

def main(figureSaveLocation):
    """Create a series of images that demonstrate the different maximum independent set finding methods.

    @type figureSaveLocation - str
    @use  figureSaveLocation - The directory location where the figures will be saved.
    """

    # Setup the output location.
    leafOutputDir = figureSaveLocation + '/LeafDemo'
    NCOutputDir = figureSaveLocation + '/NeighbourCullDemo'
    FISOutputDir = figureSaveLocation + '/FISDemo'
    if not os.path.exists(figureSaveLocation):
        os.mkdir(figureSaveLocation)
        os.mkdir(leafOutputDir)
        os.mkdir(NCOutputDir)
        os.mkdir(FISOutputDir)
    else:
        if not os.path.exists(leafOutputDir):
            os.mkdir(leafOutputDir)
        if not os.path.exists(NCOutputDir):
            os.mkdir(NCOutputDir)
        if not os.path.exists(FISOutputDir):
            os.mkdir(FISOutputDir)


    # Draw the base graph.
    baseFigure = plt.figure(figsize=(10, 10))
    baseGrid = gridspec.GridSpec(10, 10)
    baseGrid.update(left=0, right=1, bottom=0, top=1, wspace=0.05)
    basePlot = plt.subplot(baseGrid[1:-1, 1:-1])
    draw_graph(baseFigure, removed=[], kept=[])
    plt.savefig(figureSaveLocation + '/InitialGraph', bbox_inches='tight', transparent=True)

    # Draw the Leaf demo graphs.
    leafFigureOne = plt.figure(figsize=(10, 10))
    leafGridOne = gridspec.GridSpec(3, 2)
    leafGridOne.update(left=0.005, right=0.995, bottom=0.05, top=1, wspace=0.05)
    leafStep1Plot = plt.subplot(leafGridOne[0, 0:2])  # Graph for the first step of the Leaf redundancy removal.
    draw_graph(leafFigureOne, removed=['B'], kept=['A'], label='(a)')
    leafStep3Plot = plt.subplot(leafGridOne[1, 0:2])  # Graph for the third step of the Leaf redundancy removal.
    draw_graph(leafFigureOne, removed=['B', 'D', 'E', 'G', 'H'], kept=['A', 'C', 'F'], label='(c)')
    leafBlankPlot = plt.subplot(leafGridOne[2, 0:2])  # Stick a blank placeholder in to synchronise the spacing for the Leaf, NC and FIS graphs.
    draw_graph(leafFigureOne, blank=True)
    leafGridOne.tight_layout(leafFigureOne)
    plt.savefig(leafOutputDir + '/GraphsForSteps-1_3', bbox_inches='tight', transparent=True)
    leafFigureTwo = plt.figure(figsize=(10, 10))
    leafGridTwo = gridspec.GridSpec(3, 2)
    leafGridTwo.update(left=0.005, right=0.995, bottom=0.05, top=1, wspace=0.05)
    leafStep2Plot = plt.subplot(leafGridTwo[0, 0:2])  # Graph for the second step of the Leaf redundancy removal.
    draw_graph(leafFigureTwo, removed=['B', 'D', 'E'], kept=['A', 'C'], label='(b)')
    leafStep4Plot = plt.subplot(leafGridTwo[1, 0:2])  # Graph for the fourth step of the Leaf redundancy removal.
    draw_graph(leafFigureTwo, removed=['B', 'D', 'E', 'G', 'H'], kept=['A', 'C', 'F', 'I'], label='(d)')
    leafBlankPlot = plt.subplot(leafGridTwo[2, 0:2])  # Stick a blank placeholder in to synchronise the spacing for the Leaf, NC and FIS graphs.
    draw_graph(leafFigureTwo, blank=True)
    leafGridTwo.tight_layout(leafFigureTwo)
    plt.savefig(leafOutputDir + '/GraphsForSteps-2_4', bbox_inches='tight', transparent=True)

    # Draw the NeighbourCull demo graphs.
    NCFigureOne = plt.figure(figsize=(10, 10))
    NCGridOne = gridspec.GridSpec(3, 2)
    NCGridOne.update(left=0.005, right=0.995, bottom=0.05, top=1, wspace=0.05)
    NCStep1Plot = plt.subplot(NCGridOne[0, 0:2])  # Graph for the first step of the NeighourCull redundancy removal.
    draw_graph(NCFigureOne, removed=['G'], kept=[], label='(a)')
    NCStep3Plot = plt.subplot(NCGridOne[1, 0:2])  # Graph for the third step of the NeighourCull redundancy removal.
    draw_graph(NCFigureOne, removed=['B', 'D', 'G'], kept=[], label='(c)')
    NCStep5Plot = plt.subplot(NCGridOne[2, 0:2])  # Graph for the fifth step of the NeighourCull redundancy removal.
    draw_graph(NCFigureOne, removed=['B', 'C', 'D', 'G', 'H'], kept=[], label='(e)')
    NCGridOne.tight_layout(NCFigureOne)
    plt.savefig(NCOutputDir + '/GraphsForSteps-1_3_5', bbox_inches='tight', transparent=True)
    NCFigureTwo = plt.figure(figsize=(10, 10))
    NCGridTwo = gridspec.GridSpec(3, 2)
    NCGridTwo.update(left=0.005, right=0.995, bottom=0.05, top=1, wspace=0.05)
    NCStep2Plot = plt.subplot(NCGridTwo[0, 0:2])  # Graph for the second step of the NeighourCull redundancy removal.
    draw_graph(NCFigureTwo, removed=['D', 'G'], kept=[], label='(b)')
    NCStep4Plot = plt.subplot(NCGridTwo[1, 0:2])  # Graph for the fourth step of the NeighourCull redundancy removal.
    draw_graph(NCFigureTwo, removed=['B', 'D', 'G', 'H'], kept=[], label='(d)')
    NCStep6Plot = plt.subplot(NCGridTwo[2, 0:2])  # Graph for the sixth step of the NeighourCull redundancy removal.
    draw_graph(NCFigureTwo, removed=['B', 'C', 'D', 'G', 'H'], kept=['A', 'E', 'F', 'I'], label='(f)')
    NCGridTwo.tight_layout(NCFigureTwo)
    plt.savefig(NCOutputDir + '/GraphsForSteps-2_4_6', bbox_inches='tight', transparent=True)

    # Draw the FIS demo graphs.
    FISFigureOne = plt.figure(figsize=(10, 10))
    FISGridOne = gridspec.GridSpec(3, 2)
    FISGridOne.update(left=0.005, right=0.995, bottom=0.05, top=1, wspace=0.05)
    FISStep1Plot = plt.subplot(FISGridOne[0, 0:2])  # Graph for the first step of the FIS redundancy removal.
    draw_graph(FISFigureOne, removed=['B'], kept=['A'], label='(a)')
    FISStep3Plot = plt.subplot(FISGridOne[1, 0:2])  # Graph for the third step of the FIS redundancy removal.
    draw_graph(FISFigureOne, removed=['B', 'D', 'E', 'G', 'H'], kept=['A', 'C', 'F'], label='(c)')
    FISStep5Plot = plt.subplot(FISGridOne[2, 0:2])  # Graph for the fifth step of the FIS redundancy removal.
    draw_graph(FISFigureOne, removed=['B', 'C', 'D', 'E', 'G', 'H'], kept=['A', 'D', 'F', 'I'], label='(e)')
    FISGridOne.tight_layout(FISFigureOne)
    plt.savefig(FISOutputDir + '/GraphsForSteps-1_3_5', bbox_inches='tight', transparent=True)
    FISFigureTwo = plt.figure(figsize=(10, 10))
    FISGridTwo = gridspec.GridSpec(3, 2)
    FISGridTwo.update(left=0.005, right=0.995, bottom=0.05, top=1, wspace=0.05)
    FISStep2Plot = plt.subplot(FISGridTwo[0, 0:2])  # Graph for the second step of the FIS redundancy removal.
    draw_graph(FISFigureTwo, removed=['B', 'D', 'E'], kept=['A', 'C'], label='(b)')
    FISStep4Plot = plt.subplot(FISGridTwo[1, 0:2])  # Graph for the fourth step of the FIS redundancy removal.
    draw_graph(FISFigureTwo, removed=['B', 'D', 'E', 'G', 'H'], kept=['A', 'C', 'F', 'I'], label='(d)')
    FISStep6Plot = plt.subplot(FISGridTwo[2, 0:2])  # Graph for the sixth step of the FIS redundancy removal.
    draw_graph(FISFigureTwo, removed=['B', 'C', 'D', 'E', 'G', 'H'], kept=['A', 'E', 'F', 'I'], label='(f)')
    FISGridTwo.tight_layout(FISFigureTwo)
    plt.savefig(FISOutputDir + '/GraphsForSteps-2_4_6', bbox_inches='tight', transparent=True)

def draw_graph(currentFigure, removed=[], kept=[], label='', blank=False):
    """
    """

    # Define the names and locations of the nodes.
    numberOfNodes = 9
    nodeWidth = 1.0
    nodeNames = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
    nodeCenterXValues = [0, 0, -4, -2, -4, 2,  4, 4, 6]
    nodeCenterYValues = [2, 0,  1,  0, -1, 0, -1, 1, 0]

    # Setup the appearances of the nodes.
    nodeColors = ['black' if i in kept else ('white' if i in removed else '#C0C0C0') for i in nodeNames]
    nodeNameColors = ['white' if i in kept else 'black' for i in nodeNames]

    # Define the edges between the nodes.
    edges = [['A', 'B'], ['B', 'D'], ['B', 'F'], ['C', 'D'], ['C', 'E'], ['D', 'E'], ['F', 'G'], ['F', 'H'], ['G', 'H'], ['G', 'I'], ['H', 'I']]
    edgeXValues = [[nodeCenterXValues[nodeNames.index(i[0])], nodeCenterXValues[nodeNames.index(i[1])]] for i in edges]
    edgeYValues = [[nodeCenterYValues[nodeNames.index(i[0])], nodeCenterYValues[nodeNames.index(i[1])]] for i in edges]
    edgeTypes = ['--' if i[0] in removed or i[1] in removed else '-' for i in edges]
    edgeThickness = [2 if i[0] in removed or i[1] in removed else 3 for i in edges]

    # Setup the plot attributes.
    plot = currentFigure.gca()
    plot.axis('scaled')
    plot.set_xlim(left=min(nodeCenterXValues) - nodeWidth, right=max(nodeCenterXValues) + nodeWidth)
    plot.set_ylim(bottom=min(nodeCenterYValues) - nodeWidth, top=max(nodeCenterYValues) + nodeWidth)
    plot.axis('off')

    if not blank:
        # Plot the nodes
        nodes = [patches.Circle((nodeCenterXValues[i], nodeCenterYValues[i]), nodeWidth / 2) for i in range(numberOfNodes)]
        patchplotting.graphGeneration(nodes, currentFigure=currentFigure, faceColors=nodeColors, zorders=[1 for i in range(numberOfNodes)])
        addtext.graphGeneration(nodeCenterXValues, nodeCenterYValues, nodeNames, currentFigure=currentFigure, sizes=[20] * numberOfNodes,
            colors=nodeNameColors, zorders=[2 for i in range(numberOfNodes)])
        linegraph.graphGeneration(edgeXValues, edgeYValues, currentFigure=currentFigure, markerSizes=[0 for i in range(numberOfNodes)],
            lineStyles=edgeTypes, lineWidths=edgeThickness, zorders=[0 for i in range(numberOfNodes)])

        # Add the label.
        plot.text(0, min(nodeCenterYValues) - (nodeWidth / 2), label, size=17, color='black', horizontalalignment='center',
                  verticalalignment='center', rotation=0, zorder=3)

if __name__ == '__main__':
    main(sys.argv[1])