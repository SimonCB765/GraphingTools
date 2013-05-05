import argparse
from matplotlib import cm
from matplotlib import colors
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
	parser.add_argument('--color', default='black', help='the color of the bars')
	parser.add_argument('--width', default=0.8, type=float, help='the width of the bars')
	args = parser.parse_args()
	parseFile(args.inputFile, delimiter=args.delimiter, save=args.saveLocation, colors=[args.color], width=args.width)

def parseFile(inputFile, currentFigure=None, delimiter='\t', save=False, colors=['black'], width=0.8):
	"""
	"""

	occurences = np.genfromtxt(inputFile, delimiter=delimiter)
	numberOfRows = occurences.shape[0]
	numberOfColumns = occurences.shape[1]

	integerIncrease = np.ceil(width * numberOfColumns)  # Determine the amount of space that each set of bars needs.
	midIndex = integerIncrease / 2.0  # Determine the mean of the cut off for bars that should go below the center dividing lineand those that should go above.
	centerBarIndices = np.arange(midIndex, numberOfRows * integerIncrease, integerIncrease)  # Determine the center of each grouping of bars.

	lowerThanMidIndex = [i for i in range(numberOfColumns) if i < midIndex]  # Determine the indices of the collections of bars that are below the middle index.
	lowerXAxisLocations = [centerBarIndices - (width * (lowerThanMidIndex[-(i + 1)] + 1)) for i in lowerThanMidIndex]  # Determine the locations on the x axis for each of the bars in the collections that have indices below the middle index.
	greaterXAxisLocations = [centerBarIndices + (width * lowerThanMidIndex[i]) for i in lowerThanMidIndex]  # Determine the locations on the x axis for each of the bars in the collections that have indices above the middle index.
	xAxisLocations = lowerXAxisLocations + greaterXAxisLocations
	barHeightValues = [occurences[:, i] for i in range(numberOfColumns)]
	graphGeneration(xAxisLocations, barHeightValues, save=save, tickLocations=centerBarIndices, colors=colors, width=width)
		

def graphGeneration(xAxisLocations, barHeightValues, currentFigure=None, save=False, tickLocations=None, colors=['black'], width=0.8):
	"""
	"""

	numberOfBarCollections = len(barHeightValues)
	# If any colors are not provided, then fill in the missing ones with 'black'.
	colors += ['black'] * (numberOfBarCollections - len(colors))

	try:
		axes = currentFigure.gca()
	except AttributeError:
		# If the figure is not given then create it.
		currentFigure = plt.figure()
		axes = currentFigure.add_subplot(1, 1, 1)

	for i in range(len(barHeightValues)):
		axes.bar(xAxisLocations[i], barHeightValues[i], color=colors[i], width=width)

	try:
		axes.set_xticks(tickLocations)
	except Exception:
		pass

	if save:
		pass

if __name__ == '__main__':
	commandLine(sys.argv)