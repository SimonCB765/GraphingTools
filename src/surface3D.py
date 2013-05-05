import argparse
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import sys

def commandLine(args):
	"""
	"""

	parser = argparse.ArgumentParser(description='Process the command line input for creating a 3D surface.')
	parser.add_argument('inputFile', help='an input file containing the values for the surface')
	parser.add_argument('numberRows', default=0, type=int, help='the number of rows to reshape the data into')
	parser.add_argument('numberCols', default=0, type=int, help='the number of columns to reshape the data into')
	parser.add_argument('--save', default=False, help='the location to save the image')
	parser.add_argument('-d', '--delimiter', default='\t', help='the delimiter for the lines of the input file')
	parser.add_argument('--edge', default='black', help='the color of the edge of the surface')
	parser.add_argument('--color', default='black', help='the color of the surface')
	parser.add_argument('--transparency', default=1.0, type=float, help='the alpha of the surface')
	args = parser.parse_args()
	parseFile(args.inputFile, reshapeRows=[args.numberRows], reshapeCols=[args.numberCols], delimiter=args.delimiter, save=args.save, color=[args.color],
		edgeColor=[args.edge], transparency=[args.transparency])

def parseFile(inputFile, reshapeRows=[0], reshapeCols=[0], currentFigure=None, delimiter='\t', save=False, color=['black'], edgeColor=['black'],
		transparency=[1.0]):
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

	# Need to reshape the values to be 2D arrays.
	numberOfDatasets = len(xValues)
	if len(reshapeRows) != len(reshapeCols):
		print('You must provide the same number of rows and columns forthe reshaping')
	if len(reshapeRows) == 1:
		reshapeRows = reshapeRows * numberOfDatasets
	if len(reshapeCols) == 1:
		reshapeCols = reshapeCols * numberOfDatasets
	if len(reshapeRows) < numberOfDatasets:
		print('There were not enough reshape dimensions specified. You specified ' + str(len(reshapeRows)) + ' dimensions. You must specify ' + str(numberOfDataset) + '.')
		sys.exit(0)
	try:
		for i in range(len(xValues)):
			xValues[i] = xValues[i].reshape(reshapeRows[i], reshapeCols[i])
			yValues[i] = yValues[i].reshape(reshapeRows[i], reshapeCols[i])
			zValues[i] = zValues[i].reshape(reshapeRows[i], reshapeCols[i])
	except Exception:
		print('Reshape could not be performed as the dimensions specified are not applicable to the dataset provided')
		sys.exit()

	graphGeneration(xValues, yValues, zValues, currentFigure=currentFigure, save=save, color=color, edgeColor=edgeColor, transparency=transparency)
		

def graphGeneration(xValues, yValues, zValues, currentFigure=None, save=False, color=['black'], edgeColor=['black'], transparency=[1.0]):
	"""
	"""

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

	for i in range(len(xValues)):
		axes.plot_surface(xValues[i], yValues[i], zValues[i], color=color[i], edgecolor = edgeColor[i], alpha=transparency[i])

	plt.show()

	if save:
		pass

if __name__ == '__main__':
	commandLine(sys.argv)