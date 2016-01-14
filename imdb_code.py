# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 21:21:27 2015

@author: prakhar
"""

# Importing Packages
from bs4 import BeautifulSoup
from urllib2 import urlopen

# Parameters
# user_rating between ( 8.0 - 10 )
# title_type , release_date between ( 2013 - 2015 )
html_open = urlopen("http://www.imdb.com/search/title?release_date=2013-01-01,2015&title_type=feature&user_rating=8.0,10")
html_text = html_open.read()

soup = BeautifulSoup(html_text)

print "------------------------------------\nMovie Name | Year | Rating | Minutes\n-----------------------------------"

for i in soup.find_all('td','title'):
    title = i.find('a').contents[0]
    runtime = i.find('span','runtime')
    ratings = i.find('span','rating-rating').find('span','value').contents[0]
    year = i.find('span','year_type').contents[0]
    if runtime != None:
        runtime = runtime.contents[0]
        print title,"|",year,"|",ratings,"|",runtime
    
