"""
11. Popular Python Packages, 04. Searching for Businesses

https://www.yelp.com/developers

Utilizing the Yelp API in Python. 
Import requests.
Follow instructions to generate API key. 

"""
import requests
import config


url = "https://api.yelp.com/v3/businesses/search"
headers = {
    "Authorization": "Bearer " + config.api_key
}
params = {
    "term": "barber",
    "location": "NYC"
}
response = requests.get(url, headers=headers, params=params)
businesses = response.json()["businesses"]
names = [business["name"]
         for business in businesses if business["rating"] > 4.5]
print(names)

"""
Output:
["Barber's Point", 'Soho NYC Barbers', '12 Pell', 'Hairrari East Village']
"""
