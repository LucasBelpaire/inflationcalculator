# Author: Lucas Belpaire
# API: www.statbureau.org
# little script to calculate inflation
# arguments for the script are: start_date, end_date, amount
#!/usr/bin/env
import requests
import urllib
import re

def calculateInflation(start_date, end_date, amount):
	"""
	Returns the amount (in dollars) adjusted for inflation.
	The amount parameter is the amount (in dollars) on the start_date
	The return value is the adjusted amount on the end_date  
	"""
	main_api = 'https://www.statbureau.org/calculate-inflation-price-jsonp?'
	country = 'united-states'
	url = main_api + urllib.parse.urlencode({
		'country': country,
		'start': start_date,
		'end': end_date,
		'amount' : amount,
		'format' : True
		})
	# used regex to remove all characters except or digits or the first dot
	result = requests.get(url)
	float_re = re.compile(r'[^\d.]+')
	float_result = float_re.sub('', result.text)
	return float_result