#Import libraries
from bs4 import BeautifulSoup
from lxml import html
import csv
import json
import re
import requests
import urllib.request

#Login Information
USERNAME = "zachary.r.williams@gmail.com"
PASSWORD = "wp5AQNpF2HDsAj"

#URLs
login_url = "https://my.vudu.com/MyLogin.html?type=sign_in&url=https%3A%2F%2Fwww.vudu.com%2F"
url = "https://www.vudu.com/movies/#my_vudu/my_movies"

def main():
	session_requests = requests.session()

	#Create payload
	payload = {
		"Email": USERNAME, 
		"Password": PASSWORD, 
	}
	
	#Perform login
	result = session_requests.post(login_url, data = payload, headers = dict(referer=login_url))
	
	html = urllib.request.urlopen(url)
	
	soup = BeautifulSoup(html, 'html.parser')
	
	name_box = soup.find('div', attrs={'class': 'gwt-Label title'})
	
	print (name_box)

if __name__ == '__main__':
	main()