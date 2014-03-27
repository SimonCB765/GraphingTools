import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import sys

def main(figureSaveLocation):
    """Create an image for demonstrating graph definitions.
    """

    # Create the figure, the grids for the subplots and determine the spacing for the subplots.
    currentFigure = plt.figure()
    gsTopRow = gridspec.GridSpec(3, 2)
    gsMidRow = gridspec.GridSpec(3, 2)
    gsBotRow = gridspec.GridSpec(3, 2)
    gsTopRow.update(left=0.005, right=0.995, bottom=0.05, top=1, wspace=0.0, hspace=0.0)
    gsMidRow.update(left=0.005, right=0.995, bottom=0.05, top=1, wspace=0.0, hspace=0.0)
    gsBotRow.update(left=0.005, right=0.995, bottom=0.05, top=1, wspace=0.0, hspace=0.0)

    # Create the parent 1 array.
    parentOneArray = plt.subplot(gsTopRow[0, 0])
    draw_array(currentFigure, cellValues=['A', 'B', 'C', 'D', 'E', 'F', 'G'], boldCellValues=['A', 'C', 'D', 'F'], shadedCells=[], label='Parent 1')

    # Create the mask array.
    maskArray = plt.subplot(gsMidRow[1, 0])
    draw_array(currentFigure, cellValues=[1, 0, 1, 1, 1, 0, 0], boldCellValues=[], shadedCells=[], label='Mask')

    # Create the parent 2 array.
    parentTwoArray = plt.subplot(gsBotRow[2, 0])
    draw_array(currentFigure, cellValues=['A', 'B', 'C', 'D', 'E', 'F', 'G'], boldCellValues=['A', 'B', 'D', 'E'], shadedCells=['A', 'B', 'C', 'D', 'E', 'F', 'G'], label='Parent 2')

    # Create the child 1 array.
    childOneArray = plt.subplot(gsTopRow[0, 1])
    draw_array(currentFigure, cellValues=['A', 'B', 'C', 'D', 'E', 'F', 'G'], boldCellValues=['A', 'D', 'E', 'F'], shadedCells=['A', 'C', 'D', 'E'], label='Child 1')

    # Create the child 2 array.
    childTwoArray = plt.subplot(gsBotRow[2, 1])
    draw_array(currentFigure, cellValues=['A', 'B', 'C', 'D', 'E', 'F', 'G'], boldCellValues=['A', 'B', 'C', 'D'], shadedCells=['B', 'F', 'G'], label='Child 2')

    # Make all the tick marks invisible.
    for ax in currentFigure.get_axes():
        removeTickMarks(ax, xAxis=True, yAxis=True)

    plt.savefig(figureSaveLocation, bbox_inches='tight', transparent=True)

def draw_array(currentFigure, cellValues=[], boldCellValues=[], shadedCells=[], label=''):
    """Draw an array consisting of the cellValues.
    """

    # Setup the graph.
    plot = currentFigure.gca()
    plot.axis('scaled')
    plot.spines['top'].set_visible(False)
    plot.spines['right'].set_visible(False)
    plot.spines['bottom'].set_visible(False)
    plot.spines['left'].set_visible(False)
    plot.set_xlim(left=-0.5, right=len(cellValues) + 0.5)
    plot.set_ylim(bottom=0, top=3)

    # Plot the array
    currentX = 0
    for i in cellValues:
        # Create the cell.
        cell = patches.Rectangle(xy=[currentX, 0.5], width=1, height=1)
        cell.set_edgecolor('black')
        if i in shadedCells:
            cell.set_facecolor('grey')
        else:
            cell.set_facecolor('none')
        plot.add_patch(cell)

        # Add the cell value.
        if i in boldCellValues:
            plot.text(currentX + 0.5, 1, i, size=19, color='black', weight='bold', horizontalalignment='center', verticalalignment='center')
        else:
            plot.text(currentX + 0.5, 1, i, size=13, color='black', style='italic', horizontalalignment='center', verticalalignment='center')

        currentX += 1

    # Add the label
    plot.text(0, 2, label, size=12, color='black', weight='semibold', horizontalalignment='left', verticalalignment='center')

def removeTickMarks(axes, xAxis=False, yAxis=False):
    """Removes all tick marks for the given axes.
    """

    if xAxis:
        axes.set_xticks([])
    if yAxis:
        axes.set_yticks([])

if __name__ == '__main__':
    main(sys.argv[1])