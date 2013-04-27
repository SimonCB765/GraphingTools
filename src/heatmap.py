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
	parser.add_argument('-d', '--delimiter', default='\t', help='the delimiter for the lines of the input file')
	parser.add_argument('--normMin', default=None, help='the minimum value used for the normalisation')
	parser.add_argument('--normMax', default=None, help='the maximum value used for the normalisation')
	parser.add_argument('-c', '--colorMap', default='jet', choices=['jet'], help='the color map to use')
	args = parser.parse_args()
	parseFile(args.inputFile, delimiter=args.delimiter, normMin=args.normMin, normMax=args.normMax, colorMap=args.colorMap)

def parseFile(inputFile, delimiter='\t', normMin=None, normMax=None, colorMap='jet'):
	"""
	"""

	similarities = np.loadtxt(inputFile, delimiter=delimiter)
	graphGeneration(similarities, normMin=normMin, normMax=normMax, colorMap=colorMap)
		

def graphGeneration(similarities, divisions=[], normMin=None, normMax=None, colorMap='jet'):
	"""
	"""

	numberOfIndividuals = len(similarities)

	norm = colors.Normalize(vmin=normMin, vmax=normMax)
	plt.pcolormesh(similarities, norm=norm)
	plt.set_cmap(colorMap)
	plt.colorbar()
	plt.plot([0, numberOfIndividuals], [0, numberOfIndividuals], color='k')
	for i in divisions:
		plt.plot([i, i], [0, numberOfIndividuals], color='k', linewidth=2)
		plt.plot([0, numberOfIndividuals], [i, i], color='k', linewidth=2)
	plt.xlim(xmax=numberOfIndividuals)
	plt.ylim(ymax=numberOfIndividuals)
	axes = plt.gca()
	xAxis = axes.get_xaxis()
	xAxis.set_visible(False)
	yAxis = axes.get_yaxis()
	yAxis.set_visible(False)
	plt.show()

if __name__ == '__main__':
	commandLine(sys.argv)