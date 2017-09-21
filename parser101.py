# import libraries
import urllib2
import requests
from bs4 import BeautifulSoup

soup = BeautifulSoup("<html><p>This is <b>invalid HTML</p></html>", "html.parser")
print ('html.parser')
print(soup)
# <html><p>This is <b>invalid HTML</b></p></html>
print ('')

soup = BeautifulSoup("<html><p>This is <b>invalid HTML</p></html>", "lxml")
print ('lxml')
print(soup)
# <html><body><p>This is <b>invalid HTML</b></p></body></html>
print ('')

soup = BeautifulSoup("<html><p>This is <b>invalid HTML</p></html>", "xml")
print ('xml')
print(soup)
# <?xml version="1.0" encoding="utf-8"?>
# <html><p>This is <b>invalid HTML</b></p></html>
print('')

soup = BeautifulSoup("<html><p>This is <b>invalid HTML</p></html>", "html5lib")
print ('html5lib')
print(soup)
# <html><head></head><body><p>This is <b>invalid HTML</b></p></body></html>

print('')
print('')

req = requests.get('https://launch.pulsepoint.com/MarcusThomas-TravelLeaders')
soup = BeautifulSoup(req.text, "lxml")

print(soup.title)
print(soup.title.name)
print(soup.title.string)

script = soup.find_all("script")
print(script)
