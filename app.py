#!/usr/bin/python3

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, ScalarFormatter
import numpy as np
import datetime
import os


def main():
	''' main function'''

	filename = 'COVID-19 South Carolina Celeration Charts - RAW DATA.csv'
	df = pd.read_csv(filename)

	# Build plot
	fig = plt.figure()
	fig.set_size_inches(11, 8.5)

	ax = df['New Cases (SC)'].plot(kind='line', color='k', marker='.', linewidth=1, logy=True, legend=True)
	ax = df['Daily deaths'].plot(kind='line', color='r', marker='x', linewidth=1, logy=True, legend=True)

	# Set the range for the y-axis
	ax.set_ylim([1, 1000000])

	# Turn on major and minor grid lines for y-axis
	ax.yaxis.grid(True, color='lightsteelblue', which='minor', linestyle='-', alpha=0.5)
	ax.yaxis.grid(True, color='lightsteelblue', which='major', linestyle='-', alpha=0.8)

	# Set the range for the x-axis
	#ax.set_xlim([datetime.date(2020, 3, 1), datetime.date(2020, 7, 20)])

	# Set the location for x-axis ticks
	ax.xaxis.set_minor_locator(MultipleLocator(1))
	ax.xaxis.set_major_locator(MultipleLocator(7))

	# Turn on the major and minor grid lines for x-axis
	ax.xaxis.grid(True, color='lightsteelblue', which='minor', linestyle='-', alpha=0.5)
	ax.xaxis.grid(True, color='lightsteelblue', which='major', linestyle='-', alpha=0.8)

	# Set x-labels
	ax.set_xticklabels(np.arange(0, 141, 7))

	# Label axes and title
	plt.title('2019 nCoV Daily Cases in South Carolina', color='midnightblue')
	plt.xlabel('Successive Calendar Days')
	plt.ylabel('Counts of Cases and Deaths')

	plt.savefig('SC-chart.png')
	plt.show()
	


if __name__ == '__main__':
	main()
