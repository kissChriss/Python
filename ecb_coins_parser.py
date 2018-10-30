from bs4 import BeautifulSoup as bs
from requests import *
import urllib.request
import re
import os

def get_html(url):
    response = get(url)
    return response.text

def image_parse(soup):
	images = soup.find_all('div', class_='ecb-column')
	image_list = []
	for image in images:
		image_list.append('https://www.ecb.europa.eu' + image.find('img')['src'])
	return image_list

def name_folder(soup):
	name = soup.select_one('main').select_one('h1').text
	return name[:-1]
		
def main():
	countries_abbr = ['gr', 'ie', 'it', 'lv', 'lt', 'lu', 'mt', 'mo', 'nl', 'pt', 'sm', 'sk', 'sl', 'es', 'va']

	for country in countries_abbr:
		url = 'https://www.ecb.europa.eu/euro/coins/html/'+country+'.en.html'
		soup = bs(get_html(url), 'html.parser')    
	
		os.mkdir(name_folder(soup))

		for image in image_parse(soup):
			result = re.split(r'_', image, maxsplit=1)
			urllib.request.urlretrieve(image, "/Coins/"+name_folder(soup)+"/"+result[1])

if __name__ == '__main__':
	main()
