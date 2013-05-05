import argparse
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np
import sys

def commandLine(args):
	"""
	"""

	parser = argparse.ArgumentParser(description='Process the command line input for creating a 3D shape.')
	parser.add_argument('inputFile', help='an input file containing the values for the corners of the surface')
	parser.add_argument('--save', default=False, help='the location to save the image')
	parser.add_argument('-d', '--delimiter', default='\t', help='the delimiter for the lines of the input file')
	parser.add_argument('--edge', default='black', help='the color of the edge of the surface')
	parser.add_argument('--color', default='black', help='the color of the surface')
	parser.add_argument('--transparency', default=1.0, type=float, help='the alpha of the surface')
	args = parser.parse_args()
	parseFile(args.inputFile, delimiter=args.delimiter, save=args.save, color=[args.color], edgeColor=[args.edge], transparency=[args.transparency])

def parseFile(inputFile, currentFigure=None, delimiter='\t', save=False, color=['black'], edgeColor=['black'], transparency=[1.0]):
	"""
	"""

	matrix = np.genfromtxt(inputFile, delimiter=delimiter)
	numberOfRows = matrix.shape[0]
	numberOfColumns = matrix.shape[1]

	# The first column (column 0) is the x values, the second column (column 1) the y values and the third column (column 2) the z values.
	# In general, column x is the x values, x + 1 the y values and x + 2 the z values.
	xValues = [matrix[:, i] for i in range(numberOfColumns)[0::3]]  # The x values are in every third column starting at 0.
	yValues = [matrix[:, i] for i in range(numberOfColumns)[1::3]]  # The y values are in every third column starting at 1.
	zValues = [matrix[:, i] for i in range(numberOfColumns)[2::3]]  # The z values are in every third column starting at 2.
	shapes = [[tuple([xValues[i][j], yValues[i][j], zValues[i][j]]) for j in range(numberOfRows)] for i in range(len(xValues))]

	graphGeneration(shapes, currentFigure=currentFigure, save=save, color=color, edgeColor=edgeColor, transparency=transparency)
		

def graphGeneration(shapes, currentFigure=None, save=False, color=['black'], edgeColor=['black'], transparency=[1.0]):
	"""
	"""

	xValues = [j[0] for i in shapes for j in i]
	yValues = [j[1] for i in shapes for j in i]
	zValues = [j[2] for i in shapes for j in i]

	numberOfDatasets = len(xValues)
	# If any colors are not provided, then fill in the missing ones with 'black'.
	color += ['black'] * (numberOfDatasets - len(color))
	# If any edge colors are not provided, then fill in the missing ones with 'black'.
	edgeColor += ['black'] * (numberOfDatasets - len(edgeColor))
	# If any transparencies are not provided, then fill in the missing ones with 1.0.
	transparency += [1.0] * (numberOfDatasets - len(transparency))

	try:
		axes = currentFigure.gca()
	except AttributeError:
		# If the figure is not given then create it.
		currentFigure = plt.figure()
		axes = currentFigure.add_subplot(1, 1, 1, projection='3d')

	for i in range(len(shapes)):
		surface = Poly3DCollection([shapes[i]], alpha=transparency[i])
		surface.set_facecolor(color[i])
		surface.set_edgecolor(edgeColor[i])
		axes.add_collection3d(surface)

	# Rescale the axes so that all the surfaces fit in. If this is not desired, then ths can be manipulated external to this script.
	maxX = max(xValues)
	minX = min(xValues)
	maxY = max(yValues)
	minY = min(yValues)
	maxZ = max(zValues)
	minZ = min(zValues)
	axes.set_xlim3d(minX, maxX)
	axes.set_ylim3d(minY, maxY)
	axes.set_zlim3d(minZ, maxZ)

	plt.show()

	if save:
		pass

if __name__ == '__main__':
	commandLine(sys.argv)