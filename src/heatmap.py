import argparse
from matplotlib import cm
from matplotlib import colors
import numpy as np
import pylab
import sys

def commandLine(args):
	"""
	uses a -f argument to indicate the file input type
	"""

	parser = argparse.ArgumentParser(description='Process the command line input for creating a heatmap.')
	parser.add_argument('inputFile', help='an input file containing the values for the heatmap')
	parser.add_argument('-f', '--format', default='tsv', choices=['tsv', 'csv'], help='the format of the input file')
	parser.add_argument('--normMin', default=None, help='the minimum value used for the normalisation')
	parser.add_argument('--normMax', default=None, help='the maximum value used for the normalisation')
	parser.add_argument('-c', '--colorMap', default='jet', choices=['jet'], help='the color map to use')
	args = parser.parse_args()
	delimiter = '\t'
	if args.format == 'csv':
		delimiter = ','
	parseFile(args.inputFile, delimiter=delimiter, normMin=args.normMin, normMax=args.normMax, colorMap=args.colorMap)

def parseFile(inputFile, delimiter='\t', normMin=None, normMax=None, colorMap='jet'):
	"""
	"""

	similarities = np.loadtxt(inputFile, delimiter=delimiter)
	graphGeneration(similarities, normMin=normMin, normMax=normMax, colorMap=colorMap)
		

def graphGeneration(similarities, normMin=None, normMax=None, colorMap='jet'):
	"""
	"""

	numberOfIndividuals = len(similarities)
	xAxis = np.array(range(numberOfIndividuals + 1))
	yAxis = np.array(range(numberOfIndividuals + 1))

	norm = colors.Normalize(vmin=normMin, vmax=normMax)
	pylab.pcolormesh(xAxis, yAxis, similarities, cmap=cm.jet, norm=norm)
	pylab.show()

if __name__ == '__main__':
	commandLine(sys.argv)