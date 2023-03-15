"""
11. Popular Python Packages, 07. Web Scraping

Not every website has an API. 
Parsing the data wanted is called web scraping. 
In this tutorial, a program will be written to extract the newest questions on stackoverflow.
Import beautifulsoup4 and requests
"""
from bs4 import BeautifulSoup
import requests

response = requests.get("https://stackoverflow.com/questions")
soup = BeautifulSoup(response.text, "html.parser")

questions = soup.select(".question-summary")

for question in questions:
    print(question.select_one(".question-hyperlink").getText())
    print(question.select_one(".vote-count-post").getText())
