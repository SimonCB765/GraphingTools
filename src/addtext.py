import matplotlib.pyplot as plt

def graphGeneration(xValues, yValues, textToAdd, currentFigure=None, save=False, sizes=[10], colors=['black'], hAlignments=['center'],
		vAlignments=['center'], rotations=[0], zorders=[0]):
	"""
	"""

	numberOfDatasets = len(xValues)
	# If any sizes are not provided, then fill in the missing ones with 10.
	sizes += [10] * (numberOfDatasets - len(sizes))
	# If any colors are not provided, then fill in the missing ones with 'black'.
	colors += ['black'] * (numberOfDatasets - len(colors))
	# If any horizontal alignments are not provided, then fill in the missing ones with 'center'.
	hAlignments += ['center'] * (numberOfDatasets - len(hAlignments))
	# If any vertical alignments are not provided, then fill in the missing ones with 'center'.
	vAlignments += ['center'] * (numberOfDatasets - len(vAlignments))
	# If any rotations are not provided, then fill in the missing ones with 0.
	rotations += [0] * (numberOfDatasets - len(rotations))
	# If any zorders are not provided, then fill in the missing ones so that they are greater than the specified ones.
	smallestNewZorder = min(zorders) - 1
	while len(zorders) < numberOfDatasets:
		zorders += [smallestNewZorder]
		smallestNewZorder -= 1

	try:
		axes = currentFigure.gca()
	except AttributeError:
		# If the figure is not given then create it.
		currentFigure = plt.figure()
		axes = currentFigure.add_subplot(1, 1, 1)

	for i in range(len(xValues)):
		axes.text(xValues[i], yValues[i], textToAdd[i], size=sizes[i], color=colors[i], horizontalalignment=hAlignments[i],
			verticalalignment=vAlignments[i], rotation=rotations[i], zorder=zorders[i])

	if save:
		pass