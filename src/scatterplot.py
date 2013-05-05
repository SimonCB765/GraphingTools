import argparse
import matplotlib.pyplot as plt
import numpy as np
import sys

def commandLine(args):
	"""
	"""

	parser = argparse.ArgumentParser(description='Process the command line input for creating a histogram.')
	parser.add_argument('inputFile', help='an input file containing the values for the histogram')
	parser.add_argument('saveLocation', help='the location to save the image')
	parser.add_argument('-d', '--delimiter', default='\t', help='the delimiter for the lines of the input file')
	parser.add_argument('--size', default=10, type=int, help='the size of the point')
	parser.add_argument('--color', default='black', help='the color of the point')
	parser.add_argument('--shape', default='o', help='the shape of the point')
	parser.add_argument('--edge', default='none', help='the color of the edges of the point')
	args = parser.parse_args()
	parseFile(args.inputFile, delimiter=args.delimiter, save=args.saveLocation, sizes=[args.size], colors=[args.color], shapes=[args.shape], edgeColors=[args.edge])

def parseFile(inputFile, currentFigure=None, delimiter='\t', save=False, sizes=[10], colors=['black'], shapes=['o'], edgeColors=['none']):
	"""
	"""

	matrix = np.genfromtxt(inputFile, delimiter=delimiter)
	numberOfColumns = matrix.shape[1]

	# The first column (column 0) is the x values for the second column (column 1).
	# In general, column x is the x values and x + 1 the corresponding y values.
	xValues = [matrix[:, i] for i in range(numberOfColumns)[0::2]]  # The x values are even numbered columns.
	yValues = [matrix[:, i] for i in range(numberOfColumns)[1::2]]  # The y values are odd numbered columns.
	graphGeneration(xValues, yValues, currentFigure=currentFigure, save=save, sizes=sizes, colors=colors, shapes=shapes, edgeColors=edgeColors)
		

def graphGeneration(xValues, yValues, currentFigure=None, save=False, sizes=[10], colors=['black'], shapes=['o'], edgeColors=['none']):
	"""
	"""

	numberOfDatasets = len(xValues)
	# If any sizes are not provided, then fill in the missing ones with 10.
	sizes += [10] * (numberOfDatasets - len(sizes))
	# If any colors are not provided, then fill in the missing ones with 'black'.
	colors += ['black'] * (numberOfDatasets - len(colors))
	# If any shapes are not provided, then fill in the missing ones with '.'.
	shapes += ['o'] * (numberOfDatasets - len(shapes))
	# If any edge colors are not provided, then fill in the missing ones with 'none'.
	edgeColors += ['none'] * (numberOfDatasets - len(edgeColors))

	try:
		axes = currentFigure.gca()
	except AttributeError:
		# If the figure is not given then create it.
		currentFigure = plt.figure()
		axes = currentFigure.add_subplot(1, 1, 1)

	for i in range(len(xValues)):
		axes.scatter(xValues[i], yValues[i], s=sizes[i], c=colors[i], marker=shapes[i], edgecolor=edgeColors[i])

	if save:
		pass

if __name__ == '__main__':
	commandLine(sys.argv)