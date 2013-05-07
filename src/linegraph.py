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
	parser.add_argument('--markerSize', default=0, type=int, help='the size of the point')
	parser.add_argument('--shape', default='o', help='the shape of the point')

	parser.add_argument('--lineColor', default='black', help='the color of the line')
	parser.add_argument('--lineStyle', default='-', help='the style of the line')
	parser.add_argument('--lineWidth', default=2, type=float, help='the width of the line')
	parser.add_argument('--label', default='', help='the label of the line')
	
	args = parser.parse_args()
	parseFile(args.inputFile, delimiter=args.delimiter, save=args.saveLocation, markerSizes=[args.markerSize], shapes=[args.shape], lineColors=[args.lineColor],
		lineStyles=[args.lineStyle], lineWidths=[args.lineWidth], labels=[args.label])

def parseFile(inputFile, currentFigure=None, delimiter='\t', save=False, markerSizes=[10], lineColors=['black'], shapes=['o'], lineStyles=['-'],
		lineWidths=[2], labels=['']):
	"""
	"""

	matrix = np.genfromtxt(inputFile, delimiter=delimiter)
	numberOfColumns = matrix.shape[1]

	# The first column (column 0) is the x values for the second column (column 1).
	# In general, column x is the x values and x + 1 the corresponding y values.
	xValues = [matrix[:, i] for i in range(numberOfColumns)[0::2]]  # The x values are even numbered columns.
	yValues = [matrix[:, i] for i in range(numberOfColumns)[1::2]]  # The y values are odd numbered columns.
	graphGeneration(xValues, yValues, currentFigure=currentFigure, save=save, markerSizes=markerSizes, shapes=shapes, lineColors=lineColors, lineStyles=lineStyles,
		lineWidths=lineWidths, labels=labels)
		

def graphGeneration(xValues, yValues, currentFigure=None, save=False, markerSizes=[10], shapes=['o'], lineColors=['black'], lineStyles=['-'], lineWidths=[2],
		labels=[''], zorders=[0]):
	"""
	"""

	numberOfLines = len(xValues)
	# If any marker sizes are not provided, then fill in the missing ones with 10.
	markerSizes += [10] * (numberOfLines - len(markerSizes))
	# If any shapes are not provided, then fill in the missing ones with 'o'.
	shapes += ['o'] * (numberOfLines - len(shapes))
	# If any line colors are not provided, then fill in the missing ones with 'black'.
	lineColors += ['black'] * (numberOfLines - len(lineColors))
	# If any line styles are not provided, then fill in the missing ones with '-'.
	lineStyles += ['-'] * (numberOfLines - len(lineStyles))
	# If any line wdiths are not provided, then fill in the missing ones with 2.
	lineWidths += [2] * (numberOfLines - len(lineWidths))
	# If any labels are not provided, then fill in the missing ones with ''.
	labels += [''] * (numberOfLines - len(labels))
	# If any zorders are not provided, then fill in the missing ones so that they are greater than the specified ones.
	smallestNewZorder = min(zorders) - 1
	while len(zorders) < numberOfLines:
		zorders += [smallestNewZorder]
		smallestNewZorder -= 1

	try:
		axes = currentFigure.gca()
	except AttributeError:
		# If the figure is not given then create it.
		currentFigure = plt.figure()
		axes = currentFigure.add_subplot(1, 1, 1)

	for i in range(len(xValues)):
		axes.plot(xValues[i], yValues[i], markersize=markerSizes[i], color=lineColors[i], marker=shapes[i], linestyle=lineStyles[i], linewidth=lineWidths[i],
			label=labels[i], zorder=zorders[i])

	if save:
		pass

if __name__ == '__main__':
	commandLine(sys.argv)