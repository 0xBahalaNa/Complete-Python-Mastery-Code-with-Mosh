"""
11. Popular Python Packages, 08. Browser Automation

https://selenium-python.readthedocs.io/

Automate opening a browser and logging into a website.
https://pypi.org/project/selenium/

For this tutorial, I will be using Google Chrome. 
"""
from selenium import webdriver

browser = webdriver.Chrome()
browser.get("https://github.com")

signin_link = browser.find_element("Sign in")
signin_link.click()

username_box = browser.find_element("login_field")
username_box.send_keys("")  # Insert username
password_box = browser.find_element("password")
password_box.send_keys("")  # Insert password
password_box.submit()

assert "" in browser.page_source  # Insert username

profile_link = browser.find_element_by_class_name("user-profile-link")
link_label = profile_link.get_attribute("innerHTML")

assert "" in link_label  # Insert username

browser.quit()
