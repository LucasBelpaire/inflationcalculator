# Author: Lucas Belpaire
#!/usr/bin/env
import inflation_data

data = inflation_data.data

def calculate_inflation(start_year, end_year, amount):
	"""
	Returns the amount (in dollars) adjusted for inflation.
	The amount parameter is the amount (in dollars) on the start_year
	The return value is the adjusted amount on the end_year  
	"""
	CPI_start_year = data[start_year]
	CPI_end_year = data[end_year]

	CPI_difference = CPI_end_year - CPI_start_year

	inflation_rate = CPI_difference / CPI_start_year

	adjusted_amount = amount * (1 + inflation_rate)

	return adjusted_amount