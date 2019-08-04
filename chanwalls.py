import os
import requests
import urllib.request
from bs4 import BeautifulSoup

# takes the url for the thread you wanted to download the images from
# make sure that the url has the protocol thingy as the prefix
thread_url = input("Enter the url for the thread: ")

response = requests.get(thread_url)

soup = BeautifulSoup(response.text, "html.parser")

# thread_name used to create folder for storing the corresponding images
thread_name = soup.find('span', {'class': 'subject'}).string
images = soup.findAll('a', {'class': 'fileThumb'})

# creates the folder
os.mkdir(thread_name)

for img in images:
	# gets image name from the last part of href
	img_name = img.get('href').split('/')
	urllib.request.urlretrieve('https:'+img.get('href'), os.path.join(thread_name, img_name[-1]))
