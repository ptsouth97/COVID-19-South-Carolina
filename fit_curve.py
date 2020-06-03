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
	'''
	while True:
	
		if multi_trend == True:
			trends = int(input('How many trends? '))

		else:
			trends = 1

		for trend in range(0, trends):

			# find number of days between end of chart and start date
			if multi_trend == False:
				start = df.index[0]
				end = datetime.datetime(2020, 5, 17)

			else:
				start_year = int(input('What is the start date year? '))
				start_mon = int(input('What is the start date month? '))
				start_day = int(input('What is the start date day? '))
				start = datetime.datetime(start_year, start_mon, start_day)

				end_year = int(input('What is the end date year? '))
				end_mon = int(input('What is the end date month? '))
				end_day = int(input('What is the end date day? '))
				end = datetime.datetime(end_year, end_mon, end_day)

			df = df.loc[start:end]
			
			print(df)

			days = (end - start).days
			shift = 140 - days
	'''

	# Get the date range of the trend to be analyzed
	start_day = 13
	end_day = 32
	celeration_days = end_day - start_day
	shift = start_day

	# Slice the dataframe based on those dates
	df = df.iloc[13:33, :]

	df = df.fillna(1)
	df = df.replace(to_replace=0, value=1)

	# Create X and Y prediction spaces
	num = len(df)
	X = np.arange(0, num).reshape(-1, 1)
	Y = df.iloc[0:num, 1].values.reshape(-1, 1)

	# Perform regression	
	linear_regressor = LinearRegression()
	linear_regressor.fit(X, np.log(Y))

	# Get linear regression parameters
	m = linear_regressor.coef_
	b = linear_regressor.intercept_

	values = []

	for value in range(1, 140):
		values.append(math.exp(m*(value-shift) + b))

	values = pd.DataFrame(values)
	

	# Create a data frame the size of the celeration chart and fill it with the calculated values
	#predictions = pd.DataFrame(index=[np.arange(1, celeration_days)], data=values)
	


	'''
			# Initialize and fill data frame for regression results
			values = []
	
			for value in range(1, days): #140): #days+1):   # changed 'begin' from '1'
				values.append(math.exp(m*(value-shift) + b))

			# Create a data frame the size of the celeration chart and fill it with the calculated values
			predictions = pd.DataFrame(index=[np.arange(1, days)], data=values)

			# Create a data frame to join with the predictions that matches the size of the celeration chart
			total_days = 140
			early_days = 140 - days
			early_predictions = pd.DataFrame(np.zeros((early_days, 1)))

			predictions = predictions.append(early_predictions)
			predictions.reset_index(inplace=True)
			predictions.drop(['index'], axis=1, inplace=True)


			# Convert index back to dates
			dates = predictions.index.values
			dates = dates.tolist()
	
			dates = [ datetime.datetime(2019, 12, 29) + datetime.timedelta(days=date) for date in dates ]

			predictions['dates'] = dates
			predictions.set_index('dates', inplace=True)
			predictions = predictions.rename(columns={0: 'celeration curve'})
			predictions.replace(to_replace=0, value=np.nan, inplace=True)
	

			# Calculate the celeration value
			week1 = float(predictions.iloc[78])
			week0 = float(predictions.iloc[71])
			celeration = week1 / week0

			original_df = pd.concat([df, predictions], axis=1)

			if multi_trend == True:
				print(original_df)
				charting.plot_data(original_df, 'China', None, celeration, date, 'solo', multi_trend)
		
		if multi_trend == True:
			satisfied = input("Are you satisfied with the result? ")
				
			if satisfied == "Yes":
				break

		else:
			break
	'''
	return values #y_pred  #original_df, celeration


if __name__ == '__main__':
	main()
