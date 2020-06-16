#!/usr/bin/python3

import pandas as pd
import numpy as np
import datetime
from sklearn.linear_model import LinearRegression
import math
import matplotlib.pyplot as plt
#import charting


def main():
	''' main function'''

	# Load test data
	df = pd.read_csv('China_regression_test_data.csv', index_col=0)
		
	stop_date = None

	# Prep data
	df, date = prep_data(df, stop_date)

	# Regression
	df, celeration = regression(df, date, True)

	return



def regression(df, date, multi_trend):
	''' performs linear regression'''

	# Initialize blank data frames
	predictions = pd.DataFrame()
	upper_confidence_interval = pd.DataFrame()
	lower_confidence_interval = pd.DataFrame()

	while True:
	
		# Get the date range of the trend to be analyzed
		start_day = int(input('What is the start day of the trend? '))
		end_day = int(input('What is the end day of the trend? '))
		celeration_days = end_day - start_day
		shift = start_day

		# Slice the dataframe based on those dates
		current_df = df.iloc[start_day:end_day+1, :]

		current_df = current_df.fillna(1)
		current_df = current_df.replace(to_replace=0, value=1)
		
		# Create X and Y prediction spaces
		num = len(current_df)
		X = np.arange(0, num).reshape(-1, 1)
		Y = current_df.iloc[0:num, 2].values.reshape(-1, 1)

		# Perform regression	
		linear_regressor = LinearRegression()
		linear_regressor.fit(X, np.log(Y))

		# Get linear regression parameters
		m = linear_regressor.coef_
		b = linear_regressor.intercept_

		values = []
		uci = []
		lci = []

		for value in range(start_day, end_day+1):
			values.append(math.exp(m*(value-shift) + b))
			uci.append(1.90 * math.exp(m*(value-shift) + b))
			lci.append(0.90 * math.exp(m*(value-shift) + b))

		values = pd.DataFrame(values, index=np.arange(start_day,(end_day+1)))
		uci = pd.DataFrame(uci, index=np.arange(start_day,(end_day+1)))
		lci = pd.DataFrame(lci, index=np.arange(start_day,(end_day+1)))
		#print(ci)	

		predictions = predictions.append(values, ignore_index=True)
		upper_confidence_interval = upper_confidence_interval.append(uci, ignore_index=True)
		lower_confidence_interval = lower_confidence_interval.append(lci, ignore_index=True)

		#high_value = int(input('High value? '))
		#high_day = int(input('High day? '))

		more_trends = input('Do you want to add more trends? ')

		if more_trends != 'Yes':
			break

	# Create a data frame the size of the celeration chart and fill it with the calculated values
	#predictions = pd.DataFrame(index=np.arange(0, 141), data=None)
	#print(predictions)
	
	return predictions, upper_confidence_interval, lower_confidence_interval #y_pred  #original_df, celeration


if __name__ == '__main__':
	main()
