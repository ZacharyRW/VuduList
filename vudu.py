#Make sure to replace USERNAME and PASSWORD with your own username and password

#Import libraries
from bs4 import BeautifulSoup
from lxml import html
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv
import json
import re
import requests
import time
import urllib.request

#Login Information
USERNAME = "example@gmail.com"
PASSWORD = "example"

#URLs
login_url = "https://my.vudu.com/MyLogin.html?type=sign_in&url=https%3A%2F%2Fwww.vudu.com%2F"
url = "https://www.vudu.com/movies/#my_vudu/my_movies"

def main():
	session_requests = requests.session()

	chromedriver = 'C:\\chromedriver.exe'
	browser = webdriver.Chrome(chromedriver)
	browser.get('https://my.vudu.com/MyLogin.html?type=sign_in&url=https%3A%2F%2Fwww.vudu.com%2F')

	time.sleep(10)
	
	username = browser.find_element_by_name('email')
	password = browser.find_element_by_name('password')
	
	username.send_keys(USERNAME)
	password.send_keys(PASSWORD)
	
	browser.find_element_by_css_selector('.custom-button').click()
	
	html = urllib.request.urlopen(url)
	
	soup = BeautifulSoup(html, 'html.parser')
	
	name_box = soup.find('div', attrs={'class': 'gwt-Label title'})
	
	print (name_box)

if __name__ == '__main__':
	main()
