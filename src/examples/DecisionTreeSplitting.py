import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
import numpy as np
import sys

import os
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)
import scatterplot
import barchart


def main(figureSaveLocation):
	"""
	"""

	# Class 1 data and control variables
	class1X = np.array([0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 4.9])
	class1Y = np.array([1.0, 2.0, 1.0, 2.0, 1.0, 2.0, 1.0, 2.0, 1.0, 2.0, 1.0])
	class1Color = ['black']
	class1Size = [30]

	# Class 2 data and control variables
	class2X = np.array([1, 2])
	class2Y = np.array([9, 8])
	class2Color = ['#FF0000']  # Red
	class2Size = [30]

	# Class 3 data and control variables
	class3X = np.array([7, 8])
	class3Y = np.array([2, 1])
	class3Color = ['#00FF00']  # Blue
	class3Size = [30]

	# Class 4 data and control variables
	class4X = np.array([9, 7])
	class4Y = np.array([8, 7])
	class4Color = ['#0000FF']  # Green
	class4Size = [30]

	# Aggregate all class information.
	scatterXValues = [class1X, class2X, class3X, class4X]
	scatterXAllValues = [j for i in scatterXValues for j in i]
	scatterXMin = min(scatterXAllValues)
	scatterXMax = max(scatterXAllValues)
	scatterYValues = [class1Y, class2Y, class3Y, class4Y]
	scatterYAllValues = [j for i in scatterYValues for j in i]
	scatterYMin = min(scatterYAllValues)
	scatterYMax = max(scatterYAllValues)
	barChartXValues = []
	barChartYValues = []
	colors = [class1Color, class2Color, class3Color, class4Color]
	sizes = [class1Size, class2Size, class3Size, class4Size]

	currentFigure = plt.figure()

	gsTopRow = gridspec.GridSpec(3, 6)
	gsTopRow.update(left=0.005, right=0.995, bottom=0.05, top=1, wspace=0.05)#, hspace=0.05)
	topRowScatterPlot = plt.subplot(gsTopRow[0, 1:3])
	scatterplot.graphGeneration(scatterXValues, scatterYValues, currentFigure=currentFigure, colors=colors, sizes=sizes)
	topRowScatterPlot.set_xlim(left=scatterXMin - 0.5, right=scatterXMax + 0.5)
	topRowScatterPlot.set_ylim(bottom=scatterYMin - 0.5, top=scatterYMax + 0.5)
	topRowBarChart = plt.subplot(gsTopRow[0, 3:-1])

	gsMidRow = gridspec.GridSpec(3, 6)
	gsMidRow.update(left=0.005, right=0.995, bottom=0.05, top=1, wspace=0.05)#, hspace=0.05)
	midRowScatterPlot = plt.subplot(gsMidRow[1, :2])
	scatterplot.graphGeneration(scatterXValues, scatterYValues, currentFigure=currentFigure, colors=colors, sizes=sizes)
	midRowScatterPlot.set_xlim(left=scatterXMin - 0.5, right=scatterXMax + 0.5)
	midRowScatterPlot.set_ylim(bottom=scatterYMin - 0.5, top=scatterYMax + 0.5)
	midRowLeftBarChart = plt.subplot(gsMidRow[1, 2:4])
	midRowRightBarChart = plt.subplot(gsMidRow[1, 4:])

	gsBotRow = gridspec.GridSpec(3, 6)
	gsBotRow.update(left=0.005, right=0.995, bottom=0.05, top=1, wspace=0.05)#, hspace=0.05)
	botRowScatterPlot = plt.subplot(gsBotRow[2, :2])
	scatterplot.graphGeneration(scatterXValues, scatterYValues, currentFigure=currentFigure, colors=colors, sizes=sizes)
	botRowScatterPlot.set_xlim(left=scatterXMin - 0.5, right=scatterXMax + 0.5)
	botRowScatterPlot.set_ylim(bottom=scatterYMin - 0.5, top=scatterYMax + 0.5)
	botRowLeftBarChart = plt.subplot(gsBotRow[2, 2:4])
	botRowRightBarChart = plt.subplot(gsBotRow[2, 4:])

	# Make all the tick marks invisible, and label the x axes.
	labels = ['(h)', '(g)', '(f)', '(e)', '(d)', '(c)', '(b)', '(a)']
	for ax in currentFigure.get_axes():
		hideTickMarks(ax, xAxis=True, yAxis=True)
		currentLabel = labels.pop()
		setLabels(ax, xLabel=currentLabel)
		ax.xaxis.set_label_coords(0.5, -0.025)

	plt.savefig('C:/Users/Simon/Desktop/Foo.png', bbox_inches=0)
	plt.show()

def setLabels(axes, xLabel='', yLabel=''):
	"""
	"""

	axes.set_xlabel(xLabel)
	axes.set_ylabel(yLabel)

def hideAxesLabelling(axes, xAxis=False, yAxis=False):
	"""Hides all tick marks, tick labels, axis labels, etc.
	"""

	if xAxis:
		axes.xaxis.set_visible(False)
	if yAxis:
		axes.yaxis.set_visible(False)

def hideTickMarks(axes, xAxis=False, yAxis=False):
	"""
	"""

	if xAxis:
		axes.set_xticks([])
	if yAxis:
		axes.set_yticks([])

def hideTickLabels(axes, xAxis=False, yAxis=False):
	"""
	"""

	if xAxis:
		axes.set_xticklabels([])
	if yAxis:
		axes.set_yticklabels([])


if __name__ == '__main__':
	main(sys.argv[1])