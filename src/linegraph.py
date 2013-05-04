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
	parseFile(args.inputFile, delimiter=args.delimiter, save=args.saveLocation, markersize=[args.markerSize], shape=[args.shape], lineColor=[args.lineColor],
		lineStyle=[args.lineStyle], lineWidth=[args.lineWidth], label=[args.label])

def parseFile(inputFile, currentFigure=None, delimiter='\t', save=False, markersize=[10], lineColor=['black'], shape=['o'], lineStyle=['-'],
		lineWidth=[2], label=['']):
	"""
	"""

	matrix = np.genfromtxt(inputFile, delimiter=delimiter)
	numberOfColumns = matrix.shape[1]

	# The first column (column 0) is the x values for the second column (column 1).
	# In general, column x is the x values and x + 1 the corresponding y values.
	xValues = [matrix[:, i] for i in range(numberOfColumns)[0::2]]  # The x values are even numbered columns.
	yValues = [matrix[:, i] for i in range(numberOfColumns)[1::2]]  # The y values are odd numbered columns.
	graphGeneration(xValues, yValues, currentFigure=currentFigure, save=save, markersize=markersize, shape=shape, lineColor=lineColor, lineStyle=lineStyle,
		lineWidth=lineWidth, label=label)
		

def graphGeneration(xValues, yValues, currentFigure=None, save=False, markersize=[10], shape=['o'], lineColor=['black'], lineStyle=['-'], lineWidth=[2],
		label=['']):
	"""
	"""

	numberOfLines = len(xValues)
	# If any marker sizes are not provided, then fill in the missing ones with 10.
	markersize += [10] * (numberOfLines - len(markersize))
	# If any shapes are not provided, then fill in the missing ones with 'o'.
	shape += ['o'] * (numberOfLines - len(shape))
	# If any line colors are not provided, then fill in the missing ones with 'black'.
	lineColor += ['black'] * (numberOfLines - len(lineColor))
	# If any line styles are not provided, then fill in the missing ones with '-'.
	lineStyle += ['-'] * (numberOfLines - len(lineStyle))
	# If any line wdiths are not provided, then fill in the missing ones with 2.
	lineWidth += [2] * (numberOfLines - len(lineWidth))
	# If any labels are not provided, then fill in the missing ones with ''.
	label += [''] * (numberOfLines - len(label))

	try:
		axes = currentFigure.gca()
	except AttributeError:
		# If the figure is not given then create it.
		currentFigure = plt.figure()
		axes = currentFigure.add_subplot(1, 1, 1)

	for i in range(len(xValues)):
		axes.plot(xValues[i], yValues[i], markersize=markersize[i], color=lineColor[i], marker=shape[i], linestyle=lineStyle[i], linewidth=lineWidth[i],
			label=label[i])

	if save:
		pass

if __name__ == '__main__':
	commandLine(sys.argv)