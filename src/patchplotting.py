import matplotlib.pyplot as plt
import numpy as np

def graphGeneration(patches, currentFigure=None, save=False, edgeColors=['black'], faceColors=['black'], alphas=[1.0], zorders=[0]):
	"""
	patches is a list of matplotlib.patches objects
	"""

	numberOfDatasets = len(patches)
	# If any edge colors are not provided, then fill in the missing ones with 'none'.
	edgeColors += ['none'] * (numberOfDatasets - len(edgeColors))
	# If any face colors are not provided, then fill in the missing ones with 'black'.
	faceColors += ['black'] * (numberOfDatasets - len(faceColors))
	# If any alphas are not provided, then fill in the missing ones with 1.0.
	alphas += [1.0] * (numberOfDatasets - len(alphas))
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

	for i in range(len(patches)):
		patch = patches[i]
		patch.set_edgecolor(edgeColors[i])
		patch.set_facecolor(faceColors[i])
		patch.set_alpha(alphas[i])
		patch.set_zorder(zorders[i])
		axes.add_artist(patch)

	if save:
		pass