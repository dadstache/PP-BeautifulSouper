# import libraries
import urllib2
from bs4 import BeautifulSoup

#specify the URL
quote_page = 'https://launch.pulsepoint.com/MarcusThomas-TravelLeaders/index.html'

#query the website and return the html to the variable 'page'
page = urllib2.urlopen(quote_page)

#parse the html using beautiful soup and store in variable 'soup'
soup = BeautifulSoup(page, 'html.parser')

#Take our the <div>
script_box = soup.find('script', attrs={'type': 'text/javascript'})
script = script_box.text.strip() #strip() is used to remove starting and trailing
print script
