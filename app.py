#!/usr/bin/python3

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, ScalarFormatter
import numpy as np
import datetime
import os
import fit_curve


def main():
	''' main function'''

	filename = 'COVID-19 South Carolina Celeration Charts - RAW DATA.csv'

	# Read the file to a dataframe and make the date column the index
	df = pd.read_csv(filename, index_col=1)

	y_pred = fit_curve.regression(df, None, None)
	#print(y_pred)

	# Change date column to datetime
	#df.loc[:, 'Date'] = pd.to_datetime(df.loc[:, 'Date'], infer_datetime_format=True)
	#print(df['Date'])

	# Build plot
	fig = plt.figure()
	fig.set_size_inches(11, 8.5)

	# Plot data
	ax1 = df['New Cases (SC)'].plot(kind='line', color='k', marker='.', linewidth=1, logy=True, legend=True)
	ax1 = df['Daily deaths'].plot(kind='line', color='r', marker='x', linewidth=1, logy=True, legend=True)
	ax1 = y_pred[0].plot(kind='line', linestyle='dotted', color='k')

	# Set the range for the y-axis
	ax1.set_ylim([1, 1000000])

	# Turn on major and minor grid lines for y-axis
	ax1.yaxis.grid(True, color='lightsteelblue', which='minor', linestyle='-', alpha=0.5)
	ax1.yaxis.grid(True, color='lightsteelblue', which='major', linestyle='-', alpha=0.8)

	# Set the range for the x-axis
	#ax1.set_xlim([datetime.date(2020, 3, 1), datetime.date(2020, 7, 19)])
	ax1.set_xlim([0, 140])

	# Set x-labels
	#ax1.set_xticklabels(np.arange(0, 141, 7))
	

	# Set the location for x-axis ticks
	ax1.xaxis.set_minor_locator(MultipleLocator(1))
	ax1.xaxis.set_major_locator(MultipleLocator(7))

	# Turn on the major and minor grid lines for x-axis
	ax1.xaxis.grid(True, color='lightsteelblue', which='minor', linestyle='-', alpha=0.5)
	ax1.xaxis.grid(True, color='lightsteelblue', which='major', linestyle='-', alpha=0.8)

	# Create secondary x-axis
	ax2 = ax1.twiny()

	newlabel = list(df['Date'])
	newlabel = newlabel[::28]
	ax2.set_xticklabels(newlabel)
	plt.xticks(rotation=60)

	# Label axes and title
	plt.title('2019 nCoV Daily Cases in South Carolina', color='midnightblue')

	ax1.set_xlabel('Successive Calendar Days')
	ax1.set_ylabel('Counts of Cases and Deaths')

	plt.tight_layout()

	plt.savefig('SC-chart.png')
	plt.show()

	plt.close()	


if __name__ == '__main__':
	main()
