#!/usr/bin/python3

import pandas as pd


def main():
	''' main function'''

	filename = 'COVID-19 South Carolina Celeration Charts - RAW DATA.csv'
	df = pd.read_csv(filename)
	print(df)


if __name__ == '__main__':
	main()
