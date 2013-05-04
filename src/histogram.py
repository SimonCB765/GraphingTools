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
	parser.add_argument('-c', '--colorMap', default='jet', help='the color map to use')
	args = parser.parse_args()
	parseFile(args.inputFile, delimiter=args.delimiter, colorMap=args.colorMap, save=args.saveLocation)

def parseFile(inputFile, currentFigure=None, delimiter='\t', colorMap='jet', save=False):
	"""
	"""

	occurences = np.genfromtxt(inputFile, delimiter=delimiter)
	graphGeneration(occurences, colorMap=colorMap, save=save)
		

def graphGeneration(values, currentFigure=None, colorMap='jet', bins=10, range=None, save=False):
	"""
	"""

	try:
		axes = currentFigure.gca()
	except AttributeError:
		# If the figure is not given then create it.
		currentFigure = plt.figure()
		axes = currentFigure.add_subplot(1, 1, 1)

	axes.hist(values, bins=bins, range=range)

	if save:
		pass

if __name__ == '__main__':
	commandLine(sys.argv)