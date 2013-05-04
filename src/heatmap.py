import argparse
from matplotlib import cm
from matplotlib import colors
import matplotlib.pyplot as plt
import numpy as np
import sys

def commandLine(args):
	"""
	"""

	parser = argparse.ArgumentParser(description='Process the command line input for creating a heatmap.')
	parser.add_argument('inputFile', help='an input file containing the values for the heatmap')
	parser.add_argument('saveLocation', help='the location to save the image')
	parser.add_argument('-d', '--delimiter', default='\t', help='the delimiter for the lines of the input file')
	parser.add_argument('--normMin', default=None, help='the minimum value used for the normalisation')
	parser.add_argument('--normMax', default=None, help='the maximum value used for the normalisation')
	parser.add_argument('-c', '--colorMap', default='jet', help='the color map to use')
	args = parser.parse_args()
	parseFile(args.inputFile, delimiter=args.delimiter, normMin=args.normMin, normMax=args.normMax, colorMap=args.colorMap, save=args.saveLocation)

def parseFile(inputFile, currentFigure=None, delimiter='\t', normMin=None, normMax=None, colorMap='jet', save=False):
	"""
	"""

	similarities = np.genfromtxt(inputFile, delimiter=delimiter)  # Load in the data used to generate the heatmap.
	graphGeneration(similarities, currentFigure=currentFigure, normMin=normMin, normMax=normMax, colorMap=colorMap, save=save)
		

def graphGeneration(similarities, currentFigure=None, divisions=[], normMin=None, normMax=None, colorMap='jet', save=False):
	"""
	"""

	numberOfIndividuals = len(similarities)

	# Get the current axes for the current figure.
	try:
		axes = currentFigure.gca()
	except AttributeError:
		# If the figure is not given then create it.
		currentFigure = plt.figure()
		axes = currentFigure.add_subplot(1, 1, 1)

	norm = colors.Normalize(vmin=normMin, vmax=normMax)  # Normalise the values for the heatmap to be between normMin and normMax.
	heatmap = axes.pcolormesh(similarities, norm=norm, cmap=colorMap)  # Generate the heatmap.
	currentFigure.colorbar(heatmap)  # Add the colorbar.
	axes.plot([0, numberOfIndividuals], [0, numberOfIndividuals], color='k')  # Plot a diagonal line y=x.

	# If any dividing lines were specified, then plot them through the x and y axes.
	for i in divisions:
		axes.plot([i, i], [0, numberOfIndividuals], color='k', linewidth=2)
		axes.plot([0, numberOfIndividuals], [i, i], color='k', linewidth=2)

	# Set the upper limits of the x and y axes to be tight to te heatmap (no whitespace to the left or top of the fiure).
	axes.set_xlim(right=numberOfIndividuals)
	axes.set_ylim(top=numberOfIndividuals)

	# Make the numbering on the axes invisible.
	axes.set_xticks([])
	axes.set_yticks([])

	if save:
		pass

if __name__ == '__main__':
	commandLine(sys.argv)