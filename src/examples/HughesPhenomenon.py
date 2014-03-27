import matplotlib.gridspec as gridspec
import matplotlib.path as mpath
import matplotlib.patches as patches
import matplotlib.pyplot as plt
import numpy as np
import sys

import os
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)
import addtext
import linegraph


def main(figureSaveLocation):
    """Create a demo for the Hughes Phenomenon.
    """

    # Initialise the figure.
    currentFigure = plt.figure()
    gs = gridspec.GridSpec(10, 10)
    gs.update(left=0, right=1, bottom=0, top=1, wspace=0.05)
    axes = plt.subplot(gs[1:-1, 1:-1])
    axes.set_xlabel('Data Dimensionality')
    axes.set_ylabel('Classifier Performance')
    removeTickMarks(axes, xAxis=True, yAxis=True)
    axes.set_xlim(left=0, right=10)
    axes.set_ylim(bottom=0, top=10)

    # Add the worst curve.
    curveRank1Vertx = [(0.0, 0.0),
                       (3.0, 7.0),
                       (1.5, 0.5),
                       (6.0, 0.5)
                      ]
    curveRank1Moves = [mpath.Path.MOVETO,
                       mpath.Path.CURVE4,
                       mpath.Path.CURVE4,
                       mpath.Path.CURVE4
                      ]
    pathCurveRank1 = mpath.Path(curveRank1Vertx, curveRank1Moves)
    patchCurveRank1 = patches.PathPatch(pathCurveRank1, facecolor='none', lw=2)
    axes.add_patch(patchCurveRank1)
    axes.text(6.0, 0.25, r'$\mathcal{N}=50$', size=15, color='black', horizontalalignment='center', verticalalignment='center', rotation=0)

	# Add the second worst curve.
    curveRank2Vertx = [(0.0, 0.0),
                       (3.0, 9.0),
                       (2.5, 1.5),
                       (6.25, 1.0)
                      ]
    curveRank2Moves = [mpath.Path.MOVETO,
                       mpath.Path.CURVE4,
                       mpath.Path.CURVE4,
                       mpath.Path.CURVE4
                      ]
    pathCurveRank2 = mpath.Path(curveRank2Vertx, curveRank2Moves)
    patchCurveRank2 = patches.PathPatch(pathCurveRank2, facecolor='none', lw=2)
    axes.add_patch(patchCurveRank2)
    axes.text(7.0, 1.0, r'$\mathcal{N}=100$', size=15, color='black', horizontalalignment='center', verticalalignment='center', rotation=0)

	# Add the third worst curve.
    curveRank3Vertx = [(0.0, 0.0),
                       (3.5, 11.0),
                       (2.5, 3.5),
                       (6.5, 2.0)
                      ]
    curveRank3Moves = [mpath.Path.MOVETO,
                       mpath.Path.CURVE4,
                       mpath.Path.CURVE4,
                       mpath.Path.CURVE4
                      ]
    pathCurveRank3 = mpath.Path(curveRank3Vertx, curveRank3Moves)
    patchCurveRank3 = patches.PathPatch(pathCurveRank3, facecolor='none', lw=2)
    axes.add_patch(patchCurveRank3)
    axes.text(7.25, 2.0, r'$\mathcal{N}=200$', size=15, color='black', horizontalalignment='center', verticalalignment='center', rotation=0)

	# Add the middle curve.
    curveRank4Vertx = [(0.0, 0.0),
                       (3.5, 12.0),
                       (3.0, 5.5),
                       (7.0, 3.0)
                      ]
    curveRank4Moves = [mpath.Path.MOVETO,
                       mpath.Path.CURVE4,
                       mpath.Path.CURVE4,
                       mpath.Path.CURVE4
                      ]
    pathCurveRank4 = mpath.Path(curveRank4Vertx, curveRank4Moves)
    patchCurveRank4 = patches.PathPatch(pathCurveRank4, facecolor='none', lw=2)
    axes.add_patch(patchCurveRank4)
    axes.text(7.75, 3.0, r'$\mathcal{N}=500$', size=15, color='black', horizontalalignment='center', verticalalignment='center', rotation=0)

	# Add the third best curve.
    curveRank5Vertx = [(0.0, 0.0),
                       (3.0, 12.0),
                       (3.2, 8.0),
                       (7.5, 4.0)
                      ]
    curveRank5Moves = [mpath.Path.MOVETO,
                       mpath.Path.CURVE4,
                       mpath.Path.CURVE4,
                       mpath.Path.CURVE4
                      ]
    pathCurveRank5 = mpath.Path(curveRank5Vertx, curveRank5Moves)
    patchCurveRank5 = patches.PathPatch(pathCurveRank5, facecolor='none', lw=2)
    axes.add_patch(patchCurveRank5)
    axes.text(8.25, 4.0, r'$\mathcal{N}=1000$', size=15, color='black', horizontalalignment='center', verticalalignment='center', rotation=0)

	# Add the second best curve.
    curveRank6Vertx = [(0.0, 0.0),
                       (3.0, 12.0),
                       (3.0, 8.5),
                       (8.0, 5.75)
                      ]
    curveRank6Moves = [mpath.Path.MOVETO,
                       mpath.Path.CURVE4,
                       mpath.Path.CURVE4,
                       mpath.Path.CURVE4
                      ]
    pathCurveRank6 = mpath.Path(curveRank6Vertx, curveRank6Moves)
    patchCurveRank6 = patches.PathPatch(pathCurveRank6, facecolor='none', lw=2)
    axes.add_patch(patchCurveRank6)
    axes.text(8.75, 5.75, r'$\mathcal{N}=5000$', size=15, color='black', horizontalalignment='center', verticalalignment='center', rotation=0)

	# Add the best curve.
    curveRank7Vertx = [(2.42691, 7.65982),
                       (3.55, 9.6),
                       (9.0, 9.5)
                      ]
    curveRank7Moves = [mpath.Path.MOVETO,
                       mpath.Path.CURVE3,
                       mpath.Path.CURVE3
                      ]
    pathCurveRank7 = mpath.Path(curveRank7Vertx, curveRank7Moves)
    patchCurveRank7 = patches.PathPatch(pathCurveRank7, facecolor='none', lw=2)
    axes.add_patch(patchCurveRank7)
    axes.text(9.0, 9.0, r'$\mathcal{N}=\infty$', size=15, color='black', horizontalalignment='center', verticalalignment='center', rotation=0)

    # Save the figure.
    plt.savefig(figureSaveLocation, bbox_inches='tight', transparent=True)

def removeTickMarks(axes, xAxis=False, yAxis=False):
    """Removes all tick marks.
    """

    if xAxis:
        axes.set_xticks([])
    if yAxis:
        axes.set_yticks([])

if __name__ == '__main__':
    main(sys.argv[1])